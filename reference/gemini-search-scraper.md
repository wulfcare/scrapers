# Gemini Search Scraper & AI Brand Visibility Tracker ($1/1k)

`wulfcare/gemini-search-scraper`: Ask Google Gemini your prompts: get the full answer (tables and steps included), every cited source, products with prices, and a brand report: mentioned or not, rank vs competitors, own site cited. No login, API key or browser. $1 per 1,000 answers, the lowest Gemini price on Apify.

**Use it for:**
- what Google Gemini answers to a prompt, with sources, and whether it mentions a brand

- Store page: https://apify.com/wulfcare/gemini-search-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~gemini-search-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/gemini-search-scraper`

**Price:**
- $0.001 per gemini answer (gemini-answer): One Gemini answer to one prompt, with every source, products and the brand report. Prompts Gemini didn't answer are never charged.
- $0.002 per residential proxy (per answer) (residential-proxy-answer): Extra per answer only when you turn on Apify Proxy with the Residential group, to cover its bandwidth.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~gemini-search-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/gemini-search-scraper").call(run_input={"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `prompts` | array | yes |  |  | Prompts: What to ask Gemini, one prompt per line. Write them the way your customers would ask, e.g. "best accounting software for a plumber". Each prompt is asked in a new, logged-out Gemini chat. |
| `yourBrand` | string |  |  |  | Your brand: Optional. Your brand name, then any other names and your website, separated by commas: "HubSpot, HubSpot CRM, hubspot.com". Every answer then says whether it mentions you, your rank against the competitors below, and whether it cites your site. |
| `competitors` | array |  |  |  | Competitors: Optional. Other brands to track, one per line, in the same format: name, other names, website. |
| `repeats` | integer |  | 1 | 1–10 | Ask each prompt this many times: Gemini words its answer differently each time, and the brands it names can change too. Ask the same prompt 3-5 times to get your share of mentions instead of a single snapshot. Every answer is its own row (and its own charge). |
| `maxConcurrency` | integer |  | 4 | 1–10 | Prompts at a time: How many questions run in parallel. 4 is a safe default; up to 10 is faster. |
| `language` | string |  | "en" |  | Language: Interface language code, e.g. en, de, fr, es, ja (default en). Gemini usually answers in the language of the prompt anyway. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "prompt": "Which project management tool is best for a remote team?",
  "repeat": 1,
  "answer": "The \"best\" project management tool for a remote team depends entirely on your team's workflow, technical level, and how much you rely on asynchronous communication. Because remote teams cannot tap shoulders to check on progress, the ideal t…",
  "answerText": "The \"best\" project management tool for a remote team depends entirely on your team's workflow, technical level, and how much you rely on asynchronous communication. Because remote teams cannot tap shoulders to check on progress, the ideal t…",
  "sources": [
    {
      "title": "7 Best Project Management Tools for Remote Teams (2026)",
      "url": "https://kova-digital.com/work/project-management-tools",
      "domain": "kova-digital.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": "Best project management tools and software: My 21 top picks for 2026",
      "url": "https://www.wrike.com/project-management-guide/faq/what-are-project-management-tools/",
      "domain": "wrike.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": "Best project management software for 2026? : r/projectmanagers",
      "url": "https://www.reddit.com/r/projectmanagers/comments/1q4ndn0/best_project_management_software_for_2026/",
      "domain": "reddit.com",
      "siteName": null,
      "citedInline": true
    },
    "… 3 more"
  ],
  "sourceCount": 6,
  "citedDomains": [
    "kova-digital.com",
    "wrike.com",
    "reddit.com",
    "… 3 more"
  ],
  "products": [],
  "yourBrand": "HubSpot",
  "yourBrandMentioned": false,
  "yourBrandRank": null,
  "yourBrandCited": false,
  "brandsMentioned": [
    "monday.com"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Salesforce",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Zoho CRM",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    },
    "… 2 more"
  ],
  "language": "en",
  "askedAt": "2026-11-17T21:05:22Z",
  "seconds": 16.4,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
