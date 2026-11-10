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
  "prompt": "best budget wireless earbuds 2026",
  "repeat": 1,
  "answer": "The **Anker Soundcore Space A40** are the strongest all‑around budget earbuds in 2026 thanks to excellent ANC, customizable sound, long battery life, and consistently top-tier value.\n\n### ✅ Quick Answer (Top Picks)\n**Best overall:** **Anker…",
  "answerText": "The Anker Soundcore Space A40 are the strongest all‑around budget earbuds in 2026 thanks to excellent ANC, customizable sound, long battery life, and consistently top-tier value.\n\n✅ Quick Answer (Top Picks)\nBest overall: Anker Soundcore Spa…",
  "sources": [
    {
      "title": "The 5 Best Budget Wireless Earbuds of 2026 - RTINGS.com",
      "url": "https://www.rtings.com/headphones/reviews/best/cheap-wireless-earbuds",
      "domain": "rtings.com",
      "siteName": "RTINGS.com",
      "citedInline": true,
      "number": 1,
      "snippet": "The Anker Soundcore Space A40 Truly Wireless are the best budget wireless earbuds we've tested. These great-value earbuds offer amazing ANC."
    },
    {
      "title": "Best Cheap Earbuds 2026: Great sound and value on a budget",
      "url": "https://www.trustedreviews.com/best/best-cheap-earbuds-4382625",
      "domain": "trustedreviews.com",
      "siteName": "Trusted Reviews",
      "citedInline": true,
      "number": 2,
      "snippet": "True wireless earbuds don’t need to cost an arm and a leg. We’ve compiled this list of the best cheap earbuds to help you find the right pair"
    },
    {
      "title": "Best Budget Wireless Earbuds: Top Picks Under $150 - Cybernews",
      "url": "https://cybernews.com/headphones/best-budget-wireless-earbuds/",
      "domain": "cybernews.com",
      "siteName": "Cybernews",
      "citedInline": true,
      "number": 3,
      "snippet": "Discover the best budget wireless earbuds on the market in 2026. Read my detailed reviews of the top choices, with great sound, features, and value, all under $150."
    }
  ],
  "sourceCount": 3,
  "citedDomains": [
    "rtings.com",
    "trustedreviews.com",
    "cybernews.com"
  ],
  "yourBrand": "Asana",
  "yourBrandMentioned": false,
  "yourBrandRank": null,
  "yourBrandCited": false,
  "brandsMentioned": [],
  "brands": [
    {
      "brand": "Asana",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Trello",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Monday.com",
      "mentioned": false,
      "mentions": 0,
      "rank": null,
      "firstMention": null,
      "cited": false,
      "citedUrls": []
    }
  ],
  "language": "en",
  "proxy": "none",
  "askedAt": "2026-11-08T13:04:11Z",
  "seconds": 1.8,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
