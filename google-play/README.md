# Google Play reviews API: every review of any app

The official Google Play Developer API only returns reviews of **your own apps**, and only those from the last week. Libraries like the Python `google-play-scraper` run from your own IP, so big jobs depend on Google not throttling you.

These Actors read public Google Play pages and return **every review** of any app, in any country and language, with star and date filters.

| Actor | What | Price |
|---|---|---|
| [Google Play Reviews Scraper](https://apify.com/wulfcare/google-play-reviews-scraper) | Reviews only, simplest input | $0.10 / 1,000 reviews |
| [Google Play Scraper](https://apify.com/wulfcare/google-play-scraper) | Reviews, plus app details (data safety, installs, developer contacts), search, top charts, developer apps, similar apps | $0.10 / 1,000 reviews, $0.50 / 1,000 app details |

```python
from wulfcare import run   # ../wulfcare.py

reviews = run("wulfcare/google-play-reviews-scraper", {
    "appIds": ["com.spotify.music"],   # package name or Play Store URL
    "country": "us",
    "language": "en",
    "maxReviewsPerApp": 5000,
    "reviewsSort": "newest",
})
for r in reviews:
    print(r["date"], r["score"], r["thumbsUp"], r["appVersion"], r["text"][:100])
```

Each review: `reviewId`, `reviewUrl`, `score`, `text`, `date`, `thumbsUp`, `appVersion`, `replyText`, `replyDate`.

App details with Data safety:

```python
apps = run("wulfcare/google-play-scraper", {"mode": "apps", "appIds": ["com.spotify.music"]})
```
