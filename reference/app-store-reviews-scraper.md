# App Store Reviews Scraper: All Reviews, No 500 Cap

`wulfcare/app-store-reviews-scraper`: Scrape every Apple App Store review of any app, with no 500 cap: any country, newest/helpful/critical sort, star and date filters, developer replies and app versions. $0.10 per 1,000 reviews, no start fee, errors free.

**Use it for:**
- all Apple App Store reviews of an app (more than 500, any country)

- Store page: https://apify.com/wulfcare/app-store-reviews-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~app-store-reviews-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/app-store-reviews-scraper`

**Price:**
- $0.0001 per review (review): One App Store review with stars, title, text, date, the developer reply and (for recent reviews) the app version. Not-found apps and failed requests are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~app-store-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"appIds": ["324684580"], "countries": ["us"], "maxReviewsPerApp": 1000}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/app-store-reviews-scraper").call(run_input={"appIds": ["324684580"], "countries": ["us"], "maxReviewsPerApp": 1000})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `appIds` | array | yes |  |  | Apps: App Store URLs (https://apps.apple.com/us/app/.../id324684580), numeric app ids (324684580) or bundle ids (com.spotify.client). Every review of each app is fetched, up to the limit below. |
| `countries` | array |  | ["us"] |  | Countries: Two-letter App Store country codes (us, gb, de, jp, br, ...). Each country is its own store with its own reviews, prices, charts and search results; add several to cover them all in one run. Every row says which country it came from. |
| `maxReviewsPerApp` | integer |  | 100 | 0– | Max reviews per app: 0 = every review the App Store has for the app in each country (no 500 cap). With a star filter, this counts only reviews with those stars. |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `helpful` (Most helpful (App Store default)), `favorable` (Most favorable (5 stars first)), `critical` (Most critical (1 star first)) | Sort reviews by: Newest first is best for monitoring and date cutoffs. Most critical is the fastest way to get complaints. |
| `reviewStars` | array |  |  |  | Only these star ratings: Leave empty for all ratings. You're only charged for reviews with these stars. Tip: with Most critical (or Most favorable) the run stops as soon as it's past the stars you picked. |
| `reviewsSince` | string |  |  |  | Only reviews since: Skip reviews older than this, e.g. 2026-09-01 or "30 days". With Newest first the run stops as soon as it reaches older reviews. |
| `includeReviewerNames` | boolean |  | false |  | Include reviewer nicknames: Off by default. The App Store shows a nickname for each reviewer; no other reviewer data is collected. |
| `maxConcurrency` | integer |  | 6 | 1–20 | Parallel connections: How many IPs requests are spread over (the run's own IP plus proxy sessions). More is faster for very large review pulls. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "appId": "324684580",
  "appTitle": "Spotify: Music and Podcasts",
  "reviewId": "14709146123",
  "score": 1,
  "title": "Ads ruined it",
  "text": "I’ve been using Spotify for almost 5 years and never rlly had much of a problem. Ads would come on every like 3-4 songs and I just accepted that bc it seemed fair. But the past 2 weeks there’s 3 ads after EVERY song to a point where I’ve go…",
  "date": "2026-10-25T11:17:54Z",
  "isEdited": false,
  "appVersion": "9.1.94",
  "replyText": null,
  "replyDate": null,
  "userName": null,
  "appUrl": "https://apps.apple.com/us/app/id324684580",
  "country": "US",
  "language": null,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
