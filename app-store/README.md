# App Store reviews: get more than 500 (no RSS cap)

Apple's public customer-reviews RSS feed stops at 10 pages of 50, so most App Store review scrapers and libraries (including the popular `app-store-scraper` npm package, which uses that feed) **can't return more than 500 reviews per app per country**.

These two Actors read the App Store's own review catalog instead, so you get **every review** of any app, in any country.

| Actor | What | Price |
|---|---|---|
| [App Store Reviews Scraper](https://apify.com/wulfcare/app-store-reviews-scraper) | Reviews only, simplest input | $0.10 / 1,000 reviews |
| [App Store Scraper](https://apify.com/wulfcare/app-store-scraper) | Reviews, plus app details (rating histogram, version history, App Privacy labels), search, top charts, developer apps, similar apps | $0.10 / 1,000 reviews, $0.50 / 1,000 app details |

```python
from wulfcare import run   # ../wulfcare.py

reviews = run("wulfcare/app-store-reviews-scraper", {
    "appIds": ["https://apps.apple.com/us/app/spotify-music-and-podcasts/id324684580"],  # URL or numeric ID
    "countries": ["us", "gb"],
    "maxReviewsPerApp": 0,          # 0 = every review
    "reviewsSort": "newest",
    "reviewStars": ["1", "2"],      # optional: only 1- and 2-star reviews
})
for r in reviews:
    print(r["date"], r["score"], r["title"], r["appVersion"], r.get("replyText"))
```

Each review: `reviewId`, `score`, `title`, `text`, `date`, `isEdited`, `appVersion`, `replyText`, `replyDate`, `country`.

App details, search or charts (full App Store Scraper):

```python
apps = run("wulfcare/app-store-scraper", {"mode": "charts", "chartCollections": ["topfree"], "countries": ["us"]})
```

Errors (app not found, not sold in a country) come back as free rows with an `error` field and are never charged.
