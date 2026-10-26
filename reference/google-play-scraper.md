# Google Play Scraper: Reviews, App Details, Search & Charts

`wulfcare/google-play-scraper`: Scrape Google Play reviews (unlimited, any country and language, star and date filters), full app details with data safety and developer contacts, search results, top charts, developer apps and similar apps. Missing apps never crash a run.

**Use it for:**
- Google Play app details incl. data safety, installs, developer contacts
- Google Play search results, top charts, developer apps, similar apps
- Google Play reviews together with app data

- Store page: https://apify.com/wulfcare/google-play-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-play-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-play-scraper`

**Price:**
- $0.0001 per review (review): One Google Play review with stars, text, date, helpful votes, app version and the developer reply. Not-found apps and failed requests are never charged.
- $0.0005 per app details (app-details): Full details of one app: ratings histogram, installs, price, developer contact, permissions, data safety, version and more.
- $0.0002 per app in a list (app-list-item): One app from a search, top chart, developer page or similar-apps list, with title, rating, installs, price and category.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-play-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode": "apps", "appIds": ["com.spotify.music"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-play-scraper").call(run_input={"mode": "apps", "appIds": ["com.spotify.music"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `mode` | string | yes | "reviews" | `reviews` (Reviews of apps), `apps` (App details (full)), `search` (Search results), `charts` (Top charts), `developer` (Apps by developer), `similar` (Similar apps) | What to scrape: Each run returns one kind of row, so your dataset always has the same columns. Reviews and App details use the app list below; the other modes use their own section. |
| `appIds` | array |  |  |  | Apps: Package names (com.spotify.music) or Google Play URLs (https://play.google.com/store/apps/details?id=com.spotify.music). Used by Reviews, App details and Similar apps. |
| `country` | string |  | "us" |  | Country: Two-letter country code (us, gb, de, in, ng, br, ...). Prices, availability, charts and search results follow this country. |
| `language` | string |  | "en" |  | Language: Language code (en, de, es, pt-BR, ...). Google Play returns reviews written in this language, and app texts in it when the developer provides a translation. |
| `maxReviewsPerApp` | integer |  | 100 | 0– | Max reviews per app: 0 = every review Google Play has (it pages through them all). With a star filter the limit applies to each star rating separately. |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `relevant` (Most relevant (Play default)) | Sort reviews by: Newest first is best for monitoring and date cutoffs. |
| `reviewStars` | array |  |  |  | Only these star ratings: Leave empty for all ratings. Filtering happens on Google Play's side, so asking for 1-star reviews doesn't cost you the others. |
| `reviewsSince` | string |  |  |  | Only reviews since: Stop at reviews older than this date, e.g. 2026-09-01 or "30 days". Fastest with "Newest first". |
| `includeReviewerNames` | boolean |  | false |  | Include reviewer display names: Off by default. Reviewer ids and profile pictures are never collected. |
| `searchQueries` | array |  |  |  | Search terms: One search per line, e.g. "budget tracker". Google Play's website shows up to about 30 apps per search. |
| `chartCollections` | array |  | ["topselling_free"] |  | Charts: Which top charts to fetch (up to 200 apps each). |
| `chartCategories` | array |  | ["APPLICATION"] |  | Chart categories: Every chart is fetched for every category picked here. |
| `developers` | array |  |  |  | Developers: Developer names exactly as on Google Play ("Spotify AB"), numeric developer ids, or developer page URLs. |
| `maxResults` | integer |  | 0 | 0– | Max apps per search / chart / developer: 0 = everything Google Play shows (search ~30, charts 200, similar ~50). |
| `includeFullDetails` | boolean |  | false |  | Full details for every listed app: Search, charts, developer and similar modes return a compact card by default. Turn this on to get the full App details row (ratings histogram, developer contact, data safety, ...) for each app, charged as an app detail. |
| `includeDataSafety` | boolean |  | true |  | Include data safety section: What data the app collects and shares, for what purpose, and its security practices. Free, it comes with the same request. |
| `includeDescriptionHtml` | boolean |  | false |  | Also include description HTML: The plain-text description is always included. Turn on to also get the original HTML. |
| `maxConcurrency` | integer |  | 5 | 1–20 | Parallel requests: How many apps or searches are fetched at the same time. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "input": "Top free · APPLICATION",
  "rank": 1,
  "appId": "com.facebook.aura",
  "url": "https://play.google.com/store/apps/details?id=com.facebook.aura&hl=en&gl=us",
  "title": "Muse from Meta",
  "developer": "Meta Platforms, Inc.",
  "score": 4.7098,
  "genre": "Productivity",
  "installs": "5,000,000+",
  "free": true,
  "price": 0,
  "currency": "USD",
  "priceText": "Free",
  "inAppPurchasesRange": "$0.99 - $1,049.00 per item",
  "contentRating": "Teen",
  "summary": null,
  "description": "Muse is your personal AI agent that gets things done, always working on what matters to you. It manages email, books dinners, tracks budgets, and finds deals, with your approval.\n\nPERSONAL PRODUCTIVITY\nMuse takes the the busywork off your p…",
  "icon": "https://play-lh.googleusercontent.com/qDQUfohqN-eZh_a_YuWYlTsBPwjgrayoh2-Nf9o49kzN5Yjwk4yTyNUIFRI3o3PYks5lVAgEPrEPvFRYqxLP",
  "screenshots": [
    "https://play-lh.googleusercontent.com/R7pQ9kQjhDBbsreE7p2M4D91O7AuoRgmy91lKrPQ24Ey6dTQUjB32a7pPndF6PR2MYQBxGOi2IOuU-1iatSRCg",
    "https://play-lh.googleusercontent.com/9BJlFbPodn5h9R76V0DfLqGmN42U8-PNN5--xisQXBpwApN_RPXTTXD7IRl0e0bC0NQFslddPE97YWNhMtCIIcg",
    "https://play-lh.googleusercontent.com/YXf_qd3bM_bOLBiQhXwkt2aV4UB8wbXxlhiRY16uVCdtMHMZqnyy0Lx-Lhnr4Q9MuwY2iBMZjbfIeLcE6vnUfQ",
    "… 5 more"
  ],
  "country": "US",
  "language": "en",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
