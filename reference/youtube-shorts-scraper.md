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
  "title": "Giving $10,000 To A Random Subscriber",
  "id": "aNI2jv7lBPQ",
  "url": "https://www.youtube.com/shorts/aNI2jv7lBPQ",
  "type": "shorts",
  "thumbnailUrl": "https://i.ytimg.com/vi/aNI2jv7lBPQ/hqdefault.jpg",
  "viewCount": 73876519,
  "likes": 1614646,
  "commentsCount": 32166,
  "date": "2026-10-09T16:00:01Z",
  "dateText": "Oct 9, 2026",
  "duration": "00:00:40",
  "durationSeconds": 40,
  "text": null,
  "descriptionLinks": [],
  "hashtags": [],
  "location": null,
  "category": "Entertainment",
  "keywords": [],
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
  "channelName": "MrBeast",
  "channelId": "UCX6OQ3DkcsbYNE6H8uQQuVA",
  "channelUrl": "https://www.youtube.com/@MrBeast",
  "channelUsername": "MrBeast",
  "numberOfSubscribers": 525000000,
  "isChannelVerified": true,
  "channelAvatarUrl": "https://yt3.googleusercontent.com/nxYrc_1_2f77DoBadyxMTmv7ZpRZapHR5jbuYe7PlPd5cIRJxtNNEYyOC0ZsxaDyJJzXrnJiuDE=s900-c-k-c0x00ffffff-no-rj",
  "channelBannerUrl": "https://yt3.googleusercontent.com/mHMO_eEMp0dPvh0ADwXhPXNYb_GnjSVsLI8biqF1CpxT8OPl7izhNQsDPD3JHhd5y5Mg9GrP=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
  "channelDescription": "SUBSCRIBE FOR A COOKIE!\nNew MrBeast or MrBeast Gaming video every single Saturday at noon eastern time!\nAccomplishments:\n- Raised $20,000,000 To Plant 20,000,000 Trees\n- Removed 30,000,000 pounds of trash from the ocean\n- Helped 2,000 peopl…",
  "channelDescriptionLinks": [
    {
      "text": "Follow",
      "url": "https://www.instagram.com/mrbeast/"
    },
    {
      "text": "Twitter",
      "url": "https://twitter.com/MrBeast"
    },
    {
      "text": "Facebook",
      "url": "https://facebook.com/mrbeast/"
    }
  ],
  "channelLocation": "United States",
  "channelJoinedDate": "2012-02-19",
  "channelTotalVideos": 1012,
  "channelTotalViews": 146262472980,
  "input": "https://www.youtube.com/@MrBeast",
  "fromYTUrl": "https://www.youtube.com/@MrBeast/shorts",
  "order": 5,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
