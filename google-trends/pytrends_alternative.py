"""A pytrends-style Google Trends client that doesn't hit 429 Too Many Requests.

pytrends talks to Google from your own IP, so after a few requests Google answers 429 and
pytrends raises `TooManyRequestsError: The request failed: Google returned a response with
code 429`. pytrends is also archived and no longer maintained.

This module keeps the pytrends interface (build_payload, interest_over_time,
interest_by_region, related_queries) but runs each query on the Google Trends Scraper on
Apify (https://apify.com/wulfcare/google-trends-scraper), which paces requests over many
IPs and swaps an IP out the moment Google rate-limits it. It also removes two Google limits:
more than 5 keywords on one 0-100 scale, and daily data for any time range.

    pip install apify-client pandas
    export APIFY_TOKEN=...   # free account: https://console.apify.com/sign-up

    from pytrends_alternative import TrendReq
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload(["coffee", "tea"], timeframe="today 12-m", geo="US")
    df = pytrends.interest_over_time()
"""

from __future__ import annotations

import os

import pandas as pd
from apify_client import ApifyClient

ACTOR = "wulfcare/google-trends-scraper"
PRESETS = {"now 1-H", "now 4-H", "now 1-d", "now 7-d", "today 1-m", "today 3-m", "today 12-m", "today 5-y", "all"}


class TrendsError(Exception):
    pass


class TrendReq:
    def __init__(self, hl: str = "en-US", tz: int = 0, token: str | None = None, **_ignored):
        # pytrends options such as timeout, proxies, retries and backoff_factor are accepted and
        # ignored: pacing, retries and proxies are handled on Apify's side.
        self.hl = hl
        self.tz = tz
        self.client = ApifyClient(token or os.environ["APIFY_TOKEN"])
        self.kw_list: list[str] = []
        self._cache: dict[tuple, dict] = {}

    def build_payload(self, kw_list, cat=0, timeframe="today 5-y", geo="", gprop="", daily=False):
        """Same arguments as pytrends, plus `daily=True` for one point per day over any range.

        kw_list can hold up to 100 keywords (Google's own limit is 5); they all come back on one scale.
        """
        self.kw_list = list(kw_list)
        self.cat, self.timeframe, self.geo, self.gprop, self.daily = cat, timeframe, geo, gprop, daily

    def _report(self, resolution: str = "", inc_low_vol: bool = False) -> dict:
        key = (tuple(self.kw_list), self.cat, self.timeframe, self.geo, self.gprop, self.daily, resolution, inc_low_vol)
        if key not in self._cache:
            run_input = {
                "mode": "explore",
                "searchTerms": [", ".join(self.kw_list)],
                "geo": self.geo,
                "category": self.cat,
                "searchProperty": self.gprop,
                "dailyData": self.daily,
                "regionResolution": resolution,
                "includeLowVolumeRegions": inc_low_vol,
                "language": self.hl,
                "timezoneOffsetMinutes": self.tz,
                "saveCsv": False,
            }
            if self.timeframe in PRESETS:
                run_input["timeRange"] = self.timeframe
            else:  # "2024-01-01 2024-06-30"
                run_input["customTimeRange"] = self.timeframe
            items = _items(self.client, run_input)
            if not items:
                raise TrendsError("no result returned")
            if items[0].get("error"):
                raise TrendsError(items[0]["error"])
            self._cache[key] = items[0]
        return self._cache[key]

    def interest_over_time(self) -> pd.DataFrame:
        """DataFrame indexed by date, one column per keyword (0-100), plus isPartial. Same shape as pytrends."""
        rows = self._report().get("interestOverTime") or []
        if not rows:
            return pd.DataFrame()
        df = pd.DataFrame([{**r["values"], "isPartial": r.get("isPartial", False)} for r in rows],
                          index=pd.to_datetime([r["date"] for r in rows], utc=True).tz_localize(None))
        df.index.name = "date"
        return df

    def ranking(self) -> pd.DataFrame:
        """For more than 5 keywords: every keyword ranked on the shared scale (not in pytrends)."""
        return pd.DataFrame(self._report().get("ranking") or [])

    def interest_by_region(self, resolution: str = "COUNTRY", inc_low_vol: bool = False, inc_geo_code: bool = False) -> pd.DataFrame:
        """resolution: COUNTRY, REGION, CITY or DMA, as in pytrends. Up to 5 keywords per payload."""
        rows = self._report(resolution, inc_low_vol).get("interestByRegion") or []
        df = pd.DataFrame([{"geoName": r["geoName"], "geoCode": r.get("geoCode"), **r["values"]} for r in rows])
        if df.empty:
            return df
        df = df.set_index("geoName")
        return df if inc_geo_code else df.drop(columns="geoCode")

    def related_queries(self) -> dict:
        """{keyword: {"top": DataFrame(query, value), "rising": DataFrame(query, value)}}, as in pytrends."""
        out = {}
        for kw, lists in (self._report().get("relatedQueries") or {}).items():
            out[kw] = {k: _queries(lists.get(k)) for k in ("top", "rising")}
        return out

    def trending_now(self, geo: str = "US", hours: int = 24) -> pd.DataFrame:
        """Google's Trending Now list (the page that replaced Google's daily search trends)."""
        items = _items(self.client, {"mode": "trendingNow", "trendingGeos": [geo], "trendingHours": str(hours)})
        return pd.DataFrame(items)


def _queries(rows) -> pd.DataFrame | None:
    # pytrends returns None, not an empty DataFrame, when Google has no related queries.
    if not rows:
        return None
    return pd.DataFrame([{"query": q["query"], "value": q["value"]} for q in rows])


def _items(client: ApifyClient, run_input: dict) -> list[dict]:
    result = client.actor(ACTOR).call(run_input=run_input)
    if result is None:
        raise TrendsError("run did not start")
    dataset_id = result["defaultDatasetId"] if isinstance(result, dict) else result.default_dataset_id
    return list(client.dataset(dataset_id).iterate_items())


if __name__ == "__main__":
    pytrends = TrendReq()
    pytrends.build_payload(["coffee", "tea", "matcha", "espresso", "latte", "chai", "kombucha"], timeframe="today 12-m", geo="US")
    print(pytrends.ranking()[["rank", "term", "vsTop"]])
    print(pytrends.interest_over_time().tail())
