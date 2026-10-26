# YouTube Data API quota exceeded? Free YouTube scraper

The YouTube Data API v3 gives you 10,000 quota units a day, and a single `search.list` call costs 100, so you get about **100 searches a day** before `quotaExceeded`.

The [Free YouTube Scraper on Apify](https://apify.com/wulfcare/youtube-scraper) has no quota and no per-video fee (you only pay Apify's tiny platform usage; 341 videos with full details used $0.002 in our test, and Apify's free plan includes $5/month). It reads public YouTube pages: no API key, no Google account.

```python
from wulfcare import run   # ../wulfcare.py

videos = run("wulfcare/youtube-scraper", {
    "searchQueries": ["python tutorial"],
    "maxResults": 50,           # videos per search
    "maxResultsShorts": 0,
    "maxResultStreams": 0,
    "dateFilter": "month",      # optional search filters, as on YouTube
})
for v in videos:
    print(v["title"], v["viewCount"], v["likes"], v["date"])
```

Channels, playlists and hashtags go in `startUrls`: `{"startUrls": [{"url": "https://www.youtube.com/@mkbhd"}], "maxResults": 100}`.

Each video: `title`, `id`, `url`, `viewCount`, `likes`, `commentsCount`, `date`, `duration`, `text` (description), `hashtags`, `keywords`, `category`, plus channel name, subscribers, total views and country. Same input and output format as Apify's popular YouTube Scraper, so it's a drop-in swap.

Transcripts: see [../youtube-transcripts](../youtube-transcripts).
