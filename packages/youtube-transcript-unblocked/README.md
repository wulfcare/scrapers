# youtube-transcript-unblocked

**Getting `IpBlocked` or `RequestBlocked` from youtube-transcript-api on your server? Change one import.**

```
youtube_transcript_api._errors.RequestBlocked: Could not retrieve a transcript for the video ...
YouTube is blocking requests from your IP. ... You are doing requests from an IP belonging to a cloud provider (like AWS, Google Cloud Platform, Azure, etc.)
```

```bash
pip install youtube-transcript-unblocked
export APIFY_TOKEN=apify_api_...   # free account: https://console.apify.com/sign-up ($5 free credit/month)
```

```python
# from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_unblocked import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch("UF8uR6Z6KLc", languages=["en"])
for snippet in transcript:
    print(snippet.start, snippet.text)
```

That's the whole change. You get youtube-transcript-api's own objects (`FetchedTranscript`, `FetchedTranscriptSnippet`, `.to_raw_data()`) and its own exceptions (`TranscriptsDisabled`, `NoTranscriptFound`, `VideoUnavailable`, `AgeRestricted`, ...), so your `except` clauses and its formatters keep working:

```python
from youtube_transcript_api.formatters import SRTFormatter
print(SRTFormatter().format_transcript(transcript))
```

## How it works

Transcripts are fetched by a hosted [Apify Actor, wulfcare/youtube-transcript-scraper](https://apify.com/wulfcare/youtube-transcript-scraper), which handles YouTube's IP blocks: it paces requests per IP, finds IPs YouTube accepts, and switches to residential proxies when datacenter IPs are refused. Your code only talks to the Apify API, so it runs the same from a laptop, AWS Lambda, GCP, Azure, Docker or CI.

Measured 2026-10-28: 150 separate one-video calls, mixed content: every video that has captions returned a transcript, median 6.8 s per call.

## Many videos at once

`fetch_many` sends a whole list in **one** Actor run (faster and cheaper than one call per video):

```python
results = ytt_api.fetch_many(["UF8uR6Z6KLc", "dQw4w9WgXcQ", "jNQXAC9IVRw"], languages=["en", "de"])
for video_id, t in results.items():
    if isinstance(t, Exception):
        print(video_id, "failed:", type(t).__name__)
    else:
        print(video_id, t.language_code, len(t), "lines")
```

## Supported API

| youtube-transcript-api | here |
|---|---|
| `YouTubeTranscriptApi().fetch(video_id, languages=["en"])` | same |
| `YouTubeTranscriptApi().list(video_id)` | returns the caption tracks (`language`, `language_code`, `is_generated`, `.fetch()`); costs one transcript |
| `YouTubeTranscriptApi.get_transcript(...)` / `get_transcripts(...)` (0.x API) | same |
| `proxy_config=...`, `http_client=...` | accepted and ignored (not needed) |
| `translate()` | not supported (YouTube's own caption languages only) |
| — | `fetch_many(video_ids, languages)` batch call |

Video URLs work as well as ids. Options: `YouTubeTranscriptApi(api_token="...", max_cost_usd=1.0)` (spending cap per run).

## Cost

**$0.003 per transcript** ($3 per 1,000), billed by Apify from your account, plus a tiny platform fee per call (about $0.0002). Videos without captions, unavailable videos and invalid ids are free. Apify's free plan includes $5 of credit each month.

## More

Channels, playlists, searches, SRT and timestamped text: call the [Actor](https://apify.com/wulfcare/youtube-transcript-scraper) directly. Other scrapers (Google Trends, App Store, Google Play, ...): [github.com/wulfcare/scrapers](https://github.com/wulfcare/scrapers).

Not affiliated with youtube-transcript-api or YouTube; it uses youtube-transcript-api's classes so your code doesn't change. MIT licensed.
