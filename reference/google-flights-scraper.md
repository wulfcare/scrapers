# Google Flights Scraper & Price Tracker

`wulfcare/google-flights-scraper`: Google Flights prices for any route and date, with price tracking built in: each run says which prices dropped or rose, which flights are new or gone, and the all-time low. Plus total trip cost with a hotel, cheapest dates, layovers, CO2 and Google's low/typical/high verdict. Built for AI agents.

**Use it for:**
- Google Flights prices for any route and date with airlines, times, layovers and CO2
- whether a fare is good: Google's low / typical / high verdict, typical price range and price history
- flight price tracking between runs: drops, rises, new and gone flights, all-time low
- total trip cost: flight plus the cheapest well-rated hotel
- cheapest price for every departure date in a range

- Store page: https://apify.com/wulfcare/google-flights-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-flights-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-flights-scraper`

**Price:**
- $0.0005 per result (result): One row: a summary of a route and date (lowest price, Google's low/typical/high verdict, price changes since the last run, trip cost with hotel), one flight, or one date's cheapest price. Errors and 'gone' rows are free; hotel lookups are included.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-flights-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"origin": "JFK", "destination": "LAX", "departureDate": "+30 days", "maxFlights": 5}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-flights-scraper").call(run_input={"origin": "JFK", "destination": "LAX", "departureDate": "+30 days", "maxFlights": 5})
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
| `trackPrices` | boolean |  | false |  | Track prices between runs: Remember this run's prices and compare the next run with them: every flight gets priceStatus (new, cheaper, pricier, same), previousPrice, priceChange and its lowest price seen; flights no longer listed come out as "gone" (free); the summary gets the change in the lowest price and the all-time low. Schedule the Actor (e.g. daily) with the same input. Prices are kept in your named key-value store "google-flights-tracker-". |
| `trackerName` | string |  | "default" |  | Tracker name: Keep separate trackers apart (e.g. "client-a", "summer-trip"). Letters, digits, dashes. |
| `onlyChanges` | boolean |  | false |  | Only output changes: With tracking: output only flights that are new or changed price (plus one summary row per search). You pay only for those rows, so daily monitoring costs almost nothing. |
| `targetPrice` | integer |  |  | 0– | Target price: Optional: the summary's belowTargetPrice is true when the lowest price is at or under this (in the chosen currency). Handy for alerts and webhooks. |
| `includeHotels` | boolean |  | false |  | Add hotel and total trip cost: Look up the cheapest well-rated hotel (3+ stars, 4+ rating by default) in the destination city on Google Hotels for the stay (arrival to return date, or "Hotel nights" for one way), and add tripTotalPrice = flight + hotel to the summary and every flight. No extra charge. |
| `hotelNights` | integer |  | 3 | 1–30 | Hotel nights (one way): Stay length for one-way searches. Round trips stay until the return date. |
| `hotelMinRating` | string |  | "4" | `0` (Any), `3.5` (3.5+), `4` (4+), `4.5` (4.5+) | Hotel minimum rating: Google rating (out of 5) a hotel needs to count. |
| `hotelMinStars` | integer |  | 3 | 0–5 | Hotel minimum stars: Hotel class a hotel needs to count (0 = any). Hostels, dorms and apartments never count, so the trip cost is for a real hotel room. |
| `cheapestDates` | boolean |  | false |  | Cheapest dates: Also output the cheapest price for every departure date in a range (Google's date grid), one row per date, the cheapest flagged. Round trips keep the same trip length. |
| `cheapestDatesRange` | integer |  | 60 | 7–330 | Days to scan: Departure dates from the departure date on. |
| `language` | string |  | "en" |  | Language: Language of airport and airline names (hl=). |
| `maxConcurrency` | integer |  | 6 | 1–20 | Requests at once: Searches sent to Google at the same time. |
| `residentialFallback` | boolean |  | true |  | Fall back to residential proxy: With the default Apify Proxy: when Google keeps refusing datacenter IPs, finish the run on US residential IPs (no extra charge to you). |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "type": "summary",
  "route": "MEL-AKL",
  "origin": "MEL",
  "destination": "AKL",
  "destinationCity": "Auckland",
  "departureDate": "2026-12-04",
  "returnDate": null,
  "tripType": "one-way",
  "cabinClass": "economy",
  "adults": 1,
  "children": 0,
  "currency": "USD",
  "lowestPrice": 233,
  "priceLevel": "low",
  "typicalPrice": 310,
  "typicalPriceLow": 240,
  "typicalPriceHigh": 475,
  "targetPrice": null,
  "belowTargetPrice": null,
  "previousLowestPrice": null,
  "lowestPriceChange": null,
  "lowestPriceEver": null,
  "lowestPriceEverAt": null,
  "isLowestEver": null,
  "trackedSince": null,
  "trackedRuns": null,
  "changes": null,
  "cheapestFlight": {
    "price": 233,
    "airlines": [
      "Jetstar"
    ],
    "flightNumbers": [
      "JQ 217"
    ],
    "departureTime": "2026-12-04T23:55",
    "arrivalTime": "2026-12-05T05:30",
    "durationMinutes": 215,
    "stops": 0
  },
  "flightsFound": 96,
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
      "date": "2026-09-04",
      "price": 220
    },
    {
      "date": "2026-09-05",
      "price": 235
    },
    {
      "date": "2026-09-06",
      "price": 235
    },
    "… 58 more"
  ],
  "googleFlightsUrl": "https://www.google.com/travel/flights?q=Flights+to+AKL+from+MEL+on+2026-12-04+one+way&hl=en&curr=USD",
  "scrapedAt": "2026-11-04T07:56:02+00:00",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
