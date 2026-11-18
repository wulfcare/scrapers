# Bing Copilot Scraper: Answers, Citations & Brand Mentions

`wulfcare/bing-copilot-scraper`: Ask Bing Copilot (Microsoft Copilot Search) any prompts: the full answer as markdown, every cited source with title and snippet, and whether your brand is mentioned or cited. $3 per 1,000 answers ($10 when a residential proxy is needed), no start fee.

**Use it for:**
- what Bing Copilot answers to a prompt as markdown, with cited sources, and whether a brand is mentioned or cited

- Store page: https://apify.com/wulfcare/bing-copilot-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~bing-copilot-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/bing-copilot-scraper`

**Price:**
- $0.003 per copilot answer (copilot-answer): One Bing Copilot answer to one prompt, with every source and the brand report. Prompts Copilot didn't answer are never charged.
- $0.008 per residential proxy (per answer) (residential-proxy-answer): Extra per answer only when it went through Apify's residential proxy (Bing refused the server's IP address, or you chose a country), to cover its bandwidth.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~bing-copilot-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/bing-copilot-scraper").call(run_input={"prompts": ["What is the best CRM for a small business?"], "yourBrand": "HubSpot, hubspot.com", "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"]})
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
  "answer": "**For most small businesses, **HubSpot CRM** is the best starting point because its free plan covers core contact and deal management, while its broader platform can add marketing, service, and automation later. If your team is primarily sa…",
  "answerText": "For most small businesses, HubSpot CRM is the best starting point because its free plan covers core contact and deal management, while its broader platform can add marketing, service, and automation later. If your team is primarily sales-fo…",
  "sources": [
    {
      "title": "Customer Platform Pricing | HubSpot",
      "url": "https://www.hubspot.com/pricing/suite",
      "domain": "hubspot.com",
      "siteName": "HubSpot",
      "citedInline": true,
      "number": 1,
      "snippet": null
    },
    {
      "title": "HubSpot's Starter Plan for Startups & Small Businesses",
      "url": "https://www.hubspot.com/products/crm/starter",
      "domain": "hubspot.com",
      "siteName": "HubSpot",
      "citedInline": true,
      "number": 2,
      "snippet": null
    },
    {
      "title": "CRM Pricing Plans | Affordable CRM Software Costs | Pipedrive",
      "url": "https://www.pipedrive.com/en/pricing",
      "domain": "pipedrive.com",
      "siteName": "Pipedrive",
      "citedInline": true,
      "number": 3,
      "snippet": null
    },
    "… 2 more"
  ],
  "sourceCount": 5,
  "citedDomains": [
    "hubspot.com",
    "pipedrive.com",
    "zoho.com",
    "… 1 more"
  ],
  "yourBrand": "HubSpot",
  "yourBrandMentioned": true,
  "yourBrandRank": 1,
  "yourBrandCited": true,
  "brandsMentioned": [
    "HubSpot",
    "Pipedrive",
    "Zoho CRM"
  ],
  "brands": [
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 7,
      "rank": 1,
      "firstMention": "For most small businesses, HubSpot CRM is the best starting point because its free plan covers core contact and deal management, while its broader platform can add marketing, service, and automation later.",
      "cited": true,
      "citedUrls": [
        "https://www.hubspot.com/pricing/suite",
        "https://www.hubspot.com/products/crm/starter"
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
      "mentions": 6,
      "rank": 3,
      "firstMention": "If your team is primarily sales-focused, choose Pipedrive; if minimizing cost and maximizing customization matter most, choose Zoho CRM.",
      "cited": true,
      "citedUrls": [
        "https://www.zoho.com/en-us/crm/zohocrm-pricing.html"
      ]
    },
    "… 2 more"
  ],
  "language": "en",
  "proxy": "none",
  "askedAt": "2026-11-17T21:30:50Z",
  "seconds": 27.4,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
