# Google AI Mode Scraper & AI Brand Visibility Tracker

`wulfcare/google-ai-mode-scraper`: Ask Google AI Mode your prompts: get the full answer (tables included), every cited source, and a brand report: mentioned or not, rank vs competitors, own site cited. Any country. No login, API key or proxy needed.

**Use it for:**
- what Google AI Mode answers to a prompt, with sources, and whether it mentions a brand

- Store page: https://apify.com/wulfcare/google-ai-mode-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-ai-mode-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-ai-mode-scraper`

**Price:**
- $0.0045 per ai mode answer (ai-mode-answer): One Google AI Mode answer to one prompt, with every source and the brand report. Prompts AI Mode didn't answer are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-ai-mode-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-ai-mode-scraper").call(run_input={"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `prompts` | array | yes |  |  | Prompts: What to ask Google AI Mode, one prompt per line. Write them the way your customers would search, e.g. "best accounting software for a plumber". Each prompt is asked in a new, logged-out AI Mode search. |
| `yourBrand` | string |  |  |  | Your brand: Optional. Your brand name, then any other names and your website, separated by commas: "HubSpot, HubSpot CRM, hubspot.com". Every answer then says whether it mentions you, your rank against the competitors below, and whether it cites your site. |
| `competitors` | array |  |  |  | Competitors: Optional. Other brands to track, one per line, in the same format: name, other names, website. |
| `repeats` | integer |  | 1 | 1–10 | Ask each prompt this many times: AI Mode words its answer differently each time, and the brands it names can change too. Ask the same prompt 3-5 times to get your share of mentions instead of a single snapshot. Every answer is its own row (and its own charge). |
| `maxConcurrency` | integer |  | 2 | 1–5 | Prompts at a time: How many questions run in parallel (each is a browser tab). 2 is the safe default: Google slows down busy IP addresses. |
| `language` | string |  | "en" |  | Language: Google interface language (hl), e.g. en, de, fr, es, ja. Default en. |
| `country` | string |  | "US" | `US` (United States), `GB` (United Kingdom), `CA` (Canada), `AU` (Australia), `NZ` (New Zealand), `IE` (Ireland), `IN` (India), `DE` (Germany), `FR` (France), `ES` (Spain), `IT` (Italy), `NL` (Netherlands), `JP` (Japan), `BR` (Brazil), `MX` (Mexico), `SG` (Singapore), `ZA` (South Africa) | Country: Google country (gl) for the search. AI Mode leans on that country's sites and shops for local questions. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "prompt": "What is the best CRM for a small business?",
  "repeat": 1,
  "answer": "The best CRM for a small business depends on your primary goal, though HubSpot, Pipedrive, Zoho CRM, and Freshsales consistently rank as the top overall choices for affordability and ease of use. While HubSpot leads for all-in-one marketing…",
  "answerText": "The best CRM for a small business depends on your primary goal, though HubSpot, Pipedrive, Zoho CRM, and Freshsales consistently rank as the top overall choices for affordability and ease of use. While HubSpot leads for all-in-one marketing…",
  "sources": [
    {
      "title": "Best and inexpensive CRM for small business - Reddit",
      "url": "https://www.reddit.com/r/CRM/comments/1e5141p/best_and_inexpensive_crm_for_small_business/",
      "domain": "reddit.com",
      "siteName": "Reddit",
      "citedInline": true
    },
    {
      "title": null,
      "url": "https://www.hubspot.com/products/crm/ai-crm",
      "domain": "hubspot.com",
      "siteName": null,
      "citedInline": true
    },
    {
      "title": "The Best CRM Software for Small Businesses",
      "url": "https://www.zoho.com/crm/small-business-crm-software/",
      "domain": "zoho.com",
      "siteName": "Zoho",
      "citedInline": true
    },
    "… 9 more"
  ],
  "sourceCount": 12,
  "citedDomains": [
    "reddit.com",
    "hubspot.com",
    "zoho.com",
    "… 9 more"
  ],
  "yourBrand": "HubSpot",
  "yourBrandMentioned": true,
  "yourBrandRank": 1,
  "yourBrandCited": true,
  "brandsMentioned": [
    "HubSpot",
    "Pipedrive",
    "Zoho CRM",
    "… 1 more"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 5,
      "rank": 1,
      "firstMention": "The best CRM for a small business depends on your primary goal, though HubSpot, Pipedrive, Zoho CRM, and Freshsales consistently rank as the top overall choices for affordability and ease of use.",
      "cited": true,
      "citedUrls": [
        "https://www.hubspot.com/products/crm/ai-crm"
      ]
    },
    {
      "brand": "Salesforce",
      "mentioned": true,
      "mentions": 1,
      "rank": 4,
      "firstMention": "Salesforce Starter - Rapidly scaling teams - $25/user/month - No (Free trial) - Enterprise-grade scalability and deep reporting",
      "cited": true,
      "citedUrls": [
        "https://www.salesforce.com/crm/crm-for-small-business/"
      ]
    },
    {
      "brand": "Zoho CRM",
      "mentioned": true,
      "mentions": 3,
      "rank": 3,
      "firstMention": "The best CRM for a small business depends on your primary goal, though HubSpot, Pipedrive, Zoho CRM, and Freshsales consistently rank as the top overall choices for affordability and ease of use.",
      "cited": true,
      "citedUrls": [
        "https://www.zoho.com/crm/small-business-crm-software/"
      ]
    },
    "… 2 more"
  ],
  "country": "US",
  "language": "en",
  "askedAt": "2026-11-17T21:15:33Z",
  "seconds": 7,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
