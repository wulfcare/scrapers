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
  "prompt": "What is the best CRM for a small business?",
  "repeat": 1,
  "answer": "Finding the \"best\" CRM for a small business depends entirely on your budget, team size, and whether your primary focus is sales pipelines, marketing, or customer support. \n\n---\n\n### 1. HubSpot CRM — Best for Beginners & Inbound Marketing\n* …",
  "answerText": "Finding the \"best\" CRM for a small business depends entirely on your budget, team size, and whether your primary focus is sales pipelines, marketing, or customer support.\n\n---\n\n1. HubSpot CRM — Best for Beginners & Inbound Marketing\n- Best …",
  "sources": [
    {
      "title": "The Best CRM for Small Business in 2026: An Honest Comparison",
      "url": "https://1crm.com/best-crm-for-small-business/",
      "domain": "1crm.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": "10 Best CRM Tools for Small Businesses in 2026 - Helpmonks",
      "url": "https://helpmonks.com/blog/best-crm-tools-small-businesses-2026/",
      "domain": "helpmonks.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": "Best small business CRM of 2026 - TechRadar",
      "url": "https://www.techradar.com/best/best-crm-for-small-business",
      "domain": "techradar.com",
      "siteName": null,
      "citedInline": true
    },
    "… 3 more"
  ],
  "sourceCount": 6,
  "citedDomains": [
    "1crm.com",
    "helpmonks.com",
    "techradar.com",
    "… 2 more"
  ],
  "products": [],
  "yourBrand": "HubSpot",
  "yourBrandMentioned": true,
  "yourBrandRank": 1,
  "yourBrandCited": false,
  "brandsMentioned": [
    "HubSpot",
    "Pipedrive",
    "Salesforce"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 4,
      "rank": 1,
      "firstMention": "HubSpot CRM — Best for Beginners & Inbound Marketing",
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Salesforce",
      "mentioned": true,
      "mentions": 4,
      "rank": 3,
      "firstMention": "The Catch: Advanced custom workflows and deep enterprise configurations are more limited than competitors like Salesforce or Zoho.",
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Pipedrive",
      "mentioned": true,
      "mentions": 3,
      "rank": 2,
      "firstMention": "Pipedrive — Best for Sales-Driven Teams",
      "cited": false,
      "citedUrls": []
    }
  ],
  "language": "en",
  "askedAt": "2026-10-25T09:52:20Z",
  "seconds": 12.2,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
