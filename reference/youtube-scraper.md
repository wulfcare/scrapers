# Free YouTube Scraper: Videos, Shorts, Channels & Search

`wulfcare/youtube-scraper`: Free YouTube scraper: videos, Shorts and streams from searches (all filters), channels, playlists and hashtags. Views, likes, comments count, exact publish time, duration, description, tags, plus channel subscribers, total views and country. Same input and output as the popular YouTube Scraper.

**Use it for:**
- YouTube video metadata (views, likes, comment count, publish date, duration, tags) from searches, channels, playlists, hashtags
- YouTube channel stats (subscribers, total views, country)
- YouTube search without YouTube Data API quota

- Store page: https://apify.com/wulfcare/youtube-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~youtube-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/youtube-scraper`

**Price:**
- Free (only Apify platform usage, usually fractions of a cent)

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~youtube-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["python tutorial"], "maxResults": 20}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/youtube-scraper").call(run_input={"searchQueries": ["python tutorial"], "maxResults": 20})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `searchQueries` | array |  |  |  | Search terms: What you would type in YouTube's search box. Each term is searched separately and gets up to "Maximum videos" results (and Shorts / live streams if you ask for them below). |
| `maxResults` | integer |  | 10 | 0–999999 | Maximum videos per search term, channel, playlist or hashtag: Regular videos to get from each search term, channel (its Videos tab), playlist and hashtag. 0 = none. Video URLs in Direct URLs are always scraped. |
| `maxResultsShorts` | integer |  | 0 | 0–999999 | Maximum Shorts per search term or channel: Shorts to get from each search term (YouTube's "Shorts" search filter) and each channel (its Shorts tab). 0 = none. |
| `maxResultStreams` | integer |  | 0 | 0–999999 | Maximum live streams per search term or channel: Live streams to get from each channel (its Live tab: past, current and upcoming streams) and each search term (YouTube's "Live" filter: streams live right now). 0 = none. |
| `startUrls` | array |  | [] |  | Direct URLs: YouTube URLs: videos, Shorts, channels (@handle, /channel/UC..., /c/..., /user/...; a channel tab URL like /@name/shorts gets only that tab), playlists, search result pages (with their filters) and hashtag pages. Bare video ids, @handles and channel ids work too. |
| `sortingOrder` | string |  |  | `relevance` (Relevance), `rating` (Rating), `date` (Upload date), `views` (View count) | Sorting order: How YouTube orders the search results. YouTube doesn't follow "Upload date" strictly. |
| `dateFilter` | string |  |  | `hour` (Last hour), `today` (Today), `week` (This week), `month` (This month), `year` (This year) | Upload date: Only videos uploaded within this time. |
| `videoType` | string |  |  | `video` (Video), `movie` (Movie) | Type: Videos (default) or movies. |
| `lengthFilter` | string |  |  | `under4` (Under 4 minutes), `between420` (4-20 minutes), `plus20` (Over 20 minutes) | Duration: Only videos of this length. |
| `isHD` | boolean |  |  |  | HD: Only videos with the "HD" feature. |
| `hasSubtitles` | boolean |  |  |  | Subtitles/CC: Only videos with the "Subtitles/CC" feature. |
| `hasCC` | boolean |  |  |  | Creative Commons: Only videos with the "Creative Commons" feature. |
| `is3D` | boolean |  |  |  | 3D: Only videos with the "3D" feature. |
| `isLive` | boolean |  |  |  | Live: Only streams that are live now. |
| `isBought` | boolean |  |  |  | Purchased: Only videos with the "Purchased" feature. |
| `is4K` | boolean |  |  |  | 4K: Only videos with the "4K" feature. |
| `is360` | boolean |  |  |  | 360°: Only videos with the "360°" feature. |
| `hasLocation` | boolean |  |  |  | Location: Only videos with the "Location" feature. |
| `isHDR` | boolean |  |  |  | HDR: Only videos with the "HDR" feature. |
| `isVR180` | boolean |  |  |  | VR180: Only videos with the "VR180" feature. |
| `oldestPostDate` | string |  |  |  | Only videos published on or after: A date (2026-01-31) or an age ("7 days", "2 weeks", "3 months", "1 year"). Works for every source. On a channel listed newest first the run stops at the first older video; elsewhere older videos are skipped. |
| `sortVideosBy` | string |  | "NEWEST" | `NEWEST` (Newest), `POPULAR` (Popular), `OLDEST` (Oldest) | Channel order: The order of a channel's videos, Shorts and streams (the channel page's Latest / Popular / Oldest buttons). |
| `includeVideoDetails` | boolean |  | true |  | Open every video (likes, comments, exact date, description, tags...): On: each video's likes, comment count, exact publish time, full description with its links, hashtags, category, tags and more. Off: only what the list shows (title, views, duration, "3 days ago"), several times faster. Video URLs are always opened. |
| `includeChannelInfo` | boolean |  | true |  | Add channel info to each video: The channel's subscribers, total views, video count, country, joined date, description, links, avatar and banner, on every row (one small request per channel). |
| `maxConcurrency` | integer |  | 10 | 1–30 | Videos at a time: How many videos are fetched in parallel. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "title": "Learn Python in Less than 10 Minutes for Beginners (Fast & Easy)",
  "id": "fWjsdhR3z3c",
  "url": "https://www.youtube.com/watch?v=fWjsdhR3z3c",
  "type": "video",
  "thumbnailUrl": "https://i.ytimg.com/vi/fWjsdhR3z3c/hqdefault.jpg",
  "viewCount": 1870725,
  "likes": 39074,
  "commentsCount": 989,
  "date": "2021-05-26T12:32:40Z",
  "dateText": "May 26, 2021",
  "duration": "00:10:30",
  "durationSeconds": 630,
  "text": "In this crash course I'll be teaching you the basics of Python in less than 10 minutes. Python is super easy to learn compared to the other languages!\n\nDownload Python: https://www.python.org/\nDownload PyCharm: https://www.jetbrains.com/pyc…",
  "descriptionLinks": [
    {
      "url": "https://www.python.org/",
      "text": "https://www.python.org/"
    },
    {
      "url": "https://www.jetbrains.com/pycharm/download/",
      "text": "https://www.jetbrains.com/pycharm/download/"
    }
  ],
  "hashtags": [],
  "location": null,
  "category": "Education",
  "keywords": [
    "code palace",
    "cde palace",
    "code palce",
    "… 1 more"
  ],
  "isLive": false,
  "commentsTurnedOff": false,
  "isMembersOnly": false,
  "isAgeRestricted": false,
  "isUnlisted": false,
  "isMonetized": null,
  "isPaidContent": null,
  "collaborators": null,
  "subtitles": null,
  "translatedTitle": null,
  "translatedText": null,
  "channelName": "Indently",
  "channelId": "UCuudpdbKmQWq2PPzYgVCWlA",
  "channelUrl": "https://www.youtube.com/@Indently",
  "channelUsername": "Indently",
  "numberOfSubscribers": 369000,
  "isChannelVerified": true,
  "channelAvatarUrl": "https://yt3.googleusercontent.com/68ZQuFvv8mZTJQD65biYl2BWjKKMxkDS5k_sIdAGpRY9-p1vYsqwE1jNMTDEveZoSpkfOpKG=s900-c-k-c0x00ffffff-no-rj",
  "channelBannerUrl": "https://yt3.googleusercontent.com/V5C-vDux-5HHfGj_r8vnRHKuA9ACkkhELk2L-mudI1EJHKABL0P7qGnqz_dcEWTKyXjW1S8W=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
  "channelDescription": "Simple is better than complex_\n",
  "channelDescriptionLinks": [
    {
      "text": "Indently.io",
      "url": "https://www.indently.io/"
    },
    {
      "text": "Instagram",
      "url": "https://www.instagram.com/indentlyreels/"
    }
  ],
  "channelLocation": "United States",
  "channelJoinedDate": "2019-09-01",
  "channelTotalVideos": 1055,
  "channelTotalViews": 48698877,
  "input": "python tutorial",
  "fromYTUrl": "https://www.youtube.com/results?search_query=python%20tutorial&sp=EgIQAQ%3D%3D",
  "order": 1,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
