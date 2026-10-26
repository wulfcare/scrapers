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
| `entity` | string |  |  |  | Entity (compatibility): A single hotel (entity ID, link or name): same as one line in Hotels. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "query": "hotels in Paris",
  "rank": 1,
  "name": "The Originals Boutique, Hôtel Maison Montmartre, Paris",
  "hotelClass": 4,
  "hotelClassText": "4-star tourist hotel",
  "rating": 4,
  "reviewCount": 2135,
  "checkInDate": "2026-10-26",
  "checkOutDate": "2026-10-27",
  "nights": 1,
  "adults": 2,
  "currency": "USD",
  "pricePerNight": 76.03,
  "pricePerNightWithTaxes": 102.56,
  "totalPrice": 76.03,
  "totalPriceWithTaxes": 102.56,
  "priceText": "$76",
  "dealText": "17% less than usual",
  "cheapestProvider": null,
  "prices": null,
  "address": null,
  "phone": null,
  "website": "https://www.hotelmaisonmontmartre.com/?utm_campaign=uberall&utm_medium=organic&utm_source=googlelisting",
  "latitude": 48.900537,
  "longitude": 2.3362689999999997,
  "countryCode": "FR",
  "checkInTime": "3:00 PM",
  "checkOutTime": "12:00 PM",
  "description": "Hip hotel featuring a sophisticated restaurant & a cool rooftop eatery/bar with a terrace.",
  "descriptionLong": null,
  "ratingBreakdown": {
    "1": 225,
    "2": 107,
    "3": 180,
    "4": 497,
    "5": 1126
  },
  "reviewAspects": [
    {
      "aspect": "Safety",
      "mentions": 67,
      "positive": 13,
      "negative": 51
    },
    {
      "aspect": "Bar or lounge",
      "mentions": 60,
      "positive": 47,
      "negative": 6
    },
    {
      "aspect": "Room entertainment",
      "mentions": 17,
      "positive": 8,
      "negative": 9
    },
    "… 3 more"
  ],
  "otherRatings": null,
  "nearbyPlaces": [
    {
      "name": "Aéroport de Paris-Charles de Gaulle",
      "travelTimes": {
        "driving": "19 min",
        "transit": "56 min"
      }
    },
    {
      "name": "Restaurant le 365",
      "travelTimes": {
        "walking": "7 min"
      }
    }
  ],
  "thumbnailUrl": "https://lh3.googleusercontent.com/grass-cs/AABkmLfwYtcmqfrRWvXV6Jl_jRqJ1i-gDYNxdNuhF8KnH9MlOZvxPqJR-u-L9giDhwMbyl2jRtRgs-9rCsbYPTzZdW9R1MUmqq_Z8J0e33BQSSc_Zid_ePbJWZ4YavQcgFDAQzqNBvS2=s150-w92-h150-n-k-no",
  "photos": [
    "https://lh3.googleusercontent.com/grass-cs/AABkmLfwYtcmqfrRWvXV6Jl_jRqJ1i-gDYNxdNuhF8KnH9MlOZvxPqJR-u-L9giDhwMbyl2jRtRgs-9rCsbYPTzZdW9R1MUmqq_Z8J0e33BQSSc_Zid_ePbJWZ4YavQcgFDAQzqNBvS2=s287-w287-h192-n-k-no-v1",
    "https://lh3.googleusercontent.com/grass-cs/AABkmLeNZs2aEW5P2S1v2uLfL5EAo-_dNkj_vVC-0_D0Ws0CCJWKzPnPzBKN3Zluz7bAO2QpGLzK1plMg1a9n1BR2Sb9WotAg4MTqB9ZsBMKzUiIzoWDV1zSxLBbwNehjlGFN3dc3514=s287-w287-h192-n-k-no-v1",
    "https://lh3.googleusercontent.com/grass-cs/AABkmLcIWcvK-UkQaYFjs6lLuuwBw34mD0V2f_8LabReVSEGypdwGKQqelb6A_df2oWwfF3qxM18cdiPmIaAdT4-TUVO7z4ujzRTy_TOo3mMAOs3QMrX53L7GkqpCLJIFh-HZzPv2ZM1=s287-w287-h192-n-k-no-v1",
    "… 6 more"
  ],
  "googleMapsUrl": "https://www.google.com/maps?cid=11195438155682968190",
  "googleCurrency": null,
  "exchangeRate": null,
  "entityId": "ChoI_uTZsvz1i6-bARoNL2cvMTFmZHB6eDEwMxAB",
  "hotelUrl": "https://www.google.com/travel/hotels/entity/ChoI_uTZsvz1i6-bARoNL2cvMTFmZHB6eDEwMxAB/prices?hl=en&gl=us&ts=CAASCgoCCAMKAggDEAAaHBIaEhQKBwjqDxAKGBoSBwjqDxAKGBsYATICEAA",
  "input": "hotels in Paris",
  "scrapedAt": "2026-10-25T09:56:42+00:00",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
