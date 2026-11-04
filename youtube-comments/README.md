# YouTube comments API: comments and replies without an API key or quota

The [YouTube Comments Scraper on Apify](https://apify.com/wulfcare/youtube-comments-scraper) gets the comments and replies of any public video or Short, or across a channel, playlist or search. No YouTube API key, Google Cloud project or quota: it reads what a logged-out visitor sees.

```python
from wulfcare import run   # ../wulfcare.py

comments = run("wulfcare/youtube-comments-scraper", {
    "startUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    "maxComments": 100,                # per video; 0 = all
    "sortCommentsBy": "TOP_COMMENTS",  # or NEWEST_FIRST
})
for c in comments:
    print(c["voteCount"], c["replyCount"], c["hasCreatorHeart"], c["comment"])
```

Replies, each right after its comment (`type` is `reply`, `replyToCid` is the parent's `cid`):

```python
{"startUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "includeReplies": True, "maxRepliesPerComment": 5, "maxComments": 500}
```

A channel's last week, newest videos first:

```python
{"startUrls": ["https://www.youtube.com/@mkbhd"], "maxVideos": 5, "maxComments": 0, "sortCommentsBy": "NEWEST_FIRST", "oldestCommentDate": "7 days"}
```

What people say about a product, from the top search results:

```python
{"searchQueries": ["iphone 17 review"], "maxVideos": 10, "maxComments": 200}
```

Each comment: `comment`, `cid`, `author`, `voteCount`, `replyCount`, `authorIsChannelOwner`, `hasCreatorHeart`, `isPinned`, `isEdited`, `publishedTimeText`, `publishedAt`, `type`, `replyToCid`, plus the video's `title`, `videoId`, `pageUrl`, exact `commentsCount` and channel.

**Good to know:** YouTube only shows relative dates ("3 days ago"), so `publishedAt` is approximate. Like counts above 1,000 are rounded by YouTube (70K). Smaller like counts and `commentsCount` are exact. Live chat messages are not comments and aren't included.

**Switching from another Apify comments Actor:** the same input and output field names as the most used one (`startUrls`, `maxComments`, `sortCommentsBy`, `oldestCommentDate`; `comment`, `cid`, `voteCount` and so on), and `sort` + `maxItems` also work. Change only the Actor id.

**Cost:** $0.25 per 1,000 comments or replies, Apify platform usage included, no start fee. Errors and videos with comments turned off are free.

Video details: see [../youtube](../youtube). Transcripts: see [../youtube-transcripts](../youtube-transcripts).
