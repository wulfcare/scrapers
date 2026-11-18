# AI Visibility Tracker: ChatGPT, Gemini & Google AI Overviews

`wulfcare/ai-visibility-tracker`: See whether ChatGPT, Gemini and Google AI Overviews recommend your brand or your competitors. Get a visibility score, share of voice, the prompts you're missing from, the sites AI cites, and a white-label HTML report. $0.04 per answer, report free. No API keys.

**Use it for:**
- AI visibility / share of voice of a brand across ChatGPT, Gemini and Google AI Overviews in one run, with HTML report

- Store page: https://apify.com/wulfcare/ai-visibility-tracker
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~ai-visibility-tracker/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/ai-visibility-tracker`

**Price:**
- $0.04 per ai answer (ai-answer): One answer from one AI engine (ChatGPT, Gemini or Google AI Overview) to one prompt, with its brand analysis. Searches with no AI Overview, failed prompts and the report are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~ai-visibility-tracker/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"yourBrand": "Pipedrive, pipedrive.com", "competitors": ["HubSpot, hubspot.com", "Salesforce, salesforce.com"], "category": "CRM for small business", "promptCount": 5}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/ai-visibility-tracker").call(run_input={"yourBrand": "Pipedrive, pipedrive.com", "competitors": ["HubSpot, hubspot.com", "Salesforce, salesforce.com"], "category": "CRM for small business", "promptCount": 5})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `yourBrand` | string |  |  |  | Your brand: Your brand name, then any other names and your website, separated by commas: "Pipedrive, Pipedrive CRM, pipedrive.com". The report scores how often and how high AI recommends you, and whether it cites your site. Leave empty to just see who AI recommends. |
| `competitors` | array |  |  |  | Competitors: The brands you compete with, one per line, in the same format: name, other names, website. Their scores and share of voice sit next to yours in the report. |
| `category` | string |  |  |  | Category (writes the prompts for you): What you sell, the way a customer would put it: "CRM for small business", "dentist in Brisbane", "running shoes for flat feet". The Actor writes the buyer questions people ask AI ("What is the best ...?", "Which ... would you recommend?", "alternatives to "). Use it, your own prompts below, or both. |
| `promptCount` | integer |  | 10 | 1–50 | Number of prompts to write: How many questions to write from the category (1-50). Each is asked once on every engine you pick. |
| `prompts` | array |  |  |  | Your own prompts: Optional. Exact questions to ask, one per line, e.g. "best CRM for a real estate agency". Prompts that name a tracked brand ("Is HubSpot good?") are answered and shown, but left out of the scores, since they name the brand whatever its visibility. |
| `engines` | array |  | ["chatgpt", "gemini", "google_ai_overview"] |  | AI engines: Where to ask. Every engine is asked as a new, logged-out visitor, so you see what your customers see, not an API answer. |
| `country` | string |  | "US" | `US` (United States), `GB` (United Kingdom), `AU` (Australia), `CA` (Canada), `NZ` (New Zealand), `IE` (Ireland), `IN` (India), `SG` (Singapore), `ZA` (South Africa), `DE` (Germany), `FR` (France), `ES` (Spain), `IT` (Italy), `NL` (Netherlands), `SE` (Sweden), `PL` (Poland), `BR` (Brazil), `MX` (Mexico), `JP` (Japan), `AE` (United Arab Emirates) | Country: Where your customers are. Google AI Overviews are searched for this country. ChatGPT is asked through a residential IP address in this country when it isn't the US (this uses your Apify residential proxy). Gemini doesn't localise logged-out answers by country. |
| `language` | string |  | "en" |  | Language: Two-letter language code for Google and the browser (en, de, fr, es, ...). Write your prompts in the same language. |
| `repeats` | integer |  | 1 | 1–5 | Ask each prompt this many times: AI answers change between askings. Asking each prompt 2-3 times gives steadier scores. Every answer is its own row and its own charge. |
| `maxRunMinutes` | integer |  |  | 1–600 | Stop asking after (minutes): When time is up, no more prompts are asked and the report is written from the answers so far. Leave empty to ask everything. The run also stops in time before its own timeout. |
| `projectName` | string |  |  |  | Project name (tracks changes over time): Optional. Give the brand or client a name, e.g. "acme-weekly", and schedule this Actor (weekly is typical). Each run is saved under the name in your account, and the report shows the score trend and the prompts you gained or lost since the last run. |
| `reportTitle` | string |  |  |  | Report title: Optional. Heading of the HTML report (default: "AI Visibility Report: "). |
| `agencyName` | string |  |  |  | Prepared by (agency name): Optional. Shown on the HTML report as "Prepared by ...", for agencies sending it to clients. The report carries no Apify branding. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "prompt": "What is the best CRM for small business?",
  "engine": "google_ai_overview",
  "engineName": "Google AI Overview",
  "repeat": 1,
  "status": "answered",
  "brandedPrompt": false,
  "yourBrand": "Pipedrive",
  "yourBrandMentioned": true,
  "yourBrandRank": 2,
  "yourBrandCited": false,
  "brandsMentioned": [
    "HubSpot",
    "Pipedrive",
    "Zoho CRM",
    "… 1 more"
  ],
  "brands": [
    {
      "brand": "Pipedrive",
      "mentioned": true,
      "mentions": 1,
      "rank": 2,
      "firstMention": "Pipedrive: Best for sales-focused pipelines.",
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "HubSpot",
      "mentioned": true,
      "mentions": 1,
      "rank": 1,
      "firstMention": "HubSpot CRM: Best for all-in-one marketing and sales.",
      "cited": false,
      "citedUrls": []
    },
    {
      "brand": "Salesforce",
      "mentioned": true,
      "mentions": 1,
      "rank": 4,
      "firstMention": "Salesforce Starter: Best for growing businesses wanting enterprise DNA.",
      "cited": true,
      "citedUrls": [
        "https://www.salesforce.com/crm/crm-for-small-business/"
      ]
    },
    "… 2 more"
  ],
  "answerText": "The top customer relationship management (CRM) software for small businesses in 2026 varies depending on your primary goal, team size, and budget:\n\nTop Small Business CRMs\n\nHubSpot CRM: Best for all-in-one marketing and sales. Offers a popu…",
  "answer": "The top customer relationship management (CRM) software for small businesses in 2026 varies depending on your primary goal, team size, and budget:\n\nTop Small Business CRMs\n\nHubSpot CRM: Best for all-in-one marketing and sales. Offers a popu…",
  "sources": [
    {
      "title": "Best and inexpensive CRM for small business - Reddit",
      "url": "https://www.reddit.com/r/CRM/comments/1e5141p/best_and_inexpensive_crm_for_small_business/",
      "domain": "reddit.com",
      "siteName": "Reddit",
      "citedInline": true
    },
    {
      "title": "Best CRM for Small Businesses | Zoho CRM",
      "url": "https://www.zoho.com/crm/small-business-crm-software/",
      "domain": "zoho.com",
      "siteName": "Zoho",
      "citedInline": true
    },
    {
      "title": "CRM For Small Business (Your Complete Guide) - Salesforce",
      "url": "https://www.salesforce.com/crm/crm-for-small-business/",
      "domain": "salesforce.com",
      "siteName": "Salesforce",
      "citedInline": true
    },
    "… 3 more"
  ],
  "sourceCount": 6,
  "citedDomains": [
    "reddit.com",
    "zoho.com",
    "salesforce.com",
    "… 3 more"
  ],
  "country": "US",
  "askedAt": "2026-11-17T21:01:05Z",
  "seconds": 7.5,
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
