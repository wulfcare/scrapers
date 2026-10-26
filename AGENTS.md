# Instructions for AI agents

You can get the data below by calling one HTTP endpoint. No browser, scraping code or proxies are needed: each scraper is a hosted Apify Actor that takes JSON input and returns JSON items.

## 1. Pick the Actor

| The user wants | Actor | Minimal input |
|---|---|---|
| Google Trends: interest over time, by region, related queries | `wulfcare/google-trends-scraper` | `{"searchTerms": ["coffee, tea"], "geo": "US", "timeRange": "today 12-m"}` |
| Compare **more than 5** keywords in Google Trends | `wulfcare/google-trends-scraper` | `{"searchTerms": ["kw1, kw2, kw3, kw4, kw5, kw6, kw7"]}` (all on ONE line, comma-separated, up to 100) |
| **Daily** Google Trends data over a long range | `wulfcare/google-trends-scraper` | `{"searchTerms": ["bitcoin"], "timeRange": "today 5-y", "dailyData": true}` |
| What's trending on Google now | `wulfcare/google-trends-scraper` | `{"mode": "trendingNow", "trendingGeos": ["US"], "trendingHours": "24"}` |
| A YouTube video's transcript / captions / subtitles | `wulfcare/youtube-transcript-scraper` | `{"urls": ["https://www.youtube.com/watch?v=VIDEO_ID"], "languages": ["en"]}` |
| Transcripts of a whole channel or playlist | `wulfcare/youtube-transcript-scraper` | `{"urls": ["https://www.youtube.com/@handle"], "maxVideosPerSource": 50}` |
| YouTube videos / search results / channel stats (views, likes, dates) | `wulfcare/youtube-scraper` | `{"searchQueries": ["topic"], "maxResults": 20}` |
| Job listings with salary and apply links | `wulfcare/google-jobs-scraper` | `{"queries": ["data analyst jobs london"], "country": "GB"}` |
| Hotel prices across booking sites | `wulfcare/google-hotels-scraper` | `{"hotels": ["Hotel name, City"], "checkInDate": "2026-12-10", "nights": 2}` |
| Hotels in a city | `wulfcare/google-hotels-scraper` | `{"searchQueries": ["hotels in Paris"], "maxHotels": 20}` |
| App Store reviews (any number, any country) | `wulfcare/app-store-reviews-scraper` | `{"appIds": ["324684580"], "countries": ["us"], "maxReviewsPerApp": 1000}` |
| App Store app details, search, top charts | `wulfcare/app-store-scraper` | `{"mode": "apps", "appIds": ["324684580"]}` / `{"mode": "search", "searchQueries": ["budget"]}` / `{"mode": "charts"}` |
| Google Play reviews | `wulfcare/google-play-reviews-scraper` | `{"appIds": ["com.spotify.music"], "maxReviewsPerApp": 1000}` |
| Google Play app details (data safety, installs), search, charts | `wulfcare/google-play-scraper` | `{"mode": "apps", "appIds": ["com.spotify.music"]}` |
| What ChatGPT answers / recommends for a prompt | `wulfcare/chatgpt-search-scraper` | `{"prompts": ["best CRM for a small business?"]}` |
| What Gemini answers | `wulfcare/gemini-search-scraper` | `{"prompts": ["..."]}` |
| What Google AI Mode answers | `wulfcare/google-ai-mode-scraper` | `{"prompts": ["..."]}` |
| What Microsoft Copilot answers | `wulfcare/copilot-search-scraper` | `{"prompts": ["..."]}` |
| Is a brand mentioned by AI assistants, vs competitors | any of the 4 above, or `wulfcare/ai-visibility-tracker` for all engines at once | add `"yourBrand": "Name, site.com", "competitors": ["Other, other.com"]` |
| AI training / data annotation job listings | `wulfcare/ai-training-jobs-scraper` | `{"keywords": ["python"]}` |

Every field, type, default and allowed value: [`reference/<actor-name>.md`](reference), [`catalog.json`](catalog.json) (machine-readable) or the Actor's OpenAPI spec at `https://api.apify.com/v2/acts/wulfcare~<actor-name>/builds/default/openapi.json`.

## 2. Call it

Needs an Apify API token (`APIFY_TOKEN`; free account at https://console.apify.com/sign-up, $5 free credit each month). Note the `~` between owner and name in URLs.

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-trends-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN&maxTotalChargeUsd=0.50" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["coffee, tea"], "geo": "US"}'
```

The response is a JSON array of items.

- **Cap spend** with `maxTotalChargeUsd=<dollars>` on the URL. The run stops cleanly at the cap and keeps what it got.
- **CSV instead of JSON**: add `&format=csv`. **Only some fields**: `&fields=title,salary,applyUrl`.
- **Long jobs** (the sync endpoint waits at most 300 s): `POST https://api.apify.com/v2/acts/wulfcare~<name>/runs?token=...` with the same body, poll `GET https://api.apify.com/v2/actor-runs/<runId>?token=...` until `status` is `SUCCEEDED`, then `GET https://api.apify.com/v2/datasets/<defaultDatasetId>/items?token=...`.
- With an MCP client connected to `https://mcp.apify.com?tools=wulfcare/<name>`, the Actor is a tool: call it with the same input object.

## 3. Read the result

- One item per result (report, transcript, video, job, price, review, answer).
- An item with an `error` field is a failed input (app not found, no captions, no data). It is **not charged**; tell the user what the error says.
- Google Trends values are relative (0–100), not search counts. For more than 5 keywords, use `ranking` (`vsTop` = share of the top keyword). Interest by region and related queries are only returned for up to 5 keywords per line. Combined comparisons and daily data are estimates built from several Google queries; terms flagged `lowPrecision` or `tooSmallToMeasure` are less reliable.
- AI-search answers are what the engine said at run time; they vary between runs (use `repeats` for several samples).

## 4. Cost (per result, failures free)

Google Trends $0.003/report (more than 5 keywords or daily data: one report per Google query needed, e.g. 12 keywords ≈ 6) · YouTube transcripts $0.003 · YouTube videos free · Google Jobs $0.004/job · Google Hotels $0.0008/price · App Store / Google Play reviews $0.0001 · app details $0.0005 · ChatGPT $0.05/answer · Gemini $0.001 · AI Mode $0.0045 · Copilot $0.008 (+$0.008 with residential proxy) · AI Visibility $0.04/answer · AI training jobs free.

## Rules

- Public data only, collected as a logged-out visitor. Don't ask these Actors for private or logged-in content.
- Results can contain errors; for decisions that matter, tell the user to verify.
