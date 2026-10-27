"""Drop-in for youtube-transcript-api that doesn't get IP-blocked.

    from youtube_transcript_unblocked import YouTubeTranscriptApi   # was: from youtube_transcript_api import ...
    transcript = YouTubeTranscriptApi().fetch("dQw4w9WgXcQ")

Transcripts are fetched by the hosted Apify Actor wulfcare/youtube-transcript-scraper (it handles YouTube's
IP blocks), so this works from AWS, GCP, Azure and other servers. Needs an Apify API token in APIFY_TOKEN
(free account: https://console.apify.com/sign-up). $0.003 per transcript; videos without captions are free.

Results are youtube-transcript-api's own FetchedTranscript objects and errors are its own exception classes,
so existing code, `except` clauses and formatters keep working.
"""

from __future__ import annotations

import os
import re
import time
from typing import Dict, Iterable, List, Optional, Union

import requests
from youtube_transcript_api import FetchedTranscript, FetchedTranscriptSnippet
from youtube_transcript_api._errors import (AgeRestricted, CouldNotRetrieveTranscript, InvalidVideoId,
                                            NoTranscriptFound, RequestBlocked, TranscriptsDisabled,
                                            VideoUnavailable, VideoUnplayable, YouTubeTranscriptApiException)

__version__ = '0.1.0'
__all__ = ['YouTubeTranscriptApi', 'TranscriptInfo', 'ApifyError', 'FetchedTranscript', 'FetchedTranscriptSnippet']

ACTOR = 'wulfcare~youtube-transcript-scraper'
API = 'https://api.apify.com/v2'
SIGN_UP = 'https://console.apify.com/sign-up'
DONE = {'SUCCEEDED', 'FAILED', 'ABORTED', 'TIMED-OUT'}


class ApifyError(YouTubeTranscriptApiException):
    """The Apify API call itself failed (missing/invalid token, out of credit, network)."""


class _Failed(CouldNotRetrieveTranscript):
    """Any other reason the Actor gave for not returning a transcript."""

    def __init__(self, video_id: str, reason: str):
        self.reason = reason
        super().__init__(video_id)

    @property
    def cause(self) -> str:
        return self.reason


class TranscriptInfo:
    """One caption track a video has (what youtube-transcript-api's Transcript describes)."""

    def __init__(self, api: 'YouTubeTranscriptApi', video_id: str, language: str, language_code: str,
                 is_generated: bool):
        self._api, self.video_id = api, video_id
        self.language, self.language_code, self.is_generated = language, language_code, is_generated

    def fetch(self, preserve_formatting: bool = False) -> FetchedTranscript:
        return self._api.fetch(self.video_id, [self.language_code])

    def __repr__(self) -> str:
        return f'{self.language_code} ("{self.language}"){" [generated]" if self.is_generated else ""}'


def video_id_of(ref: str) -> str:
    """A video id from an id or any YouTube video URL."""
    m = re.search(r'(?:v=|youtu\.be/|shorts/|live/|embed/)([\w-]{11})', ref)
    return m.group(1) if m else ref.strip()


def _error(video_id: str, message: str, languages: Iterable[str]) -> CouldNotRetrieveTranscript:
    """The Actor's error row -> the matching youtube-transcript-api exception."""
    m = message.lower()
    if 'no captions' in m and 'neither' in m:
        return TranscriptsDisabled(video_id)
    if m.startswith('no ') and 'available:' in m:
        return NoTranscriptFound(video_id, list(languages), message)
    if m.startswith('video unavailable'):
        return VideoUnavailable(video_id)
    if m.startswith('age-restricted'):
        return AgeRestricted(video_id)
    if m.startswith('not a youtube'):
        return InvalidVideoId(video_id)
    if m.startswith('live stream'):
        return VideoUnplayable(video_id, message, [])
    if 'sign in to confirm' in m:
        return RequestBlocked(video_id)
    return _Failed(video_id, message)


class YouTubeTranscriptApi:
    """Same methods as youtube_transcript_api.YouTubeTranscriptApi (fetch, list), plus fetch_many for batches.

    api_token: Apify API token (default: the APIFY_TOKEN environment variable).
    max_cost_usd: optional spending cap per Actor run.
    proxy_config / http_client are accepted for compatibility and ignored: proxies are handled by the Actor.
    """

    def __init__(self, proxy_config=None, http_client=None, api_token: Optional[str] = None,
                 max_cost_usd: Optional[float] = None, timeout: float = 900):
        self.token = api_token or os.environ.get('APIFY_TOKEN') or os.environ.get('APIFY_API_TOKEN')
        if not self.token:
            raise ApifyError(f'Set the APIFY_TOKEN environment variable (or pass api_token=...). A free Apify '
                             f'account includes $5 of credit each month: {SIGN_UP}')
        self.max_cost_usd = max_cost_usd
        self.timeout = timeout
        self.http = requests.Session()
        self.http.headers['Authorization'] = f'Bearer {self.token}'

    # ---------------------------------------------------------------- Actor calls

    def _call(self, run_input: dict) -> List[dict]:
        params = {'waitForFinish': 60}
        if self.max_cost_usd:
            params['maxTotalChargeUsd'] = self.max_cost_usd
        r = self._req('POST', f'{API}/acts/{ACTOR}/runs', params=params, json=run_input)
        run, t0 = r['data'], time.monotonic()
        while run['status'] not in DONE:
            if time.monotonic() - t0 > self.timeout:
                raise ApifyError(f"Actor run {run['id']} still running after {self.timeout:.0f} s")
            run = self._req('GET', f"{API}/actor-runs/{run['id']}", params={'waitForFinish': 60})['data']
        items = self._req('GET', f"{API}/datasets/{run['defaultDatasetId']}/items", params={'clean': 1})
        if run['status'] != 'SUCCEEDED' and not items:
            raise ApifyError(f"Actor run {run['status']}: {run.get('statusMessage') or ''}".strip())
        return items

    def _req(self, method: str, url: str, **kw):
        for attempt in range(4):
            try:
                r = self.http.request(method, url, timeout=90, **kw)
            except requests.RequestException as e:
                err = ApifyError(f'Apify API unreachable: {e}')
            else:
                if r.status_code < 300:
                    return r.json()
                if r.status_code in (401, 403):
                    raise ApifyError(f'Apify refused the token (HTTP {r.status_code}). Get yours at '
                                     'https://console.apify.com/settings/integrations')
                if r.status_code == 402:
                    raise ApifyError('Apify account is out of credit (HTTP 402).')
                err = ApifyError(f'Apify API HTTP {r.status_code}: {r.text[:200]}')
                if r.status_code < 500 and r.status_code != 429:
                    raise err
            time.sleep(2 * (attempt + 1))
        raise err

    def _rows(self, video_ids: List[str], languages: Iterable[str]) -> Dict[str, dict]:
        rows = self._call({'urls': video_ids, 'languages': list(languages), 'ifLanguageMissing': 'skip',
                           'includeSegments': True, 'includePublishDate': False, 'includeDescription': False,
                           'maxConcurrency': 5})
        return {r.get('videoId') or video_id_of(r.get('input') or ''): r for r in rows}

    @staticmethod
    def _transcript(vid: str, row: dict) -> FetchedTranscript:
        name = row.get('languageName') or row.get('language') or ''
        return FetchedTranscript(
            snippets=[FetchedTranscriptSnippet(text=s['text'], start=s['start'], duration=s['duration'])
                      for s in row.get('segments') or []],
            video_id=vid,
            language=f'{name} (auto-generated)' if row.get('isAutoGenerated') else name,
            language_code=row.get('language') or '',
            is_generated=bool(row.get('isAutoGenerated')),
        )

    # ---------------------------------------------------------------- public API

    def fetch(self, video_id: str, languages: Iterable[str] = ('en',),
              preserve_formatting: bool = False) -> FetchedTranscript:
        """The transcript in the first of `languages` the video has (creator captions before auto-generated)."""
        vid = video_id_of(video_id)
        languages = list(languages)
        row = self._rows([vid], languages).get(vid)
        if not row:
            raise _Failed(vid, 'The Actor returned no result for this video')
        if row.get('error'):
            raise _error(vid, row['error'], languages)
        return self._transcript(vid, row)

    def fetch_many(self, video_ids: Iterable[str], languages: Iterable[str] = ('en',)
                   ) -> Dict[str, Union[FetchedTranscript, CouldNotRetrieveTranscript]]:
        """Many videos in ONE Actor run (faster and cheaper than one fetch per video).
        Returns {video_id: FetchedTranscript or the exception for that video}."""
        ids = list(dict.fromkeys(video_id_of(v) for v in video_ids))
        languages = list(languages)
        rows = self._rows(ids, languages)
        out = {}
        for vid in ids:
            row = rows.get(vid)
            if not row:
                out[vid] = _Failed(vid, 'The Actor returned no result for this video')
            elif row.get('error'):
                out[vid] = _error(vid, row['error'], languages)
            else:
                out[vid] = self._transcript(vid, row)
        return out

    def list(self, video_id: str) -> List[TranscriptInfo]:
        """The caption tracks the video has. Costs one transcript ($0.003): it fetches the original-language one."""
        vid = video_id_of(video_id)
        rows = self._call({'urls': [vid], 'languages': [], 'includeSegments': False, 'includePublishDate': False,
                           'includeDescription': False})
        row = next((r for r in rows if r.get('videoId') == vid), None)
        if not row:
            raise _Failed(vid, 'The Actor returned no result for this video')
        if row.get('error') and not row.get('availableLanguages'):
            raise _error(vid, row['error'], [])
        return [TranscriptInfo(self, vid, t['name'], t['language'], t['isAutoGenerated'])
                for t in row.get('availableLanguages') or []]

    # ---------------------------------------------------------------- youtube-transcript-api 0.x style

    @classmethod
    def get_transcript(cls, video_id: str, languages: Iterable[str] = ('en',), proxies=None, cookies=None,
                       preserve_formatting: bool = False) -> List[dict]:
        """Old (0.x) API: a list of {'text', 'start', 'duration'} dicts."""
        return cls().fetch(video_id, languages).to_raw_data()

    @classmethod
    def get_transcripts(cls, video_ids: Iterable[str], languages: Iterable[str] = ('en',),
                        continue_after_error: bool = False, proxies=None, cookies=None,
                        preserve_formatting: bool = False):
        """Old (0.x) API: ({video_id: [dicts]}, [video ids that failed])."""
        got, failed = {}, []
        for vid, t in cls().fetch_many(video_ids, languages).items():
            if isinstance(t, Exception):
                if not continue_after_error:
                    raise t
                failed.append(vid)
            else:
                got[vid] = t.to_raw_data()
        return got, failed
