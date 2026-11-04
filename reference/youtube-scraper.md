# YouTube Scraper: Videos, Shorts, Channels & Search

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
  "title": "Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)",
  "id": "dQw4w9WgXcQ",
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "type": "video",
  "thumbnailUrl": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
  "viewCount": 1833429343,
  "likes": 19491500,
  "commentsCount": 2461285,
  "date": "2009-10-25T06:57:33Z",
  "dateText": "Oct 24, 2009",
  "duration": "00:03:33",
  "durationSeconds": 213,
  "text": "The official video for “Never Gonna Give You Up” by Rick Astley. \n\nNever: The Autobiography 📚 OUT NOW! \nFollow this link to get your copy and listen to Rick’s ‘Never’ playlist ❤️ #RickAstleyNever\nhttps://linktr.ee/rickastleynever\n\n“Never Go…",
  "descriptionLinks": [
    {
      "url": "https://linktr.ee/rickastleynever",
      "text": "https://linktr.ee/rickastleynever"
    },
    {
      "url": "https://RickAstley.lnk.to/YTSubID",
      "text": "https://RickAstley.lnk.to/YTSubID"
    },
    {
      "url": "https://RickAstley.lnk.to/FBFollowID",
      "text": "https://RickAstley.lnk.to/FBFollowID"
    },
    "… 8 more"
  ],
  "hashtags": [
    "#OfficialMusicVideo",
    "#NeverGonnaGiveYouUp",
    "#RickAstleyNever",
    "… 2 more"
  ],
  "location": null,
  "category": "Music",
  "keywords": [
    "rick astley",
    "Never Gonna Give You Up",
    "nggyu",
    "… 24 more"
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
  "channelName": "Rick Astley",
  "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
  "channelUrl": "https://www.youtube.com/@RickAstleyYT",
  "channelUsername": "RickAstleyYT",
  "numberOfSubscribers": 4560000,
  "isChannelVerified": true,
  "channelAvatarUrl": "https://yt3.googleusercontent.com/_ShEGOdg-t5YGJse14Ooq6FYBZqX_QSlhaTNjG06miYusm5lWm1UroLyVxnYtahADfRTVLtuVQ=s900-c-k-c0x00ffffff-no-rj",
  "channelBannerUrl": "https://yt3.googleusercontent.com/pi1YBgcetxpQG-xtEKHBLwe3nUxoo-cT1AKYfqLxh8krCgnkpZZM5zOtP2VlFfSFnRFi8EyA=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
  "channelDescription": "Rick Astley’s Swinging Christmas 2026 🎄 Dec 9th, Royal Albert Hall. SOLD OUT ❤️\n",
  "channelDescriptionLinks": [
    {
      "text": "Swinging Christmas tickets",
      "url": "https://lnk.to/RASC26"
    },
    {
      "text": "New single 'Raindrops'",
      "url": "https://rickastley.lnk.to/Raindrops"
    },
    {
      "text": "Website",
      "url": "https://www.rickastley.co.uk/"
    },
    "… 8 more"
  ],
  "channelLocation": "United Kingdom",
  "channelJoinedDate": "2015-02-01",
  "channelTotalVideos": 439,
  "channelTotalViews": 2596229655,
  "input": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "fromYTUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "order": 1,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
