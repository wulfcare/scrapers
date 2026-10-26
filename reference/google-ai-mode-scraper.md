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
  "answer": "Finding the best CRM for a small business depends heavily on your team's specific goals, technical comfort level, and budget. Because there is no one-size-fits-all solution, small business CRMs generally fall into a few distinct categories—…",
  "answerText": "Finding the best CRM for a small business depends heavily on your team's specific goals, technical comfort level, and budget. Because there is no one-size-fits-all solution, small business CRMs generally fall into a few distinct categories—…",
  "sources": [
    {
      "title": "The Best Small Business CRM Software We've Tested for 2026 | PCMag",
      "url": "https://www.pcmag.com/picks/the-best-small-business-crm-software",
      "domain": "pcmag.com",
      "siteName": "PCMag",
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
    "pcmag.com",
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
    "Pipedrive"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 5,
      "rank": 1,
      "firstMention": "HubSpot CRM - Ease of Use & Growth - Smohest user interface; excellent free tier.",
      "cited": true,
      "citedUrls": [
        "https://www.hubspot.com/products/crm/ai-crm"
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
      "brand": "Pipedrive",
      "mentioned": true,
      "mentions": 3,
      "rank": 2,
      "firstMention": "Pipedrive - Sales-Focused Teams - Visual, intuitive deal pipelines that teams pick up instantly.",
      "cited": true,
      "citedUrls": [
        "https://www.pipedrive.com/"
      ]
    }
  ],
  "country": "US",
  "language": "en",
  "askedAt": "2026-10-25T09:57:02Z",
  "seconds": 7.3,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
