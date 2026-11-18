# YouTube Shorts Scraper: Search, Channels, Views & Likes

`wulfcare/youtube-shorts-scraper`: Scrape YouTube Shorts from search terms and channels: views, likes, comment count, publish date, description, hashtags, plus channel subscribers. No login, no API key. $0.50 per 1,000 Shorts, no start fee.

**Use it for:**
- YouTube Shorts from search terms or channels with views, likes, comment count, publish date and hashtags

- Store page: https://apify.com/wulfcare/youtube-shorts-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~youtube-shorts-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/youtube-shorts-scraper`

**Price:**
- $0.0005 per short (video): One YouTube Short with all its details. Errors and not-found inputs are never charged. No start fee.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~youtube-shorts-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchQueries": ["cooking hacks"], "maxResultsShorts": 20}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/youtube-shorts-scraper").call(run_input={"searchQueries": ["cooking hacks"], "maxResultsShorts": 20})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `searchQueries` | array |  |  |  | Search terms: What you would type in YouTube's search box. Each term is searched with YouTube's Shorts filter and gets up to "Maximum Shorts" results. |
| `maxResultsShorts` | integer |  | 50 | 1–999999 | Maximum Shorts per search term or channel: Shorts to get from each search term and each channel (its Shorts tab). |
| `startUrls` | array |  | [] |  | Direct URLs: Channels (@handle, /channel/UC..., /@name/shorts) to get their Shorts tab, or Shorts URLs (youtube.com/shorts/ID) to get those Shorts. |
| `sortingOrder` | string |  |  | `relevance` (Relevance), `rating` (Rating), `date` (Upload date), `views` (View count) | Sorting order: How YouTube orders the search results. YouTube doesn't follow "Upload date" strictly. |
| `dateFilter` | string |  |  | `hour` (Last hour), `today` (Today), `week` (This week), `month` (This month), `year` (This year) | Upload date: Only videos uploaded within this time. |
| `oldestPostDate` | string |  |  |  | Only videos published on or after: A date (2026-01-31) or an age ("7 days", "2 weeks", "3 months", "1 year"). Works for every source. On a channel listed newest first the run stops at the first older video; elsewhere older videos are skipped. |
| `sortVideosBy` | string |  | "NEWEST" | `NEWEST` (Newest), `POPULAR` (Popular), `OLDEST` (Oldest) | Channel order: The order of a channel's videos, Shorts and streams (the channel page's Latest / Popular / Oldest buttons). |
| `includeVideoDetails` | boolean |  | true |  | Open every video (likes, comments, exact date, description, tags...): On: each video's likes, comment count, exact publish time, full description with its links, hashtags, category, tags and more. Off: only what the list shows (title, views, duration, "3 days ago"), several times faster. Video URLs are always opened. |
| `includeChannelInfo` | boolean |  | true |  | Add channel info to each video: The channel's subscribers, total views, video count, country, joined date, description, links, avatar and banner, on every row (one small request per channel). |
| `maxConcurrency` | integer |  | 10 | 1–30 | Videos at a time: How many videos are fetched in parallel. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "title": "Useful Kitchen Hacks and DIY Solutions for Easier Cooking! 🍳 #easy #quick #cooking #recipes",
  "id": "fHuCMjddNr8",
  "url": "https://www.youtube.com/shorts/fHuCMjddNr8",
  "type": "shorts",
  "thumbnailUrl": "https://i.ytimg.com/vi/fHuCMjddNr8/hqdefault.jpg",
  "viewCount": 190143,
  "likes": 2312,
  "commentsCount": 10,
  "date": "2026-11-12T17:00:08Z",
  "dateText": "Nov 12, 2026",
  "duration": "00:02:58",
  "durationSeconds": 178,
  "text": "Discover clever kitchen hacks and practical DIY solutions that simplify food preparation, save time, and make everyday cooking easier and more enjoyable.",
  "descriptionLinks": [],
  "hashtags": [],
  "location": null,
  "category": "People & Blogs",
  "keywords": [
    "simple",
    "cooking",
    "tricks"
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
  "channelName": "Beamish Mealy",
  "channelId": "UCXEJKxzUrHy8p9XQUSojgdA",
  "channelUrl": "https://www.youtube.com/@BeamishMealy",
  "channelUsername": "BeamishMealy",
  "numberOfSubscribers": 3060,
  "isChannelVerified": false,
  "channelAvatarUrl": "https://yt3.googleusercontent.com/TQgNRuTL-wau93UsWXnmOgCR02z3XnzsziZewlWSfPp_9dMwZc30ZrKrY-xbd2HkW70pXD7gA9A=s900-c-k-c0x00ffffff-no-rj",
  "channelBannerUrl": null,
  "channelDescription": "We strive to bring you the best and most creative recipes, cooking skills, and kitchen techniques. From delicious homemade meals to inspiring new ideas, we share our passion for food, creativity, and the art of cooking.\n\nDiscover new flavor…",
  "channelDescriptionLinks": [],
  "channelLocation": "United States",
  "channelJoinedDate": "2026-10-18",
  "channelTotalVideos": 18,
  "channelTotalViews": 2641706,
  "input": "cooking hacks",
  "fromYTUrl": "https://www.youtube.com/results?search_query=cooking%20hacks&sp=EgIQCQ%3D%3D",
  "order": 8,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
