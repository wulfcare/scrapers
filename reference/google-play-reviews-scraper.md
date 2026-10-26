# Google Play Reviews Scraper: All Reviews, No Cap

`wulfcare/google-play-reviews-scraper`: Scrape every Google Play review of any app, with no 150/1,000 cap: newest or most relevant, star and date filters, helpful votes, app versions and developer replies, any country and language. $0.10 per 1,000 reviews, no start fee, errors free.

**Use it for:**
- all Google Play reviews of an app, any country and language

- Store page: https://apify.com/wulfcare/google-play-reviews-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-play-reviews-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-play-reviews-scraper`

**Price:**
- $0.0001 per review (review): One Google Play review with stars, text, date, helpful votes, the app version and the developer reply. Not-found apps and failed requests are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-play-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"appIds": ["com.spotify.music"], "country": "us", "maxReviewsPerApp": 1000}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-play-reviews-scraper").call(run_input={"appIds": ["com.spotify.music"], "country": "us", "maxReviewsPerApp": 1000})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `appIds` | array | yes |  |  | Apps: Package names (com.spotify.music) or Google Play URLs (https://play.google.com/store/apps/details?id=com.spotify.music). Every review of each app is fetched, up to the limit below. |
| `country` | string |  | "us" |  | Country: Two-letter country code (us, gb, de, in, ng, br, ...). Prices, availability, charts and search results follow this country. |
| `language` | string |  | "en" |  | Language: Language code (en, de, es, pt-BR, ...). Google Play returns reviews written in this language, and app texts in it when the developer provides a translation. |
| `maxReviewsPerApp` | integer |  | 100 | 0– | Max reviews per app: 0 = every review Google Play has (it pages through them all). With a star filter the limit applies to each star rating separately. |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `relevant` (Most relevant (Play default)) | Sort reviews by: Newest first is best for monitoring and date cutoffs. |
| `reviewStars` | array |  |  |  | Only these star ratings: Leave empty for all ratings. Filtering happens on Google Play's side, so asking for 1-star reviews doesn't cost you the others. |
| `reviewsSince` | string |  |  |  | Only reviews since: Stop at reviews older than this date, e.g. 2026-09-01 or "30 days". Fastest with "Newest first". |
| `includeReviewerNames` | boolean |  | false |  | Include reviewer display names: Off by default. Reviewer ids and profile pictures are never collected. |
| `maxConcurrency` | integer |  | 5 | 1–20 | Parallel requests: How many apps or searches are fetched at the same time. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "appId": "com.spotify.music",
  "appTitle": "Spotify: Music and Podcasts",
  "reviewId": "dfe3987b-e7ce-4cae-a7d0-d4988e3b848b",
  "reviewUrl": "https://play.google.com/store/apps/details?id=com.spotify.music&reviewId=dfe3987b-e7ce-4cae-a7d0-d4988e3b848b&hl=en&gl=us",
  "score": 4,
  "text": "If you have Spotify Premium, this is a great app; unlimited downloads, no ads, and a monthly hour rate to listen to many audiobooks free. Great for music, podcasts, ASMR, etc. However, without Spotify Premium there is an unattractive amount…",
  "date": "2026-10-24T09:52:29Z",
  "thumbsUp": 0,
  "appVersion": "9.1.92.3058",
  "replyText": null,
  "replyDate": null,
  "country": "US",
  "language": "en",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
