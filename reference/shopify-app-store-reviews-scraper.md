# Shopify App Store Reviews Scraper: Every Review, No Cap

`wulfcare/shopify-app-store-reviews-scraper`: Scrape every review of any Shopify App Store app: stars, text, date, the merchant's store name and country, time using the app and the developer's reply. Star and date filters. $0.03 per 1,000 reviews, no start fee, errors free.

**Use it for:**
- every review of a Shopify App Store app with stars, date, merchant store and country, time using the app and developer reply

- Store page: https://apify.com/wulfcare/shopify-app-store-reviews-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~shopify-app-store-reviews-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/shopify-app-store-reviews-scraper`

**Price:**
- $0.000025 per review (review): One Shopify App Store review with stars, text, date, the store name and country, and the developer reply. Apps not found and failed requests are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~shopify-app-store-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"apps": ["judgeme"], "maxReviewsPerApp": 200}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/shopify-app-store-reviews-scraper").call(run_input={"apps": ["judgeme"], "maxReviewsPerApp": 200})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `apps` | array | yes |  |  | Apps: Shopify App Store apps: the handle from the app's URL (judgeme for apps.shopify.com/judgeme) or the full URL. Every review of each app is fetched, up to the limit below. |
| `maxReviewsPerApp` | integer |  | 1000 | 0– | Maximum reviews per app: 0 = every review the app has (the biggest apps have 50,000+). |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `relevant` (Most relevant (Shopify's default)) | Order: Newest first can also stop at a date (below). |
| `reviewStars` | array |  |  |  | Star ratings: Only reviews with these ratings, e.g. 1 and 2 for complaints. Filtered on Shopify's side, so you only pay for the reviews you want. Empty = all. |
| `reviewsSince` | string |  |  |  | Only reviews since: Skip reviews older than this, e.g. 2026-09-01 or "30 days". The run stops as soon as it reaches older reviews (uses Newest first). |
| `maxConcurrency` | integer |  | 8 | 1–20 | Proxy IPs at a time: Review pages are spread over this many Apify Proxy IPs, each read at Shopify's polite rate. Ignored with the proxy off. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "appHandle": "judgeme",
  "appName": "Judge.me Product Reviews App",
  "developer": "Judge.me",
  "reviewId": "2420949",
  "rating": 1,
  "text": "Really complicated and you need to be a computer tech engineer to figure it out! Spent hours going around in circles....",
  "date": "2026-11-06",
  "edited": false,
  "storeName": "(removed)",
  "storeCountry": "United Kingdom",
  "timeUsingApp": "About 1 year using the app",
  "replyText": null,
  "replyDate": null,
  "reviewUrl": "https://apps.shopify.com/reviews/2420949",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
