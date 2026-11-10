# Google Trends Trending Now Scraper: Every Trending Search

`wulfcare/google-trends-trending-now`: Every search trending on Google right now, for any country: search volume, % increase, start time, related searches and news articles. 4/24/48/168-hour windows, categories, many countries per run. $0.30 per 1,000 trends, no start fee.

**Use it for:**
- every search trending on Google right now in one or many countries, with search volume, % increase, related searches and news
- cheapest way to get Trending Now only (no keyword reports)

- Store page: https://apify.com/wulfcare/google-trends-trending-now
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-trends-trending-now/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-trends-trending-now`

**Price:**
- $0.0003 per trending search (trending-item): One trending search from Trending Now, with volume, growth, related searches and category. Failed countries are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-trends-trending-now/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"trendingGeos": ["US"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-trends-trending-now").call(run_input={"trendingGeos": ["US"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `trendingGeos` | array |  |  |  | Countries or regions: ISO codes like US, GB, AU, or regions like US-CA. One set of trends per entry. |
| `trendingHours` | string |  | "24" | `4` (Past 4 hours), `24` (Past 24 hours), `48` (Past 48 hours), `168` (Past 7 days) | Time window: How far back to look for trending searches. |
| `trendingCategories` | array |  |  |  | Only these categories (optional): Leave empty for all categories. |
| `trendingActiveOnly` | boolean |  | false |  | Only trends that are still active: Skip trends that have already ended. |
| `maxTrendsPerGeo` | integer |  | 0 | 0– | Max trends per country (0 = all): Trends are sorted by search volume, highest first. |
| `language` | string |  | "en-US" |  | Interface language: Language of Google's labels and related queries, e.g. en-US, en-GB, de, ja. |
| `maxConcurrency` | integer |  | 3 | 1–10 | Parallel reports: How many reports run at once, each on its own IP. Only applies when using a proxy. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "type": "trendingNow",
  "title": "bills",
  "geo": "US",
  "windowHours": 24,
  "searchVolume": 1000000,
  "increasePercent": 1000,
  "startedAt": "2026-11-10T00:30:00+00:00",
  "endedAt": null,
  "isActive": true,
  "relatedSearches": [
    "bills",
    "vikings",
    "buffalo bills",
    "… 100 more"
  ],
  "categories": [
    "Sports"
  ],
  "categoryIds": [
    17
  ],
  "newsArticleCount": 0,
  "trendsUrl": "https://trends.google.com/trends/explore?q=bills&geo=US&date=now+1-d",
  "rank": 1
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
