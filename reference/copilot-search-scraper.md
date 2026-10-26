# Microsoft Copilot Search Scraper & AI Brand Visibility Tracker

`wulfcare/copilot-search-scraper`: Ask Microsoft Copilot Search (Bing) your prompts: get the full answer as markdown, every cited source with title and snippet, and a brand report: mentioned or not, rank vs competitors, own site cited. No login or API key.

**Use it for:**
- what Microsoft Copilot Search (Bing) answers to a prompt, with sources, and whether it mentions a brand

- Store page: https://apify.com/wulfcare/copilot-search-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~copilot-search-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/copilot-search-scraper`

**Price:**
- $0.008 per copilot answer (copilot-answer): One Microsoft Copilot answer to one prompt, with every source and the brand report. Prompts Copilot didn't answer are never charged.
- $0.008 per residential proxy (per answer) (residential-proxy-answer): Extra per answer only when it went through Apify's residential proxy (Bing refused the server's IP address, or you chose a country), to cover its bandwidth.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~copilot-search-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/copilot-search-scraper").call(run_input={"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `prompts` | array | yes |  |  | Prompts: What to ask Copilot, one prompt per line. Write them the way your customers would ask, e.g. "best accounting software for a plumber". Each prompt is asked in a new, logged-out Copilot Search. |
| `yourBrand` | string |  |  |  | Your brand: Optional. Your brand name, then any other names and your website, separated by commas: "HubSpot, HubSpot CRM, hubspot.com". Every answer then says whether it mentions you, your rank against the competitors below, and whether it cites your site. |
| `competitors` | array |  |  |  | Competitors: Optional. Other brands to track, one per line, in the same format: name, other names, website. |
| `repeats` | integer |  | 1 | 1–10 | Ask each prompt this many times: Copilot words its answer differently each time, and the brands it names can change too. Ask the same prompt 3-5 times to get your share of mentions instead of a single snapshot. Every answer is its own row (and its own charge). |
| `maxConcurrency` | integer |  | 3 | 1–8 | Prompts at a time: How many questions run in parallel (each is a browser tab). 3 is a safe default. |
| `language` | string |  | "en" |  | Language: Interface language code, e.g. en, de, fr, es, ja (default en). Copilot usually answers in the language of the prompt anyway. |
| `useResidentialProxy` | boolean |  | false |  | Always use residential proxy: Off (recommended): questions go out from the Apify server's own IP address (in the US), and the run switches to Apify residential proxy by itself only if Bing starts asking for captchas. Turn on to ask from a home IP in the country below, e.g. to see what Copilot tells people in that country. Answers through residential proxy cost an extra residential-proxy-answer event (it covers the bandwidth). |
| `proxyCountry` | string |  | "US" | `US` (United States), `GB` (United Kingdom), `CA` (Canada), `AU` (Australia), `DE` (Germany), `FR` (France), `ES` (Spain), `IT` (Italy), `NL` (Netherlands), `IN` (India), `JP` (Japan), `BR` (Brazil), `MX` (Mexico) | Residential proxy country: Where residential-proxy questions come from. Copilot tailors local answers (shops, prices, places) to it. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "prompt": "What is the best CRM for a small business?",
  "repeat": 1,
  "answer": "The **best overall CRM for most small businesses is HubSpot CRM**, thanks to its intuitive interface, strong automation, and all‑in‑one sales/marketing tools [2].\n\n**If you want the simplest setup:** Bigin by Zoho CRM\n**If you want visual p…",
  "answerText": "The best overall CRM for most small businesses is HubSpot CRM, thanks to its intuitive interface, strong automation, and all‑in‑one sales/marketing tools.\n\nIf you want the simplest setup: Bigin by Zoho CRM\nIf you want visual pipelines: mond…",
  "sources": [
    {
      "title": "10 Best Small Business CRM Software Of 2026 - Forbes",
      "url": "https://www.forbes.com/advisor/business/software/best-crm-small-business/",
      "domain": "forbes.com",
      "siteName": "Forbes",
      "citedInline": true,
      "number": 1,
      "snippet": "To find the best small business CRMs, we evaluated 41 providers and ranked 33 features and tools that have the biggest impact on SMBs."
    },
    {
      "title": "12 Best Small Business CRM Tools",
      "url": "https://fitsmallbusiness.com/best-crm-for-small-business/",
      "domain": "fitsmallbusiness.com",
      "siteName": "Fit Small Business",
      "citedInline": true,
      "number": 2,
      "snippet": "Compare the 12 best CRM tools for small business. Our 2026 top picks are HubSpot CRM, Bigin by Zoho CRM, and monday CRM to drive sales and growth."
    }
  ],
  "sourceCount": 2,
  "citedDomains": [
    "forbes.com",
    "fitsmallbusiness.com"
  ],
  "yourBrand": "HubSpot",
  "yourBrandMentioned": true,
  "yourBrandRank": 1,
  "yourBrandCited": false,
  "brandsMentioned": [
    "HubSpot",
    "Pipedrive"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 4,
      "rank": 1,
      "firstMention": "The best overall CRM for most small businesses is HubSpot CRM, thanks to its intuitive interface, strong automation, and all‑in‑one sales/marketing tools.",
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
      "brand": "Pipedrive",
      "mentioned": true,
      "mentions": 3,
      "rank": 2,
      "firstMention": "If you want deep email marketing: Pipedrive",
      "cited": false,
      "citedUrls": []
    }
  ],
  "language": "en",
  "proxy": "residential-US",
  "askedAt": "2026-10-25T09:53:11Z",
  "seconds": 21,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
