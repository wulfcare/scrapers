# Google Trends Scraper: Unlimited Keywords + Daily Data

`wulfcare/google-trends-scraper`: Google Trends without its limits: compare up to 100 keywords on one 0-100 scale (Google stops at 5), and daily data for any range, even 5 years or 2004-now (Google gives weekly/monthly). Plus regions, related queries and Trending Now. Paced so runs finish.

**Use it for:**
- Google Trends interest over time, interest by region, related queries for keywords
- compare more than 5 keywords on one 0-100 scale (up to 100)
- daily Google Trends data for long ranges (12 months, 5 years, 2004-now)
- what is trending on Google right now in a country (Trending Now)
- replacement for pytrends when it fails with 429 TooManyRequestsError

- Store page: https://apify.com/wulfcare/google-trends-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-trends-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-trends-scraper`

**Price:**
- $0.003 per trends report (trends-report): One Explore report: interest over time, interest by region and related queries for up to 5 compared terms.
- $0.0005 per trending search (trending-item): One trending search from Trending Now, with volume, growth, related searches and category.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-trends-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["coffee, tea"], "geo": "US", "timeRange": "today 12-m"}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-trends-scraper").call(run_input={"searchTerms": ["coffee, tea"], "geo": "US", "timeRange": "today 12-m"})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `mode` | string |  | "explore" | `explore` (Explore: search terms (interest over time, by region, related queries)), `trendingNow` (Trending Now: what's trending in a country right now) | What to scrape: Explore gives interest over time, by region and related queries for your search terms. Trending Now lists every search trending in the countries you pick. |
| `searchTerms` | array |  |  |  | Search terms: One report per line. Compare terms by separating them with commas, e.g. coffee, tea. No 5-term limit: put up to 100 terms on one line and they all come back on one 0-100 scale (Google itself compares only 5; we chain overlapping groups, charged per Google query used). You can also paste a Google Trends explore URL, and its terms, country, time range and category are used as-is. |
| `geo` | string |  | "" |  | Country or region: ISO country code like US, AU, GB, or a region like US-CA. Leave empty for worldwide. |
| `timeRange` | string |  | "today 12-m" | `now 1-H` (Past hour), `now 4-H` (Past 4 hours), `now 1-d` (Past day), `now 7-d` (Past 7 days), `today 1-m` (Past 30 days), `today 3-m` (Past 90 days), `today 12-m` (Past 12 months), `today 5-y` (Past 5 years), `all` (2004 - present) | Time range: Period to analyse. Google picks the resolution: minutes for the past hour or 4 hours, hours for 7 days, days up to 90 days, weeks up to 5 years, and months since 2004. |
| `customTimeRange` | string |  |  |  | Custom time range (optional): Overrides the time range above. Format YYYY-MM-DD YYYY-MM-DD, e.g. 2024-01-01 2024-06-30. |
| `dailyData` | boolean |  | false |  | Daily data for any time range: Google only gives daily points for ranges under ~9 months, then weekly or monthly. Turn this on to get daily points for the whole range (12 months, 5 years, even 2004 to now): we fetch ~8-month daily windows and scale each one to Google's full-range series. Each window is one more Google query, charged as a report (5 years ≈ 10 reports). Up to 5 terms per line. |
| `category` | integer |  | 0 |  | Category ID: Google Trends category, e.g. 0 = all, 71 = Food & Drink, 7 = Finance. Default 0. |
| `searchProperty` | string |  | "" | `` (Web search), `images` (Image search), `news` (News search), `froogle` (Google Shopping), `youtube` (YouTube search) | Search type: Which Google search to measure: web (default), images, news, Google Shopping or YouTube. |
| `interestOverTime` | boolean |  | true |  | Interest over time: Relative search interest (0-100) over the chosen time range. |
| `interestByRegion` | boolean |  | true |  | Interest by region: Relative search interest (0-100) by country, region, city or US metro area. |
| `relatedQueries` | boolean |  | true |  | Related queries (top + rising): The top and rising searches related to each term, including "Breakout" queries (growth over 5,000%). |
| `regionResolution` | string |  | "" | `` (Google default), `COUNTRY` (Countries), `REGION` (Regions / states), `CITY` (Cities), `DMA` (US metro areas (DMA)) | Region resolution: Level of detail for interest by region. "Google default" uses countries for worldwide and regions within a country. |
| `includeLowVolumeRegions` | boolean |  | false |  | Include low search volume regions: Include regions with too little search volume for Google to rate reliably (they usually show 0). |
| `saveCsv` | boolean |  | true |  | Also save spreadsheet-friendly CSVs: Saves interest_over_time.csv, interest_by_region.csv and related_queries.csv (one row per value) to the run's key-value store for Excel or Google Sheets. Free. |
| `trendingGeos` | array |  |  |  | Countries or regions: ISO codes like US, GB, AU, or regions like US-CA. One set of trends per entry. |
| `trendingHours` | string |  | "24" | `4` (Past 4 hours), `24` (Past 24 hours), `48` (Past 48 hours), `168` (Past 7 days) | Time window: How far back to look for trending searches. |
| `trendingCategories` | array |  |  |  | Only these categories (optional): Leave empty for all categories. |
| `trendingActiveOnly` | boolean |  | false |  | Only trends that are still active: Skip trends that have already ended. |
| `maxTrendsPerGeo` | integer |  | 0 | 0– | Max trends per country (0 = all): Trends are sorted by search volume, highest first. |
| `language` | string |  | "en-US" |  | Interface language: Language of Google's labels and related queries, e.g. en-US, en-GB, de, ja. |
| `timezoneOffsetMinutes` | integer |  | 0 |  | Timezone offset (minutes): Google's tz parameter: minutes WEST of UTC (Sydney = -600, New York = 300). |
| `maxConcurrency` | integer |  | 3 | 1–10 | Parallel reports: How many reports run at once, each on its own IP. Only applies when using a proxy. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "searchTerms": [
    "coffee",
    "tea"
  ],
  "geo": "US",
  "timeRange": "today 12-m",
  "category": 0,
  "property": "web",
  "trendsUrl": "https://trends.google.com/trends/explore?q=coffee%2Ctea&date=today+12-m&hl=en-US&geo=US",
  "interestOverTime": [
    {
      "date": "2025-11-02T00:00:00+00:00",
      "label": "Nov 2 – 8, 2025",
      "values": {
        "coffee": 65,
        "tea": 32
      },
      "isPartial": false
    },
    {
      "date": "2025-11-09T00:00:00+00:00",
      "label": "Nov 9 – 15, 2025",
      "values": {
        "coffee": 73,
        "tea": 34
      },
      "isPartial": false
    },
    {
      "date": "2025-11-16T00:00:00+00:00",
      "label": "Nov 16 – 22, 2025",
      "values": {
        "coffee": 71,
        "tea": 35
      },
      "isPartial": false
    },
    "… 50 more"
  ],
  "averages": {
    "coffee": 77,
    "tea": 37
  },
  "interestByRegion": [
    {
      "geoCode": "US-WY",
      "geoName": "Wyoming",
      "values": {
        "coffee": 69,
        "tea": 31
      },
      "hasData": true
    },
    {
      "geoCode": "US-HI",
      "geoName": "Hawaii",
      "values": {
        "coffee": 70,
        "tea": 30
      },
      "hasData": true
    },
    {
      "geoCode": "US-KS",
      "geoName": "Kansas",
      "values": {
        "coffee": 69,
        "tea": 31
      },
      "hasData": true
    },
    "… 48 more"
  ],
  "relatedQueries": {
    "coffee": {
      "top": [
        {
          "query": "coffee near me",
          "value": 100,
          "formattedValue": "100",
          "link": "https://trends.google.com/trends/explore?q=coffee+near+me&date=today+12-m&geo=US"
        },
        {
          "query": "coffee shop",
          "value": 85,
          "formattedValue": "85",
          "link": "https://trends.google.com/trends/explore?q=coffee+shop&date=today+12-m&geo=US"
        },
        {
          "query": "coffee maker",
          "value": 81,
          "formattedValue": "81",
          "link": "https://trends.google.com/trends/explore?q=coffee+maker&date=today+12-m&geo=US"
        },
        "… 22 more"
      ],
      "rising": [
        {
          "query": "home workout routines",
          "value": 6200,
          "formattedValue": "Breakout",
          "link": "https://trends.google.com/trends/explore?q=home+workout+routines&date=today+12-m&geo=US",
          "isBreakout": true
        },
        {
          "query": "sports scores today",
          "value": 6000,
          "formattedValue": "Breakout",
          "link": "https://trends.google.com/trends/explore?q=sports+scores+today&date=today+12-m&geo=US",
          "isBreakout": true
        },
        {
          "query": "top songs this week",
          "value": 5950,
          "formattedValue": "Breakout",
          "link": "https://trends.google.com/trends/explore?q=top+songs+this+week&date=today+12-m&geo=US",
          "isBreakout": true
        },
        "… 22 more"
      ]
    },
    "tea": {
      "top": [
        {
          "query": "green tea",
          "value": 100,
          "formattedValue": "100",
          "link": "https://trends.google.com/trends/explore?q=green+tea&date=today+12-m&geo=US"
        },
        {
          "query": "black tea",
          "value": 43,
          "formattedValue": "43",
          "link": "https://trends.google.com/trends/explore?q=black+tea&date=today+12-m&geo=US"
        },
        {
          "query": "coffee",
          "value": 41,
          "formattedValue": "41",
          "link": "https://trends.google.com/trends/explore?q=coffee&date=today+12-m&geo=US"
        },
        "… 22 more"
      ],
      "rising": [
        {
          "query": "loaded tea shop",
          "value": 2100,
          "formattedValue": "+2,100%",
          "link": "https://trends.google.com/trends/explore?q=loaded+tea+shop&date=today+12-m&geo=US",
          "isBreakout": false
        },
        {
          "query": "how to make cold brew tea",
          "value": 2000,
          "formattedValue": "+2,000%",
          "link": "https://trends.google.com/trends/explore?q=how+to+make+cold+brew+tea&date=today+12-m&geo=US",
          "isBreakout": false
        },
        {
          "query": "the loaded tea shop",
          "value": 1900,
          "formattedValue": "+1,900%",
          "link": "https://trends.google.com/trends/explore?q=the+loaded+tea+shop&date=today+12-m&geo=US",
          "isBreakout": false
        },
        "… 22 more"
      ]
    }
  },
  "scrapedAt": "2026-11-04T08:10:15+00:00"
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
