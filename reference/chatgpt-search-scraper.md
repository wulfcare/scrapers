# ChatGPT Search Scraper & AI Brand Visibility Tracker

`wulfcare/chatgpt-search-scraper`: Ask ChatGPT (with web search) your prompts for $0.05 per answer (Apify's own scraper: $0.20). Get the full answer, every cited source, every brand and product ChatGPT recommends (price, rating, reviews), its follow-up questions, and a free brand rank and citation report. No login.

**Use it for:**
- what ChatGPT (with web search) answers to a prompt, with cited sources and recommended products
- whether ChatGPT mentions / recommends / cites a brand vs competitors

- Store page: https://apify.com/wulfcare/chatgpt-search-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~chatgpt-search-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/chatgpt-search-scraper`

**Price:**
- $0.05 per chatgpt answer (answer): One ChatGPT answer to one prompt, with every cited source and the brand report. Prompts ChatGPT didn't answer are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~chatgpt-search-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/chatgpt-search-scraper").call(run_input={"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `prompts` | array | yes |  |  | Prompts: What to ask ChatGPT, one prompt per line. Write them the way your customers would ask, e.g. "best accounting software for a plumber". Each prompt is asked in a new, logged-out ChatGPT chat. |
| `yourBrand` | string |  |  |  | Your brand: Optional. Your brand name, then any other names and your website, separated by commas: "HubSpot, HubSpot CRM, hubspot.com". Every answer then says whether it mentions you, your rank against the competitors below, and whether it cites your site. |
| `competitors` | array |  |  |  | Competitors: Optional. Other brands to track, one per line, in the same format: name, other names, website. |
| `repeats` | integer |  | 1 | 1–10 | Ask each prompt this many times: ChatGPT words its answer differently each time, and the brands it names can change too. Ask the same prompt 3-5 times to get your share of mentions instead of a single snapshot. Every answer is its own row (and its own charge). |
| `webSearch` | boolean |  | true |  | Use web search: On (recommended): ChatGPT searches the web and cites sources, like it does for most product questions. Off: ChatGPT decides for itself whether to search. |
| `maxConcurrency` | integer |  | 2 | 1–4 | Prompts at a time: How many chats run in parallel. 2 is a safe default; 3-4 is faster but needs 4 GB of memory. |
| `language` | string |  |  |  | Browser language: Optional, e.g. en-GB, de-DE, fr-FR (default en-US). ChatGPT usually answers in the language of the prompt anyway. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "prompt": "What is the best CRM for a small business?",
  "repeat": 1,
  "yourBrand": "HubSpot",
  "yourBrandMentioned": true,
  "yourBrandRank": 1,
  "yourBrandCited": true,
  "brandsMentioned": [
    "HubSpot",
    "Zoho CRM"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 4,
      "rank": 1,
      "firstMention": "For most small businesses, I'd start with HubSpot, Zoho CRM, or Pipedrive.",
      "cited": true,
      "citedUrls": [
        "https://www.hubspot.com/products/crm",
        "https://www.hubspot.com/pricing"
      ]
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
      "mentioned": true,
      "mentions": 5,
      "rank": 2,
      "firstMention": "For most small businesses, I'd start with HubSpot, Zoho CRM, or Pipedrive.",
      "cited": true,
      "citedUrls": [
        "https://www.zoho.com/crm/",
        "https://www.zoho.com/crm/zohocrm-pricing.html"
      ]
    }
  ],
  "recommendedBrands": [
    {
      "rank": 1,
      "name": "HubSpot CRM",
      "category": "software",
      "description": "Customer relationship management software"
    },
    {
      "rank": 2,
      "name": "Zoho CRM",
      "category": "software",
      "description": "Customer relationship management software"
    },
    {
      "rank": 3,
      "name": "Pipedrive",
      "category": "software",
      "description": "Sales-focused CRM software"
    },
    "… 2 more"
  ],
  "productCount": 0,
  "products": [],
  "followUpQuestions": [
    {
      "question": "1. What kind of business do you run?",
      "options": [
        "Service business (consulting, agency, contractor, etc.)",
        "Professional services (accounting, legal, real estate, etc.)",
        "E-commerce or retail",
        "… 2 more"
      ]
    },
    {
      "question": "2. How many people will use the CRM?",
      "options": [
        "Just me",
        "2–5 people",
        "6–20 people",
        "… 1 more"
      ]
    },
    {
      "question": "3. What's your monthly budget?",
      "options": [
        "Free only",
        "Under $50/month",
        "$50–$150/month",
        "… 1 more"
      ]
    },
    "… 1 more"
  ],
  "answerText": "The best CRM for a small business depends on how you find customers, manage sales, and follow up with leads. For most small businesses, I'd start with HubSpot, Zoho CRM, or Pipedrive. They cover different needs, and the most expensive optio…",
  "answer": "The best CRM for a small business depends on how you find customers, manage sales, and follow up with leads. For most small businesses, I'd start with HubSpot, Zoho CRM, or Pipedrive. They cover different needs, and the most expensive optio…",
  "sources": [
    {
      "title": null,
      "url": "https://www.hubspot.com/products/crm",
      "domain": "hubspot.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": null,
      "url": "https://www.hubspot.com/pricing",
      "domain": "hubspot.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": null,
      "url": "https://www.zoho.com/crm/",
      "domain": "zoho.com",
      "siteName": null,
      "citedInline": true
    },
    "… 6 more"
  ],
  "sourceCount": 9,
  "citedDomains": [
    "hubspot.com",
    "zoho.com",
    "pipedrive.com",
    "… 2 more"
  ],
  "webSearch": true,
  "location": "US",
  "askedAt": "2026-10-25T22:50:55Z",
  "seconds": 29.2,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
