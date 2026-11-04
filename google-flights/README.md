# Google Flights API: prices, price tracking and total trip cost

Google Flights has no public API. The [Google Flights Scraper on Apify](https://apify.com/wulfcare/google-flights-scraper) returns every flight for a route and date, Google's **low / typical / high** price verdict, and, with tracking on, what changed since your last run.

```python
from wulfcare import run   # ../wulfcare.py

rows = run("wulfcare/google-flights-scraper", {
    "origin": "JFK",
    "destination": "LAX",
    "departureDate": "+30 days",   # or 2026-12-10
    "maxFlights": 5,
})
summary = next(r for r in rows if r["type"] == "summary")
print(summary["lowestPrice"], summary["priceLevel"], summary["typicalPriceLow"], summary["typicalPriceHigh"])

for f in rows:
    if f["type"] == "flight":
        print(f["price"], f["airlines"], f["departureTime"], f["stops"], f["durationMinutes"])
```

Round trip: add `"returnDate": "+7 days"` or `"tripDays": 7`. More airports: `"origin": "JFK,LGA,EWR"`. More routes: `"routes": ["SYD-LAX", "MEL to AKL"]`.

Tell me when it drops (run on an [Apify schedule](https://docs.apify.com/platform/schedules); you pay only for what changed):

```python
{"origin": "SFO", "destination": "HNL", "departureDate": "2027-01-15", "trackPrices": True, "onlyChanges": True, "targetPrice": 250}
```

Flights get `priceStatus` and `priceChange`; the summary gets `lowestPriceEver` and `belowTargetPrice`.

Total trip cost, flight plus the cheapest well-rated hotel (no extra charge):

```python
{"origin": "SYD", "destination": "HND,NRT", "departureDate": "2027-03-10", "tripDays": 7, "includeHotels": True, "maxFlights": 0}
```

Read `tripTotalPrice`, `hotelName` and `hotelOptions`.

Cheapest date to fly: `"cheapestDates": true` adds one row per departure date (`"cheapestDatesRange": 60` by default).

Each flight: `price`, `airlines`, `flightNumbers`, `departureTime`, `arrivalTime`, `durationMinutes`, `stops`, `layovers`, `emissionsKg`, `isBest`, `isCheapest`, `hasLongLayover`, `hasOvernightLayover`, `googleFlightsUrl`. Prices are the total for all passengers, in the `currency` you pick.

**Cost:** $0.50 per 1,000 results. Errors are free.

Hotels only: see [../google-hotels](../google-hotels).
