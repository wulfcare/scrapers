# App Store Scraper: Reviews, App Details, Search & Charts

`wulfcare/app-store-scraper`: Scrape Apple App Store reviews with no 500 cap (any country, newest/helpful/critical sort, star and date filters, developer replies), full app details with rating histogram, version history and App Privacy labels, search results, top charts, developer apps and similar apps.

**Use it for:**
- Apple App Store app details, rating histogram, version history, privacy labels
- App Store search results, top charts, developer apps, similar apps
- App Store reviews together with app data

- Store page: https://apify.com/wulfcare/app-store-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~app-store-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/app-store-scraper`

**Price:**
- $0.0001 per review (review): One App Store review with stars, title, text, date, the developer reply and (for recent reviews) the app version. Not-found apps and failed requests are never charged.
- $0.0005 per app details (app-details): Full details of one app: rating histogram, price, in-app purchases, version history, age rating, privacy labels, chart position and more.
- $0.0002 per app in a list (app-list-item): One app from a search, top chart, developer page or similar-apps list, with title, rating, price, category and description.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~app-store-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode": "apps", "appIds": ["324684580"], "countries": ["us"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/app-store-scraper").call(run_input={"mode": "apps", "appIds": ["324684580"], "countries": ["us"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `mode` | string | yes | "reviews" | `reviews` (Reviews of apps), `apps` (App details (full)), `search` (Search results), `charts` (Top charts), `developer` (Apps by developer), `similar` (Similar apps (You Might Also Like)) | What to scrape: Each run returns one kind of row, so your dataset always has the same columns. Reviews, App details and Similar apps use the app list below; the other modes use their own section. |
| `appIds` | array |  |  |  | Apps: App Store URLs (https://apps.apple.com/us/app/.../id324684580), numeric app ids (324684580) or bundle ids (com.spotify.client). Used by Reviews, App details and Similar apps. |
| `countries` | array |  | ["us"] |  | Countries: Two-letter App Store country codes (us, gb, de, jp, br, ...). Each country is its own store with its own reviews, prices, charts and search results; add several to cover them all in one run. Every row says which country it came from. |
| `language` | string |  |  |  | Language: Optional, e.g. en-US, de-DE, fr-FR. App names and descriptions come in this language when the developer provides it. Leave empty for each country's default language. Reviews are always the ones written in that country's store, whatever their language. |
| `maxReviewsPerApp` | integer |  | 100 | 0– | Max reviews per app: 0 = every review the App Store has for the app in each country (no 500 cap). With a star filter, this counts only reviews with those stars. |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `helpful` (Most helpful (App Store default)), `favorable` (Most favorable (5 stars first)), `critical` (Most critical (1 star first)) | Sort reviews by: Newest first is best for monitoring and date cutoffs. Most critical is the fastest way to get complaints. |
| `reviewStars` | array |  |  |  | Only these star ratings: Leave empty for all ratings. You're only charged for reviews with these stars. Tip: with Most critical (or Most favorable) the run stops as soon as it's past the stars you picked. |
| `reviewsSince` | string |  |  |  | Only reviews since: Skip reviews older than this, e.g. 2026-09-01 or "30 days". With Newest first the run stops as soon as it reaches older reviews. |
| `includeReviewerNames` | boolean |  | false |  | Include reviewer nicknames: Off by default. The App Store shows a nickname for each reviewer; no other reviewer data is collected. |
| `searchQueries` | array |  |  |  | Search terms: One search per line, e.g. "habit tracker". Up to 200 apps per term and country. |
| `chartCollections` | array |  | ["topfree"] |  | Charts: Which top charts to fetch (up to 100 apps each, Apple's limit). |
| `chartDevice` | string |  | "iphone" | `iphone` (iPhone), `ipad` (iPad), `mac` (Mac) | Chart device: iPhone, iPad or Mac App Store charts. |
| `chartGenres` | array |  | ["all"] |  | Chart categories: One chart per category (and per chart and country). iPhone and iPad only; Mac charts are overall. |
| `developers` | array |  |  |  | Developers: Developer page URLs (https://apps.apple.com/us/developer/supercell/id488106216), numeric developer ids, or exact developer names as shown on the App Store. |
| `maxResults` | integer |  | 0 | 0– | Max apps per search / chart / developer / similar: 0 = everything the App Store lists (search up to 200, charts up to 100). |
| `includeFullDetails` | boolean |  | false |  | Full details for every listed app: Search, charts, developer and similar modes return an app card by default. Turn this on to get the full App details row (ratings histogram, version history, privacy labels, ...) for each app, charged as an app detail. |
| `includePrivacyLabels` | boolean |  | true |  | Include App Privacy labels: The app's privacy "nutrition label": data linked to you, data used to track you, and why. Free, it comes with the same request. |
| `includeVersionHistory` | boolean |  | true |  | Include version history: Recent versions with their dates and release notes. |
| `maxConcurrency` | integer |  | 6 | 1–20 | Parallel connections: How many IPs requests are spread over (the run's own IP plus proxy sessions). More is faster for very large review pulls. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "input": "top free iphone · all apps",
  "rank": 1,
  "appId": "632064380",
  "bundleId": "lt.manodrabuziai.fr",
  "url": "https://apps.apple.com/us/app/vinted-pre-loved-marketplace/id632064380",
  "title": "Vinted: Pre-loved marketplace",
  "subtitle": "Sell & buy second-hand clothes",
  "developer": "Vinted Limited",
  "developerId": "554164035",
  "score": 4.9,
  "ratings": 581190,
  "genre": "Shopping",
  "free": true,
  "price": 0,
  "currency": "USD",
  "priceText": "Free",
  "inAppPurchases": false,
  "contentRating": "4+",
  "releasedAt": "2013-04-11",
  "description": "The idea is simple: you sell your pre-loved stuff to other members who’ll love it again. They get the thrill of unboxing a great find, you get more space at home. It's look-good, do-good, feel-good, for everyone. \n\nSelling is easy and free\n…",
  "icon": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/d3/cd/83/d3cd83d1-4d21-6390-1c53-4e1557fdf70d/VintedAppIcon-0-0-1x_U007epad-0-1-85-220.png/512x512bb.png",
  "country": "US",
  "language": null,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
