# Wulfcare Data scrapers: Google Trends, YouTube, App Store, Google Play, Google Jobs, Hotels and AI search APIs

Ready-to-run scrapers for data that has no good official API, with Python examples, a pytrends replacement and one-line setup for AI agents (MCP). Each one runs on [Apify](https://apify.com/wulfcare), so you don't manage proxies, IP blocks or rate limits: you send JSON, you get JSON.

**AI agents:** start with [AGENTS.md](AGENTS.md) (which scraper for which request, one curl call each). Machine-readable: [catalog.json](catalog.json), [llms.txt](llms.txt), [llms-full.txt](llms-full.txt), full input reference per scraper in [reference/](reference), OpenAPI spec per scraper at `https://api.apify.com/v2/acts/wulfcare~<name>/builds/default/openapi.json`.

**Common problems these fix:**

- `pytrends` **429 Too Many Requests** / `TooManyRequestsError` → [google-trends](google-trends) (drop-in `TrendReq`, plus more than 5 keywords on one scale and daily data for any range)
- `youtube-transcript-api` **RequestBlocked / IpBlocked: YouTube is blocking requests from your IP** → `pip install youtube-transcript-unblocked` and change one import ([package](packages/youtube-transcript-unblocked)), or call the Actor directly: [youtube-transcripts](youtube-transcripts)
- Paying **$0.01–$0.05 per transcript** on another Apify YouTube transcript Actor → [same input and output for $0.003](youtube-transcripts/README.md#switching-from-another-apify-transcript-actor) (change only the Actor id)
- YouTube Data API **quotaExceeded** (about 100 searches a day) → [youtube](youtube) (free)
- App Store reviews stuck at **500 per app** (RSS feed cap) → [app-store](app-store)
- Google Play Developer API only returns **your own apps' reviews from the last week** → [google-play](google-play)
- No official **Google Jobs API** → [google-jobs](google-jobs)
- No official **Google Hotels API** → [google-hotels](google-hotels)
- No API for what **ChatGPT search, Gemini, Copilot and Google AI Mode** actually tell users about your brand → [ai-search](ai-search)
- AI training job listings spread over 15 sites → [ai-training-jobs](ai-training-jobs) (free)

## All scrapers

| Scraper | Apify Actor | What you get | Price |
|---|---|---|---|
| Google Trends | [`wulfcare/google-trends-scraper`](https://apify.com/wulfcare/google-trends-scraper) | Interest over time, by region, related queries, Trending Now; up to 100 keywords on one scale; daily data for any range | $0.003 / report |
| YouTube transcripts | [`wulfcare/youtube-transcript-scraper`](https://apify.com/wulfcare/youtube-transcript-scraper) | Transcripts as text, timestamped segments or SRT for videos, channels, playlists, searches; drop-in input/output for other transcript Actors | $3 / 1,000 |
| YouTube | [`wulfcare/youtube-scraper`](https://apify.com/wulfcare/youtube-scraper) | Videos, Shorts, streams from searches, channels, playlists, hashtags; views, likes, comments count, channel stats | Free |
| Google Jobs | [`wulfcare/google-jobs-scraper`](https://apify.com/wulfcare/google-jobs-scraper) | Title, company, salary, description, every apply link; 27 countries | $0.004 / job |
| Google Hotels | [`wulfcare/google-hotels-scraper`](https://apify.com/wulfcare/google-hotels-scraper) | Every booking site's price per hotel and date; hotel searches | $0.80 / 1,000 prices |
| App Store | [`wulfcare/app-store-scraper`](https://apify.com/wulfcare/app-store-scraper) | Reviews (no 500 cap), app details, privacy labels, search, charts | $0.10 / 1,000 reviews |
| App Store reviews | [`wulfcare/app-store-reviews-scraper`](https://apify.com/wulfcare/app-store-reviews-scraper) | Every review of any app, any country | $0.10 / 1,000 |
| Google Play | [`wulfcare/google-play-scraper`](https://apify.com/wulfcare/google-play-scraper) | Reviews, app details with data safety, search, charts | $0.10 / 1,000 reviews |
| Google Play reviews | [`wulfcare/google-play-reviews-scraper`](https://apify.com/wulfcare/google-play-reviews-scraper) | Every review of any app, any country and language | $0.10 / 1,000 |
| ChatGPT search | [`wulfcare/chatgpt-search-scraper`](https://apify.com/wulfcare/chatgpt-search-scraper) | Answer, cited sources, recommended products, brand rank | $0.05 / answer |
| Gemini | [`wulfcare/gemini-search-scraper`](https://apify.com/wulfcare/gemini-search-scraper) | Answer, sources, products, brand rank | $1 / 1,000 |
| Google AI Mode | [`wulfcare/google-ai-mode-scraper`](https://apify.com/wulfcare/google-ai-mode-scraper) | Answer, sources, brand rank | $4.50 / 1,000 |
| Microsoft Copilot | [`wulfcare/copilot-search-scraper`](https://apify.com/wulfcare/copilot-search-scraper) | Answer, sources, brand rank | $8 / 1,000 (+ proxy) |
| AI visibility | [`wulfcare/ai-visibility-tracker`](https://apify.com/wulfcare/ai-visibility-tracker) | ChatGPT + Gemini + AI Overviews: visibility score, share of voice, HTML report | $0.04 / answer |
| AI training jobs | [`wulfcare/ai-training-jobs-scraper`](https://apify.com/wulfcare/ai-training-jobs-scraper) | Jobs from Mercor, Outlier, DataAnnotation, Alignerr and 11 more | Free |

Failed requests and empty results are never charged. Apify's free plan includes $5 of credit every month.

## Quick start (Python)

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # free account: https://console.apify.com/sign-up → Settings → API & Integrations
```

```python
from wulfcare import run   # wulfcare.py in this repo

rows = run("wulfcare/google-trends-scraper", {"searchTerms": ["coffee, tea"], "geo": "US"})
```

Every folder has a working example. The full input of each Actor is on its Apify page (Input tab).

## Any language (HTTP)

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-trends-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["coffee, tea"], "geo": "US"}'
```

Swap the Actor name and the JSON input for any scraper above. For runs longer than 5 minutes, start the run with `POST /v2/acts/{actor}/runs` and read the dataset when it finishes ([API docs](https://docs.apify.com/api/v2)).

## Use them from AI agents (MCP)

Give Claude, Cursor, VS Code or any MCP client these scrapers as tools with [Apify's MCP server](https://mcp.apify.com).

Hosted (sign in with OAuth, or send `Authorization: Bearer <APIFY_TOKEN>`):

```
https://mcp.apify.com?tools=wulfcare/google-trends-scraper,wulfcare/youtube-transcript-scraper,wulfcare/youtube-scraper,wulfcare/google-jobs-scraper,wulfcare/google-hotels-scraper,wulfcare/app-store-scraper,wulfcare/google-play-scraper,wulfcare/chatgpt-search-scraper,wulfcare/gemini-search-scraper,wulfcare/google-ai-mode-scraper
```

Local (`claude_desktop_config.json`, `.cursor/mcp.json`, ...):

```json
{
  "mcpServers": {
    "wulfcare": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server", "--tools",
               "wulfcare/google-trends-scraper,wulfcare/youtube-transcript-scraper,wulfcare/youtube-scraper,wulfcare/google-jobs-scraper,wulfcare/google-hotels-scraper,wulfcare/app-store-scraper,wulfcare/google-play-scraper,wulfcare/chatgpt-search-scraper,wulfcare/gemini-search-scraper,wulfcare/google-ai-mode-scraper"],
      "env": { "APIFY_TOKEN": "your_token" }
    }
  }
}
```

Keep only the ones you need; each becomes one tool. Agents can also read [`llms.txt`](llms.txt) for a plain-text summary of every scraper.

## Notes

- Everything is collected from public pages as a logged-out visitor sees them. No accounts or logins are used.
- Results are what each source showed at run time and can contain errors; check anything important before you rely on it.
- Questions or a field you need: open an issue here or on the Actor's Issues tab on Apify.

MIT licensed (the examples and helpers in this repo).
