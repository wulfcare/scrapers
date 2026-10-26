# pytrends alternative: fix `429 Too Many Requests` (Google Trends API for Python)

If you use [pytrends](https://github.com/GeneralMills/pytrends) you've probably seen this:

```
pytrends.exceptions.TooManyRequestsError: The request failed: Google returned a response with code 429
```

**Why it happens:** pytrends sends every request from your own IP address. Google Trends rate-limits an IP after a handful of requests, and then answers everything with HTTP 429. `sleep()`, `retries=` and `backoff_factor=` only slow it down, and cloud servers (Colab, AWS, GitHub Actions) are often blocked from the first request. pytrends itself is **archived** and no longer maintained.

**The fix:** [`pytrends_alternative.py`](pytrends_alternative.py) keeps the pytrends interface but runs each query on the [Google Trends Scraper on Apify](https://apify.com/wulfcare/google-trends-scraper), which spreads requests over many IP addresses, paces each one, and swaps an IP out the moment Google returns 429. Your code changes by one import.

```python
# from pytrends.request import TrendReq
from pytrends_alternative import TrendReq

pytrends = TrendReq(hl="en-US", tz=360)
pytrends.build_payload(["coffee", "tea"], timeframe="today 12-m", geo="US")

pytrends.interest_over_time()                       # DataFrame: date index, one column per keyword, isPartial
pytrends.interest_by_region(resolution="REGION")    # DataFrame: one row per state
pytrends.related_queries()                          # {"coffee": {"top": DataFrame, "rising": DataFrame}, ...}
```

## Setup

```bash
pip install apify-client pandas
export APIFY_TOKEN=your_token   # free account: https://console.apify.com/sign-up, token under Settings → API & Integrations
```

Then copy `pytrends_alternative.py` next to your code.

## Two things pytrends can't do

**More than 5 keywords on one scale.** Google compares at most 5 terms, and each comparison has its own 0–100 scale, so batches of 5 can't be put side by side. Pass up to 100 keywords and they come back on one scale, ranked:

```python
pytrends.build_payload(["coffee", "tea", "matcha", "espresso", "latte", "chai", "kombucha"], timeframe="today 12-m", geo="US")
pytrends.ranking()
```

```
   rank      term   vsTop  lowPrecision
0     1    coffee  1.0000         False
1     2       tea  0.4673         False
2     3  espresso  0.1239         False
3     4    matcha  0.0798         False
4     5     latte  0.0675         False
5     6      chai  0.0386         False
6     7  kombucha  0.0139         False
```

(Real output, US, past 12 months.) Terms are compared in overlapping groups of 5 that share a term, then chained onto one scale, the anchor method from the [G-TAB paper](https://arxiv.org/abs/2007.13861).

**Daily data for any range.** Google gives daily points only for ranges under ~9 months, then weekly, then monthly. Add `daily=True` to get one point per day for 12 months, 5 years or 2004 to now:

```python
pytrends.build_payload(["bitcoin"], timeframe="today 5-y", daily=True)
pytrends.interest_over_time()   # ~1,826 daily rows
```

Accuracy, from real runs: daily data summed into weeks matched Google's own weekly series with 0.99 correlation. These combined numbers are **estimates** built from several Google queries, not Google's published numbers; check anything important before you rely on it.

## Same thing without pytrends

Any language, plain HTTP:

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-trends-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["coffee, tea"], "geo": "US", "timeRange": "today 12-m"}'
```

Or with the generic helper in this repo:

```python
from wulfcare import run
report = run("wulfcare/google-trends-scraper", {"searchTerms": ["coffee, tea"], "geo": "US"})[0]
report["interestOverTime"], report["interestByRegion"], report["relatedQueries"]
```

Trending Now (what's trending in a country right now, with search volume):

```python
pytrends.trending_now(geo="US", hours=24)
```

## Cost

Pay per report: **$0.003 per report** (interest over time + regions + related queries for up to 5 terms). More than 5 keywords or daily data use one report per Google query needed: 12 keywords ≈ 6 reports, daily data for 5 years = 10. Failed queries are never charged. Apify's free plan includes $5 of credit every month, about 1,600 reports. Calling `interest_by_region()` with a different `resolution` than the first call runs one more report.

## pytrends → this, quick map

| pytrends | here | notes |
|---|---|---|
| `TrendReq(hl, tz, timeout, proxies, retries, backoff_factor)` | `TrendReq(hl, tz)` | proxy/retry options accepted and ignored: handled for you |
| `build_payload(kw_list, cat, timeframe, geo, gprop)` | same, plus `daily=True` | up to 100 keywords |
| `interest_over_time()` | same | |
| `interest_by_region(resolution, inc_low_vol, inc_geo_code)` | same | up to 5 keywords |
| `related_queries()` | same | |
| `related_topics()` | not available | Google no longer returns related topics to logged-out sessions |
| `trending_searches()` / `realtime_trending_searches()` | `trending_now(geo, hours)` | |
| — | `ranking()` | new: every keyword on one scale |

Full input options: [apify.com/wulfcare/google-trends-scraper](https://apify.com/wulfcare/google-trends-scraper).
