# Steam Reviews Scraper: All Reviews, Any Game, No Key

`wulfcare/steam-reviews-scraper`: Scrape every Steam review of any game, with no cap and no API key: newest/helpful sort, positive/negative, any language, playtime, votes, Steam Deck and developer replies. $0.10 per 1,000 reviews, no start fee, errors free.

**Use it for:**
- every Steam review of a game (any language, no API key) with votes, playtime, Steam Deck flag and developer replies

- Store page: https://apify.com/wulfcare/steam-reviews-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~steam-reviews-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/steam-reviews-scraper`

**Price:**
- $0.0001 per review (review): One Steam review with the recommendation, text, date, playtime, votes and the developer reply. Games not found and failed requests are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~steam-reviews-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"appIds": ["1145360"], "maxReviewsPerApp": 200}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/steam-reviews-scraper").call(run_input={"appIds": ["1145360"], "maxReviewsPerApp": 200})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `appIds` | array | yes |  |  | Games: Steam app ids (1145360), store URLs (https://store.steampowered.com/app/1145360/) or game names (the best match on Steam is used). Every review of each game is fetched, up to the limit below. |
| `maxReviewsPerApp` | integer |  | 1000 | 0– | Maximum reviews per game: 0 = every review the game has (big games have hundreds of thousands). |
| `reviewsSort` | string |  | "newest" | `newest` (Newest first), `helpful` (Most helpful first), `updated` (Recently updated first) | Order: Newest first can also stop at a date (below). |
| `reviewType` | string |  | "all" | `all` (All), `positive` (Positive (recommended) only), `negative` (Negative (not recommended) only) | Reviews: Positive = the reviewer recommends the game (thumbs up). Filtered on Steam's side, so you only pay for the reviews you want. |
| `languages` | array |  | ["all"] |  | Languages: "all", or Steam language names like english, schinese, russian, spanish, brazilian, german, french, japanese, koreana. |
| `purchaseType` | string |  | "all" | `all` (Everyone (incl. free-to-play and gifted)), `steam` (Bought on Steam only), `key` (Activated with a key only) | Who wrote them: Everyone matches the review counts on free-to-play games. "Bought on Steam only" matches the default count on a paid game's store page. |
| `reviewsSince` | string |  |  |  | Only reviews since: Skip reviews older than this, e.g. 2026-09-01 or "30 days". The run stops as soon as it reaches older reviews (uses Newest first). |
| `includeReviewerIds` | boolean |  | false |  | Include reviewer Steam IDs: Off by default. On: each row gets the reviewer's public Steam ID and a link to the review. |
| `maxConcurrency` | integer |  | 5 | 1–20 | Games at a time: Each game's reviews are read page by page; this many games run in parallel. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "appId": "1145360",
  "appName": "Hades",
  "reviewId": "240453969",
  "recommended": true,
  "text": "I LOVE IT (Scratches the Wakfu/Dofus dungeon experiences in a crazy way) \r\nFinished the game 87 times, moving to Hades 2",
  "language": "english",
  "createdAt": "2026-11-17T21:36:01Z",
  "updatedAt": "2026-11-17T21:36:01Z",
  "votesUp": 0,
  "votesFunny": 0,
  "helpfulScore": 0.5,
  "commentCount": 0,
  "steamPurchase": true,
  "receivedForFree": false,
  "refunded": false,
  "writtenDuringEarlyAccess": false,
  "primarilySteamDeck": false,
  "playtimeAtReviewHours": 207.1,
  "playtimeForeverHours": 207.1,
  "playtimeLastTwoWeeksHours": 55.6,
  "deckPlaytimeAtReviewHours": null,
  "lastPlayedAt": "2026-11-17T21:34:38Z",
  "authorReviewCount": 4,
  "developerResponse": null,
  "developerResponseAt": null,
  "reviewUrl": null,
  "authorSteamId": null,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
