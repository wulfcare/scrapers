# Google Hotels API: every booking site's price for any hotel

Google Hotels has no public API. The [Google Hotels Prices Scraper on Apify](https://apify.com/wulfcare/google-hotels-scraper) returns **every booking site's price** (Booking.com, Expedia, Agoda, Hotels.com, the hotel's own site...) for any hotel and dates, per night and total, with and without taxes, plus hotel searches like "hotels in Paris" with rating, stars, address and lowest price.

```python
from wulfcare import run   # ../wulfcare.py

prices = run("wulfcare/google-hotels-scraper", {
    "hotels": ["Hilton London Paddington"],
    "checkInDate": "2026-12-10",
    "nights": 2,
    "adults": 2,
    "currency": "USD",
})
for p in prices:
    print(p["provider"], p["totalPriceWithTaxes"], p["isCheapest"], p["bookingUrl"])
```

Search mode: `{"searchQueries": ["hotels in Paris"], "maxHotels": 20}` → `name`, `hotelClass`, `rating`, `reviewCount`, `pricePerNight`, `cheapestProvider`, `address`.

Price tracking over many dates: set `"days": 30` to check 30 consecutive check-in dates in one run.

**Cost:** $0.80 per 1,000 prices, $1.50 per 1,000 hotels from a search. Dates without prices and errors are free.
