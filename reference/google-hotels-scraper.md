# Google Hotels Prices Scraper

`wulfcare/google-hotels-scraper`: Hotel prices from Google Hotels: every booking site's price (Booking.com, Expedia, Agoda, the hotel's own site...) for any hotel and dates, per night and total, with and without taxes, plus hotel searches like "hotels in Paris" with ratings, stars, address and lowest price. $0.80 per 1,000 prices.

**Use it for:**
- hotel prices from every booking site (Booking.com, Expedia, Agoda, official site) for given dates
- hotel price calendar over many check-in dates
- list of hotels in a city with rating, stars and lowest price

- Store page: https://apify.com/wulfcare/google-hotels-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-hotels-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-hotels-scraper`

**Price:**
- $0.0008 per price (price): One booking site's price for one hotel and one check-in date (per night and total, with and without taxes, booking link). Dates without prices and errors are never charged.
- $0.0015 per hotel from a search (hotel): One hotel from a Google Hotels search, with its details (stars, rating, reviews, address, location, photos) and lowest price.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-hotels-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"hotels": ["Hilton London Paddington"], "checkInDate": "+30 days", "nights": 2, "adults": 2, "currency": "USD"}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-hotels-scraper").call(run_input={"hotels": ["Hilton London Paddington"], "checkInDate": "+30 days", "nights": 2, "adults": 2, "currency": "USD"})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `hotels` | array |  |  |  | Hotels: Hotels to get every booking site's prices for. Each one can be a hotel's name (best with the city: "Hilton London Paddington"), a Google Hotels link (https://www.google.com/travel/hotels/entity/...) or its entity ID (the "Ch..." code in that link), or the hotel's Google Maps link or CID. |
| `searchQueries` | array |  |  |  | Searches: Google Hotels searches, e.g. "hotels in Paris" or "beach hotels in Bali". Each gives one row per hotel (name, stars, rating, reviews, address, lowest price and more), up to "Maximum hotels per search". |
| `maxHotels` | integer |  | 20 | 1–1000 | Maximum hotels per search: Hotels to get from each search, in Google's order. |
| `includeAllPrices` | boolean |  | false |  | Every booking site's price for searched hotels: Searches give each hotel's lowest price. Turn this on to also get every booking site's price for each hotel found (in its "prices" list, charged per price). |
| `checkInDate` | string |  |  |  | Check-in date: First check-in date (YYYY-MM-DD, or "tomorrow", "+7 days"). Empty = tomorrow. Google has prices for about a year ahead. |
| `days` | integer |  | 1 | 1–365 | Check-in dates: How many check-in dates in a row, from the first: 30 gives a price calendar for the next 30 check-ins. |
| `nights` | integer |  | 1 | 1–30 | Nights: Length of each stay. |
| `adults` | integer |  | 2 | 1–10 | Adults: Guests. Prices and the booking sites offering them change with the number of guests. |
| `currency` | string |  | "USD" |  | Currency: Three-letter code (USD, EUR, GBP, AUD...). Google prices in the currency of the country the request comes from (USD with the default US proxy); other currencies are converted at the day's ECB reference rate. For prices exactly as shown in a country (local currency and taxes), use a residential proxy from that country. |
| `outputFormat` | string |  | "providers" | `providers` (One row per booking site and date), `hotels` (One row per hotel and date (prices in a list)) | Output: How rows for the hotels above come out. Searches always give one row per hotel. |
| `device` | string |  | "desktop" | `desktop` (Desktop), `mobile` (Mobile) | Device: Get the prices Google shows on desktop or on mobile (some sites have mobile-only rates). |
| `language` | string |  | "en" |  | Language: Language of hotel descriptions and texts (en, fr, de, es...). |
| `maxConcurrency` | integer |  | 6 | 1–20 | Parallel requests: Requests to Google at once. |
| `onlyChanges` | boolean |  | false |  | Monitor: only new and changed prices: For a schedule or a task that runs every hour or day. The Actor remembers each price from the last run (in a key-value store named "google-hotels-monitor" on your own account) and outputs only prices that are new, cheaper, dearer or gone, each with change, previousPrice, priceChange and priceChangePercent. You pay only for the rows that come out. The first run outputs every price as new. If a run stops early (maximum cost reached, or blocked), the remembered prices stay as they were, so the next run reports those changes again. |
| `minChangePercent` | integer |  | 0 | 0–100 | Ignore changes smaller than (%): With monitoring on: skip price moves smaller than this, e.g. 5 to hear only about moves of 5% or more. 0 reports every change. |
| `onlyDrops` | boolean |  | false |  | Only price drops: With monitoring on: output only new prices and price drops (no rises, no gone rows). Good for deal alerts. |
| `monitorName` | string |  |  |  | Monitor name (optional): With monitoring on: which saved prices to compare against. Leave empty and each different input keeps its own; set a name to keep comparing after you edit the input, or to run two monitors on the same input. |
| `entity` | string |  |  |  | Entity (compatibility): A single hotel (entity ID, link or name): same as one line in Hotels. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "hotelName": "Hôtel Atrium by HappyCulture",
  "provider": "Agoda",
  "isOfficial": false,
  "price": 71,
  "price2": 82,
  "adults": 2,
  "currency": "USD",
  "checkInDate": "2026-12-17",
  "checkOutDate": "2026-12-18",
  "nights": 1,
  "pricePerNight": 71.13,
  "pricePerNightWithTaxes": 82.38,
  "totalPrice": 71.13,
  "totalPriceWithTaxes": 82.38,
  "rank": 1,
  "isCheapest": true,
  "bookingUrl": "https://www.agoda.com/partners/partnersearch.aspx?site_id=1917614&CkInDay=17&CkInMonth=12&CkInYear=2026&CkOutDay=18&campaignid=&CkOutMonth=12&CkOutYear=2026&SearchDateType=default&NumberOfAdults=2&LT=29&NumberOfChildren=0&childages=&NumberO…",
  "otaUrl": "https://www.google.com/travel/lodging/clk?pc=AJ0xEyhrWPnkXWOzI8HriD1qsmSs7SOHIzO06nsu5uHBzATgrjPU821OYNdEsuZckHh0dbdbS3Pk_D5HYZWRowOq1K9S2-BmYPle3v3s3xYzYlEg5jRhzdKEgF0VS1mTKuKx6chV23Q4giuDTmKsbnhmzeGwy3zKAuypgv2w9bXPhIPDr_gDqTdGPNEXq0aFSg&…",
  "isAd": false,
  "rooms": null,
  "priceText": "$71",
  "googleCurrency": null,
  "exchangeRate": null,
  "entityId": "ChcIhpronI2bp7cBGgsvZy8xdmc2dDB6NRAB",
  "hotelUrl": "https://www.google.com/travel/hotels/entity/ChcIhpronI2bp7cBGgsvZy8xdmc2dDB6NRAB/prices?hl=en&gl=us&ts=CAASCgoCCAMKAggDEAAaHBIaEhQKBwjqDxAMGBESBwjqDxAMGBIYATICEAA",
  "input": "ChcIhpronI2bp7cBGgsvZy8xdmc2dDB6NRAB",
  "scrapedAt": "2026-11-17T23:20:10+00:00",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
