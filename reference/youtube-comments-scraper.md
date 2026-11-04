# YouTube Comments Scraper: Replies, Likes & Hearts

`wulfcare/youtube-comments-scraper`: Scrape YouTube comments and replies from any video or Short, or from a channel, playlist or search. Text, author, likes, reply count, creator heart, pinned, date and exact comment total. No API key or quota. Same input and output as the popular YouTube Comments Scraper. $0.25 per 1,000 comments.

**Use it for:**
- comments and replies of YouTube videos and Shorts with likes, reply counts, creator hearts, pinned flags and dates
- comments across a channel, playlist or search, optionally only since a date
- YouTube comments for sentiment analysis, brand monitoring or AI datasets, without a YouTube API key or quota
- drop-in replacement for other Apify YouTube comments Actors: accepts startUrls + maxComments + sortCommentsBy and startUrls + sort + maxItems, same output field names as the most used one

- Store page: https://apify.com/wulfcare/youtube-comments-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~youtube-comments-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/youtube-comments-scraper`

**Price:**
- $0.00025 per comment (comment): One YouTube comment or reply row. Errors, unavailable videos and turned-off comments are never charged. No start fee.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~youtube-comments-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "maxComments": 100, "sortCommentsBy": "TOP_COMMENTS"}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/youtube-comments-scraper").call(run_input={"startUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "maxComments": 100, "sortCommentsBy": "TOP_COMMENTS"})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `startUrls` | array |  |  |  | YouTube URLs: Videos or Shorts (one per line; {"url": ...} objects work too) to get comments from (watch, youtu.be, /shorts/ URLs or 11-character video IDs). Channel URLs (@handle, /channel/UC...; add /shorts for Shorts), playlist URLs and search result URLs also work: their newest/first "Maximum videos" videos are used. |
| `maxComments` | integer |  | 100 | 0–1000000 | Maximum comments per video: Comments (and replies, when on) to get from each video. 0 = all of them. ~1,000 comments take about 20 seconds. |
| `sortCommentsBy` | string |  | "NEWEST_FIRST" | `TOP_COMMENTS` (Top comments), `NEWEST_FIRST` (Newest first) | Sort comments by: YouTube's own Top / Newest order. |
| `includeReplies` | boolean |  | false |  | Include replies: Also get the replies to each comment, right after it (type "reply", replyToCid = the comment). Replies count toward "Maximum comments". |
| `maxRepliesPerComment` | integer |  | 0 | 0–100000 | Maximum replies per comment: 0 = all replies of each comment. |
| `oldestCommentDate` | string |  |  |  | Only comments posted on or after: A date (2026-01-31) or an age ("7 days", "3 months"). With "Newest first" the run stops reading a video once comments get older. YouTube only says "x days ago", so the cut is approximate. |
| `searchQueries` | array |  |  |  | Search terms: Get comments from the top "Maximum videos" YouTube search results of each term (e.g. a product or brand name). |
| `maxVideos` | integer |  | 10 | 1–10000 | Maximum videos per channel, playlist or search: How many videos each channel (newest first), playlist or search term contributes. |
| `maxItems` | integer |  |  | 1–10000000 | Maximum comments in total: Optional cap for the whole run (all videos together). Empty = no cap. |
| `maxConcurrency` | integer |  | 5 | 1–20 | Videos at a time: How many videos are read in parallel. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "comment": "(comment text removed)",
  "cid": "UgyBzai4Mnxf_2fOSLd4AaABAg",
  "author": "(name removed)",
  "videoId": "NiCgcUTL9_Q",
  "pageUrl": "https://www.youtube.com/watch?v=NiCgcUTL9_Q",
  "commentsCount": 6239,
  "replyCount": 55,
  "voteCount": 308,
  "authorIsChannelOwner": true,
  "hasCreatorHeart": false,
  "type": "comment",
  "replyToCid": null,
  "title": "Fiber Optics are so much cooler than I thought",
  "publishedTimeText": "3 weeks ago",
  "publishedAt": "2026-10-13T21:00:24Z",
  "isEdited": false,
  "isPinned": true,
  "replyLevel": 0,
  "authorChannelId": "(removed)",
  "authorChannelUrl": "(removed)",
  "authorAvatarUrl": "(removed)",
  "authorIsVerified": true,
  "authorIsArtist": false,
  "channelName": "Veritasium",
  "channelId": "UCHnyfMqiRRG1u-2MsSQLbXA",
  "channelUrl": "https://www.youtube.com/@veritasium",
  "input": "https://www.youtube.com/@veritasium",
  "order": 2,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
