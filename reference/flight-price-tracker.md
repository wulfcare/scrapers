# Flight Price Tracker: Price Drop Alerts from Google Flights

`wulfcare/flight-price-tracker`: Track flight prices on any route: schedule it and every run says which fares dropped or rose, which flights are new or gone, the all-time low and if a fare is under your target. Google Flights data. $0.15 per 1,000 flights, no start fee.

**Use it for:**
- scheduled flight price checks that say which fares dropped or rose, new or gone flights, the all-time low and whether a fare is under a target

- Store page: https://apify.com/wulfcare/flight-price-tracker
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~flight-price-tracker/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/flight-price-tracker`

**Price:**
- $0.00015 per result (result): One row: a route-and-date summary (lowest price, Google's verdict, changes since the last run), one flight, or one date's cheapest price. Errors and 'gone' rows are free.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~flight-price-tracker/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"origin": "JFK", "destination": "LAX", "departureDate": "+30 days"}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/flight-price-tracker").call(run_input={"origin": "JFK", "destination": "LAX", "departureDate": "+30 days"})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `origin` | string |  |  |  | From (airport code): IATA code of the departure airport, e.g. JFK. Several, comma-separated, to search them together: JFK,LGA,EWR. |
| `destination` | string |  |  |  | To (airport code): IATA code of the arrival airport, e.g. LAX (or several: LAX,BUR,LGB). |
| `departureDate` | string |  |  |  | Departure date: YYYY-MM-DD, or relative: "+30 days", "in 2 weeks", "tomorrow". Empty = in 30 days. |
| `returnDate` | string |  |  |  | Return date (round trip): Empty = one way. YYYY-MM-DD, or "+7 days" counted from the departure date. Round-trip prices are for the whole trip, as on Google Flights. |
| `tripDays` | integer |  |  | 0–330 | Trip length in days (round trip): Instead of a return date: return this many days after departure. 0 = one way. |
| `routes` | array |  |  |  | More routes: Extra routes, one per line: "SYD-LAX", "JFK,EWR-LHR", "MEL to AKL". Each is searched for the same dates and options. |
| `departureDays` | integer |  | 1 | 1–60 | Departure dates in a row: Search this many consecutive departure dates from the first (full flight lists for each). For just the cheapest price per date over a long range, use "Cheapest dates" instead. |
| `maxFlights` | integer |  | 20 | 0–500 | Flights per search: Flight rows per route and date: Google's "best" flights first, then the rest by price. Google lists 50-300. 0 = just the summary row (lowest price, verdict, trip cost). |
| `cabinClass` | string |  | "economy" | `economy` (Economy), `premium-economy` (Premium economy), `business` (Business), `first` (First) | Cabin: Seat class. |
| `adults` | integer |  | 1 | 1–9 | Adults: Prices are the total for all passengers. |
| `children` | integer |  | 0 | 0–8 | Children (2-11): Children aged 2-11 (count toward the total price). |
| `maxStops` | string |  | "any" | `any` (Any), `nonstop` (Nonstop only), `1` (1 stop or fewer), `2` (2 stops or fewer) | Stops: Most stops a flight may have. |
| `currency` | string |  | "USD" |  | Currency: Three-letter code: USD, EUR, GBP, AUD, INR... Google prices directly in it. |
| `trackerName` | string |  | "default" |  | Tracker name: Keep separate trackers apart (e.g. "client-a", "summer-trip"). Letters, digits, dashes. |
| `onlyChanges` | boolean |  | false |  | Only output changes: With tracking: output only flights that are new or changed price (plus one summary row per search). You pay only for those rows, so daily monitoring costs almost nothing. |
| `targetPrice` | integer |  |  | 0– | Target price: Optional: the summary's belowTargetPrice is true when the lowest price is at or under this (in the chosen currency). Handy for alerts and webhooks. |
| `cheapestDates` | boolean |  | false |  | Cheapest dates: Also output the cheapest price for every departure date in a range (Google's date grid), one row per date, the cheapest flagged. Round trips keep the same trip length. |
| `cheapestDatesRange` | integer |  | 60 | 7–330 | Days to scan: Departure dates from the departure date on. |
| `language` | string |  | "en" |  | Language: Language of airport and airline names (hl=). |
| `maxConcurrency` | integer |  | 6 | 1–20 | Requests at once: Searches sent to Google at the same time. |
| `residentialFallback` | boolean |  | true |  | Fall back to residential proxy: With the default Apify Proxy: when Google keeps refusing datacenter IPs, finish the run on US residential IPs (no extra charge to you). |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "type": "summary",
  "route": "JFK-LAX",
  "origin": "JFK",
  "destination": "LAX",
  "destinationCity": "Los Angeles",
  "departureDate": "2026-12-08",
  "returnDate": null,
  "tripType": "one-way",
  "cabinClass": "economy",
  "adults": 1,
  "children": 0,
  "currency": "USD",
  "lowestPrice": 164,
  "priceLevel": "typical",
  "typicalPrice": 179,
  "typicalPriceLow": 105,
  "typicalPriceHigh": 325,
  "targetPrice": null,
  "belowTargetPrice": null,
  "previousLowestPrice": 164,
  "lowestPriceChange": 0,
  "lowestPriceEver": 164,
  "lowestPriceEverAt": "2026-11-08T13:02:34+00:00",
  "isLowestEver": true,
  "trackedSince": "2026-11-08T13:02:34+00:00",
  "trackedRuns": 3,
  "changes": {
    "new": 0,
    "cheaper": 0,
    "pricier": 0,
    "gone": 0
  },
  "cheapestFlight": {
    "price": 164,
    "airlines": [
      "American"
    ],
    "flightNumbers": [
      "AA 341"
    ],
    "departureTime": "2026-12-08T14:59",
    "arrivalTime": "2026-12-08T18:16",
    "durationMinutes": 377,
    "stops": 0
  },
  "flightsFound": 89,
  "hotelName": null,
  "hotelRating": null,
  "hotelStars": null,
  "hotelNights": null,
  "hotelPricePerNight": null,
  "hotelTotalPrice": null,
  "hotelUrl": null,
  "hotelOptions": null,
  "tripTotalPrice": null,
  "priceHistory": [
    {
      "date": "2026-09-08",
      "price": 169
    },
    {
      "date": "2026-09-09",
      "price": 169
    },
    {
      "date": "2026-09-10",
      "price": 169
    },
    "… 59 more"
  ],
  "googleFlightsUrl": "https://www.google.com/travel/flights?q=Flights+to+LAX+from+JFK+on+2026-12-08+one+way&hl=en&curr=USD",
  "scrapedAt": "2026-11-08T13:04:58+00:00",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
