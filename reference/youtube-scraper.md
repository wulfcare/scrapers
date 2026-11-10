# YouTube Scraper: Videos, Shorts, Channels & Search

`wulfcare/youtube-scraper`: YouTube scraper: videos, Shorts and streams from searches, channels, playlists and hashtags. Views, likes, comments count, publish time, duration, tags, plus channel subscribers, total views and country. Same input and output as the popular YouTube Scraper. Free until Nov 18, then $0.90 per 1,000.

**Use it for:**
- YouTube video metadata (views, likes, comment count, publish date, duration, tags) from searches, channels, playlists, hashtags
- YouTube channel stats (subscribers, total views, country)
- YouTube search without YouTube Data API quota

- Store page: https://apify.com/wulfcare/youtube-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~youtube-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/youtube-scraper`

**Price:**
- Free (only Apify platform usage, usually fractions of a cent)
- From 2026-11-18: $0.0009 per video (video): One YouTube video, Short or stream row with all its details. Errors and not-found inputs are never charged. No start fee.

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
  "title": "Python for Data Analytics - Full Course for Beginners",
  "id": "wUSDVGivd-8",
  "url": "https://www.youtube.com/watch?v=wUSDVGivd-8",
  "type": "video",
  "thumbnailUrl": "https://i.ytimg.com/vi/wUSDVGivd-8/hqdefault.jpg",
  "viewCount": 1651110,
  "likes": 37906,
  "commentsCount": 1195,
  "date": "2024-06-07T12:01:05Z",
  "dateText": "Jun 7, 2024",
  "duration": "11:09:41",
  "durationSeconds": 40181,
  "text": "📁 FREE Course Files & Project 👉 https://lukeb.co/python_repo\n🏆 Supporter Access: Problems, Certificate, & More 👉 https://lukeb.co/python\n\nMy FREE Course to be a Data Analyst 👉 https://lukebarousse.com/5daycourse\n\n📌💬 See pinned comment for t…",
  "descriptionLinks": [
    {
      "url": "https://lukeb.co/python_repo",
      "text": "https://lukeb.co/python_repo"
    },
    {
      "url": "https://lukeb.co/python",
      "text": "https://lukeb.co/python"
    },
    {
      "url": "https://lukebarousse.com/5daycourse",
      "text": "https://lukebarousse.com/5daycourse"
    },
    "… 26 more"
  ],
  "hashtags": [
    "#datanerd",
    "#dataanalyst",
    "#datascience"
  ],
  "location": null,
  "category": "Science & Technology",
  "keywords": [
    "data viz by luke",
    "business intelligence",
    "data science",
    "… 15 more"
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
  "channelName": "Luke Barousse",
  "channelId": "UCLLw7jmFsvfIVaUFsLs8mlQ",
  "channelUrl": "https://www.youtube.com/@LukeBarousse",
  "channelUsername": "LukeBarousse",
  "numberOfSubscribers": 681000,
  "isChannelVerified": true,
  "channelAvatarUrl": "https://yt3.googleusercontent.com/ytc/AIdro_my6YXWfudW8qM_i1Na9IWEbiIUtVgb54u0XVVmtlYQig=s900-c-k-c0x00ffffff-no-rj",
  "channelBannerUrl": "https://yt3.googleusercontent.com/NiqHB8Sy0UaObmZgUVDE3eLrp-GZkn445VvZIj1mB1VRXRwxQGotWNNGLkTnF3LH6k9NmfCj5w=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
  "channelDescription": "What's up, Data Nerds! I'm Luke, a data analyst who loves making tutorials.\n\n❓ If you have a question, drop a comment in any video. \n\n📩 Email is for business inquiries only, please.\n\n\n",
  "channelDescriptionLinks": [
    {
      "text": "My FREE Data Courses",
      "url": "https://lukebarousse.com/crash-courses"
    },
    {
      "text": "All My Courses ",
      "url": "https://lukebarousse.com/courses"
    },
    {
      "text": "My Job-Skills App",
      "url": "https://datanerd.tech"
    },
    "… 2 more"
  ],
  "channelLocation": "United States",
  "channelJoinedDate": "2020-08-03",
  "channelTotalVideos": 172,
  "channelTotalViews": 36148433,
  "input": "python tutorial",
  "fromYTUrl": "https://www.youtube.com/results?search_query=python%20tutorial&sp=EgIQAQ%3D%3D",
  "order": 8,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
