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
  "input": "com.spotify.music",
  "rank": null,
  "appId": "com.spotify.music",
  "url": "https://play.google.com/store/apps/details?id=com.spotify.music&hl=en&gl=us",
  "title": "Spotify: Music and Podcasts",
  "summary": "Listen to songs, play podcasts, create playlists and discover music you'll love",
  "description": "With the Spotify music and podcast app, you can play millions of songs, albums and original podcasts for free. We have even added audiobooks, so you can enjoy thousands of stories wherever you are!\n\nStream music and podcasts, listen to audi…",
  "descriptionHtml": null,
  "score": 4.3492,
  "ratings": 36544130,
  "reviews": 1857350,
  "histogram": {
    "1": 3715583,
    "2": 1066810,
    "3": 1307845,
    "4": 3104700,
    "5": 27349176
  },
  "installs": "1,000,000,000+",
  "minInstalls": 1000000000,
  "realInstalls": 3173851392,
  "free": true,
  "price": 0,
  "currency": "USD",
  "priceText": "Free",
  "inAppPurchases": true,
  "inAppPurchasesRange": "$4.99 - $203.88 per item",
  "containsAds": true,
  "genre": "Music & Audio",
  "genreId": "MUSIC_AND_AUDIO",
  "categories": [
    {
      "name": "Music & Audio",
      "id": "MUSIC_AND_AUDIO"
    }
  ],
  "contentRating": "Teen",
  "contentRatingDescription": null,
  "interactiveElements": "In-App Purchases",
  "developer": "Spotify AB",
  "developerId": "6523013212965523194",
  "developerUrl": "https://play.google.com/store/apps/developer?id=Spotify+AB",
  "developerWebsite": "https://www.spotify.com",
  "developerEmail": "support@spotify.com",
  "developerLegalName": "Spotify AB",
  "developerLegalEmail": "support@spotify.com",
  "developerAddress": "Regeringsgatan 19\n111 53 Stockholm\nSweden",
  "developerPhone": "+46 10 334 03 65",
  "privacyPolicy": "https://www.spotify.com/legal/privacy-policy/",
  "released": "May 27, 2014",
  "releasedAt": "2014-05-27T13:12:17Z",
  "updatedAt": "2026-10-23T12:37:22Z",
  "version": "Varies with device",
  "minAndroidVersion": "Varies with device",
  "minSdk": null,
  "targetSdk": 35,
  "recentChanges": "We’re always making changes and improvements to Spotify. To make sure you don’t miss a thing, just keep your Updates turned on.",
  "chartRank": 1,
  "chartName": "top free music & audio",
  "icon": "https://play-lh.googleusercontent.com/IzQgYCcnCFCD08GR-3bdtcT8xzOvrNkC84avGT5CwTX2VIqmTmKKJcP_Cd4JoBOdmCMlTndlOzV6hrthg2fOWA",
  "headerImage": "https://play-lh.googleusercontent.com/WdedaGD6EAXZgy88wZM97aIcenQ5Cqzu_IUWBMMalkZmVe2lhv_3YqIUh-6pFqLv27kZ44cQX3qxyZTXHH-S91Q",
  "screenshots": [
    "https://play-lh.googleusercontent.com/c1jnjL-9CIFlwlTMX3xNyeo8aEH39sNuC5zpTHhfW8keGxQE3TBMRX9Rm3VqM3E03Cyl9AqtnxuKvxJpcW0WCA",
    "https://play-lh.googleusercontent.com/YxWsaNLSEBvLh04geMOADhSq6Ln5LmRrpa51ixZ7YkcEwmPQ-wdtnvoZDjVAgufbi2et0IlTVDAsvCCmlsJYnNA",
    "https://play-lh.googleusercontent.com/RevDecVUzkc8iYhVazBoXb0O0Amy3_w6MNzzABHyAlyZjEYBq3xl-UxuxL5PGB6xTZpuxV7tET3pg1rp6weFWAY",
    "… 37 more"
  ],
  "video": null,
  "videoImage": null,
  "permissions": [
    {
      "group": "Identity",
      "permissions": [
        "find accounts on the device"
      ]
    },
    {
      "group": "Contacts",
      "permissions": [
        "find accounts on the device"
      ]
    },
    {
      "group": "Location",
      "permissions": [
        "approximate location (network-based)",
        "precise location (GPS and network-based)"
      ]
    },
    "… 8 more"
  ],
  "dataSafety": {
    "sharedData": [
      {
        "category": "Device or other IDs",
        "type": "Device or other IDs",
        "optional": false,
        "purposes": [
          "Advertising or marketing",
          "Fraud prevention, security, and compliance"
        ]
      },
      {
        "category": "Location",
        "type": "Approximate location",
        "optional": false,
        "purposes": [
          "Analytics",
          "Advertising or marketing"
        ]
      },
      {
        "category": "Personal info",
        "type": "Other info",
        "optional": false,
        "purposes": [
          "Analytics"
        ]
      }
    ],
    "sharedSummary": null,
    "collectedData": [
      {
        "category": "Device or other IDs",
        "type": "Device or other IDs",
        "optional": false,
        "purposes": [
          "App functionality",
          "Analytics",
          "Developer communications",
          "… 3 more"
        ]
      },
      {
        "category": "Audio",
        "type": "Voice or sound recordings",
        "optional": true,
        "purposes": [
          "App functionality",
          "Fraud prevention, security, and compliance"
        ]
      },
      {
        "category": "Photos and videos",
        "type": "Photos",
        "optional": true,
        "purposes": [
          "App functionality",
          "Fraud prevention, security, and compliance"
        ]
      },
      "… 16 more"
    ],
    "collectedSummary": null,
    "securityPractices": [
      "Data is encrypted in transit",
      "You can request that data be deleted"
    ]
  },
  "country": "US",
  "language": "en",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
