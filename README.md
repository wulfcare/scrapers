# Wulfcare Data scrapers: Google Trends, YouTube, App Store, Google Play, Steam, Shopify, Google Jobs, Hotels, Flights and AI search APIs

Ready-to-run scrapers for data that has no good official API, with Python examples, a pytrends replacement and one-line setup for AI agents (MCP). Each one runs on [Apify](https://apify.com/wulfcare), so you don't manage proxies, IP blocks or rate limits: you send JSON, you get JSON.

**AI agents:** start with [AGENTS.md](AGENTS.md) (which scraper for which request, one curl call each). Machine-readable: [catalog.json](catalog.json), [llms.txt](llms.txt), [llms-full.txt](llms-full.txt), full input reference per scraper in [reference/](reference), OpenAPI spec per scraper at `https://api.apify.com/v2/acts/wulfcare~<name>/builds/default/openapi.json`.

**Common problems these fix:**

- `pytrends` **429 Too Many Requests** / `TooManyRequestsError` → [google-trends](google-trends) (drop-in `TrendReq`, plus more than 5 keywords on one scale and daily data for any range)
- `youtube-transcript-api` **RequestBlocked / IpBlocked: YouTube is blocking requests from your IP** → `pip install youtube-transcript-unblocked` and change one import ([package](packages/youtube-transcript-unblocked)), or call the Actor directly: [youtube-transcripts](youtube-transcripts)
- Paying **$0.01–$0.05 per transcript** on another Apify YouTube transcript Actor → [same input and output for $0.003](youtube-transcripts/README.md#switching-from-another-apify-transcript-actor) (change only the Actor id)
- YouTube Data API **quotaExceeded** (about 100 searches a day) → [youtube](youtube)
- YouTube comments and replies with **no API key or quota** → [youtube-comments](youtube-comments)
- Paying more on the most used Apify YouTube comments Actor → [same input and output field names for $0.25 per 1,000](youtube-comments) (change only the Actor id)
- App Store reviews stuck at **500 per app** (RSS feed cap) → [app-store](app-store)
- Google Play Developer API only returns **your own apps' reviews from the last week** → [google-play](google-play)
- No official **Google Jobs API** → [google-jobs](google-jobs)
- No official **Google Hotels API** → [google-hotels](google-hotels)
- No official **Google Flights API** → [google-flights](google-flights) (prices, price tracking, total trip cost)
- No API for what **ChatGPT search, Gemini, Copilot and Google AI Mode** actually tell users about your brand → [ai-search](ai-search)
- Every **Steam review** of a game, any language, with no API key → [`wulfcare/steam-reviews-scraper`](https://apify.com/wulfcare/steam-reviews-scraper)
- No official **Shopify App Store reviews API** → [`wulfcare/shopify-app-store-reviews-scraper`](https://apify.com/wulfcare/shopify-app-store-reviews-scraper)
- **Flight price drop alerts** on a schedule (drops, rises, all-time low, under-target) → [`wulfcare/flight-price-tracker`](https://apify.com/wulfcare/flight-price-tracker)
- **YouTube Shorts** views and likes from searches or channels → [`wulfcare/youtube-shorts-scraper`](https://apify.com/wulfcare/youtube-shorts-scraper)
- Everything **trending on Google right now**, any country → [`wulfcare/google-trends-trending-now`](https://apify.com/wulfcare/google-trends-trending-now)
- AI training job listings spread over 15 sites → [ai-training-jobs](ai-training-jobs) (free)

**Guides:** [youtube-transcript-api IpBlocked](https://wulfcare.github.io/scrapers/youtube-transcript-api-ipblocked/) · [pytrends 429](https://wulfcare.github.io/scrapers/pytrends-429-fix/) · [YouTube quotaExceeded](https://wulfcare.github.io/scrapers/youtube-api-quota-exceeded/) · [export YouTube comments to CSV](https://wulfcare.github.io/scrapers/export-youtube-comments-csv/) · [YouTube comments scrapers compared](https://wulfcare.github.io/scrapers/youtube-comments-scrapers-compared/)

**Free history:** [PastCharts](https://pastcharts.com/) saves App Store and Google Play top charts and Google trending searches every day, free to browse or download as JSON and CSV. AI agents can query it with no key through its MCP server at `https://pastcharts.com/mcp`. Use the scrapers here when you need today's data.

## All scrapers

| Scraper | Apify Actor | What you get | Price |
|---|---|---|---|
| Google Trends | [`wulfcare/google-trends-scraper`](https://apify.com/wulfcare/google-trends-scraper) | Interest over time, by region, related queries, Trending Now; up to 100 keywords on one scale; daily data for any range | $0.003 / report |
| YouTube transcripts | [`wulfcare/youtube-transcript-scraper`](https://apify.com/wulfcare/youtube-transcript-scraper) | Transcripts as text, timestamped segments or SRT for videos, channels, playlists, searches; drop-in input/output for other transcript Actors | $3 / 1,000 |
| YouTube | [`wulfcare/youtube-scraper`](https://apify.com/wulfcare/youtube-scraper) | Videos, Shorts, streams from searches, channels, playlists, hashtags; views, likes, comments count, channel stats | Free until 2026-11-18, then $0.90 / 1,000 |
| YouTube comments | [`wulfcare/youtube-comments-scraper`](https://apify.com/wulfcare/youtube-comments-scraper) | Comments and replies with likes, reply counts, creator hearts, pinned flags and dates; videos, Shorts, channels, playlists, searches | $0.25 / 1,000 |
| Google Jobs | [`wulfcare/google-jobs-scraper`](https://apify.com/wulfcare/google-jobs-scraper) | Title, company, salary, description, every apply link; 27 countries | $0.004 / job |
| Google Hotels | [`wulfcare/google-hotels-scraper`](https://apify.com/wulfcare/google-hotels-scraper) | Every booking site's price per hotel and date; hotel searches | $0.80 / 1,000 prices |
| Google Flights | [`wulfcare/google-flights-scraper`](https://apify.com/wulfcare/google-flights-scraper) | Flights, prices and Google's low / typical / high verdict; price tracking between runs; total trip cost with a hotel | $0.50 / 1,000 |
| App Store | [`wulfcare/app-store-scraper`](https://apify.com/wulfcare/app-store-scraper) | Reviews (no 500 cap), app details, privacy labels, search, charts | $0.10 / 1,000 reviews |
| App Store reviews | [`wulfcare/app-store-reviews-scraper`](https://apify.com/wulfcare/app-store-reviews-scraper) | Every review of any app, any country | $0.10 / 1,000 |
| Google Play | [`wulfcare/google-play-scraper`](https://apify.com/wulfcare/google-play-scraper) | Reviews, app details with data safety, search, charts | $0.10 / 1,000 reviews |
| Google Play reviews | [`wulfcare/google-play-reviews-scraper`](https://apify.com/wulfcare/google-play-reviews-scraper) | Every review of any app, any country and language | $0.10 / 1,000 |
| ChatGPT search | [`wulfcare/chatgpt-search-scraper`](https://apify.com/wulfcare/chatgpt-search-scraper) | Answer, cited sources, recommended products, brand rank | $0.05 / answer |
| Gemini | [`wulfcare/gemini-search-scraper`](https://apify.com/wulfcare/gemini-search-scraper) | Answer, sources, products, brand rank | $1 / 1,000 (+ proxy) |
| Google AI Mode | [`wulfcare/google-ai-mode-scraper`](https://apify.com/wulfcare/google-ai-mode-scraper) | Answer, sources, brand rank | $4.50 / 1,000 |
| Microsoft Copilot | [`wulfcare/copilot-search-scraper`](https://apify.com/wulfcare/copilot-search-scraper) | Answer, sources, brand rank | $8 / 1,000 (+ proxy) |
| AI visibility | [`wulfcare/ai-visibility-tracker`](https://apify.com/wulfcare/ai-visibility-tracker) | ChatGPT + Gemini + AI Overviews: visibility score, share of voice, HTML report | $0.04 / answer |
| Google Trends Trending Now | [`wulfcare/google-trends-trending-now`](https://apify.com/wulfcare/google-trends-trending-now) | Every search trending on Google now: volume, % increase, related searches, news; 4/24/48/168 h windows | $0.30 / 1,000 trends |
| YouTube Shorts | [`wulfcare/youtube-shorts-scraper`](https://apify.com/wulfcare/youtube-shorts-scraper) | Shorts from searches and channels: views, likes, comment count, date, hashtags, channel subscribers | $0.50 / 1,000 |
| Flight price tracker | [`wulfcare/flight-price-tracker`](https://apify.com/wulfcare/flight-price-tracker) | Scheduled Google Flights checks: which fares dropped or rose, new/gone flights, all-time low, under-target alerts | $0.15 / 1,000 flights |
| Steam reviews | [`wulfcare/steam-reviews-scraper`](https://apify.com/wulfcare/steam-reviews-scraper) | Every review of any game: text, votes, playtime, language, Steam Deck, developer replies | $0.10 / 1,000 |
| Shopify App Store reviews | [`wulfcare/shopify-app-store-reviews-scraper`](https://apify.com/wulfcare/shopify-app-store-reviews-scraper) | Every review of any Shopify app: stars, text, date, merchant store and country, developer reply | $0.03 / 1,000 |
| Bing Copilot | [`wulfcare/bing-copilot-scraper`](https://apify.com/wulfcare/bing-copilot-scraper) | Answer as markdown, cited sources, brand mentioned or cited | $3 / 1,000 ($10 with residential proxy) |
| AI training jobs | [`wulfcare/ai-training-jobs-scraper`](https://apify.com/wulfcare/ai-training-jobs-scraper) | Jobs from Mercor, Outlier, DataAnnotation, Alignerr and 11 more | Free |

Failed requests and empty results are never charged. Apify's free plan includes $5 of credit every month.

## YouTube transcripts in Python (easiest)

1. Get a free Apify token: sign up at https://console.apify.com/sign-up, then **Settings → API & Integrations → copy the token** ($5 free credit every month).
2. Install and set the token:

```bash
pip install youtube-transcript-unblocked
export APIFY_TOKEN=apify_api_...        # Windows PowerShell: $env:APIFY_TOKEN="apify_api_..."
```

3. Get a transcript:

```python
from youtube_transcript_unblocked import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi().fetch("https://www.youtube.com/watch?v=UF8uR6Z6KLc")

print(" ".join(s.text for s in transcript))   # the whole transcript as text
for s in transcript:                           # or line by line with timestamps
    print(f"{s.start:7.1f}s  {s.text}")
```

Other languages: `fetch(video, languages=["es", "en"])` (Spanish, else English). Many videos in one go: `fetch_many([...])`. Already using `youtube-transcript-api`? Only the import changes; your existing code keeps working, including on AWS/GCP/Azure where YouTube blocks it. Cost: $0.003 per transcript, videos without captions free. Details: [packages/youtube-transcript-unblocked](packages/youtube-transcript-unblocked).

## Quick start (Python, any scraper)

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

**One-click bundles** (also listed in the [official MCP Registry](https://registry.modelcontextprotocol.io) as `io.github.wulfcare/<name>`). Paste one URL into your MCP client; each scraper in it becomes one tool:

| Bundle | Registry name | MCP URL |
|---|---|---|
| Google Flights | `io.github.wulfcare/google-flights` | `https://mcp.apify.com/?tools=wulfcare/google-flights-scraper,wulfcare/flight-price-tracker` |
| Google Hotels | `io.github.wulfcare/google-hotels` | `https://mcp.apify.com/?tools=wulfcare/google-hotels-scraper` |
| Google Trends | `io.github.wulfcare/google-trends` | `https://mcp.apify.com/?tools=wulfcare/google-trends-scraper,wulfcare/google-trends-trending-now` |
| ChatGPT, Gemini, Copilot & AI Mode answers | `io.github.wulfcare/chatgpt-gemini-copilot-search` | `https://mcp.apify.com/?tools=wulfcare/chatgpt-search-scraper,wulfcare/gemini-search-scraper,wulfcare/copilot-search-scraper,wulfcare/google-ai-mode-scraper` |
| AI Brand Visibility Tracker | `io.github.wulfcare/ai-brand-visibility` | `https://mcp.apify.com/?tools=wulfcare/ai-visibility-tracker` |
| Google Play & App Store reviews | `io.github.wulfcare/app-reviews` | `https://mcp.apify.com/?tools=wulfcare/google-play-reviews-scraper,wulfcare/app-store-reviews-scraper,wulfcare/google-play-scraper` |
| Steam Reviews | `io.github.wulfcare/steam-reviews` | `https://mcp.apify.com/?tools=wulfcare/steam-reviews-scraper` |
| Shopify App Store Reviews | `io.github.wulfcare/shopify-app-reviews` | `https://mcp.apify.com/?tools=wulfcare/shopify-app-store-reviews-scraper` |
| YouTube transcripts, comments & videos | `io.github.wulfcare/youtube-transcripts-comments` | `https://mcp.apify.com/?tools=wulfcare/youtube-transcript-scraper,wulfcare/youtube-comments-scraper,wulfcare/youtube-shorts-scraper,wulfcare/youtube-scraper` |
| Google Jobs | `io.github.wulfcare/google-jobs` | `https://mcp.apify.com/?tools=wulfcare/google-jobs-scraper,wulfcare/ai-training-jobs-scraper` |

All of them at once, or any mix you choose:

Hosted (sign in with OAuth, or send `Authorization: Bearer <APIFY_TOKEN>`):

```
https://mcp.apify.com?tools=wulfcare/google-trends-scraper,wulfcare/youtube-transcript-scraper,wulfcare/youtube-scraper,wulfcare/youtube-comments-scraper,wulfcare/google-jobs-scraper,wulfcare/google-hotels-scraper,wulfcare/google-flights-scraper,wulfcare/app-store-scraper,wulfcare/google-play-scraper,wulfcare/chatgpt-search-scraper,wulfcare/gemini-search-scraper,wulfcare/google-ai-mode-scraper
```

Local (`claude_desktop_config.json`, `.cursor/mcp.json`, ...):

```json
{
  "mcpServers": {
    "wulfcare": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server", "--tools",
               "wulfcare/google-trends-scraper,wulfcare/youtube-transcript-scraper,wulfcare/youtube-scraper,wulfcare/youtube-comments-scraper,wulfcare/google-jobs-scraper,wulfcare/google-hotels-scraper,wulfcare/google-flights-scraper,wulfcare/app-store-scraper,wulfcare/google-play-scraper,wulfcare/chatgpt-search-scraper,wulfcare/gemini-search-scraper,wulfcare/google-ai-mode-scraper"],
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
