# Google Jobs Scraper: Salaries, Descriptions & Apply Links

`wulfcare/google-jobs-scraper`: Scrape Google Jobs: title, company, location, salary, job type, posted date, full description, highlights and every real apply link (LinkedIn, Indeed, company site...). Up to 200 unique jobs per search, 27 countries.

**Use it for:**
- job listings from Google Jobs (Google for Jobs) with salary, description and apply links

- Store page: https://apify.com/wulfcare/google-jobs-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~google-jobs-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/google-jobs-scraper`

**Price:**
- $0.004 per job posting (google-job): One unique Google Jobs posting with title, company, location, salary, type, description, highlights and apply links. Duplicates are never charged.

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~google-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries": ["data analyst jobs london"], "country": "GB", "maxJobsPerQuery": 30}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/google-jobs-scraper").call(run_input={"queries": ["data analyst jobs london"], "country": "GB", "maxJobsPerQuery": 30})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `queries` | array | yes |  |  | Searches: What you'd type into Google, one per line, e.g. data analyst jobs london or remote python developer. Include the place in the search. |
| `country` | string |  | "US" | `US` (United States), `GB` (United Kingdom), `IE` (Ireland), `CA` (Canada), `DE` (Germany), `AT` (Austria), `CH` (Switzerland), `FR` (France), `BE` (Belgium), `NL` (Netherlands), `ES` (Spain), `PT` (Portugal), `IT` (Italy), `PL` (Poland), `SE` (Sweden), `NO` (Norway), `DK` (Denmark), `FI` (Finland), `IN` (India), `SG` (Singapore), `AE` (United Arab Emirates), `ZA` (South Africa), `BR` (Brazil), `MX` (Mexico), `JP` (Japan), `AU` (Australia (limited)), `NZ` (New Zealand (limited)) | Country: Which country's Google to search. Google Jobs isn't offered for every country; Australia and New Zealand usually return no jobs view. |
| `maxJobsPerQuery` | integer |  | 30 | 1–200 | Max jobs per search: Unique jobs to return per search. Google shows 10 at a time, so more than 10 needs 'Expand results'. |
| `expandResults` | boolean |  | true |  | Expand results: Google only shows 10 jobs per search. This runs natural variations (full time, senior, posted this week, remote...) and removes duplicates, for typically 40-80 unique jobs per search. You're only charged for unique jobs. |
| `includeDescription` | boolean |  | true |  | Include full job description: The full posting text. Turn off for smaller, faster output. |
| `language` | string |  | "en" |  | Language: Google interface language, e.g. en, de, fr, es. |
| `maxConcurrency` | integer |  | 3 | 1–10 | Parallel searches: How many Google searches run at once. |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "query": "nurse jobs new york",
  "searchUsed": "nurse jobs new york",
  "country": "US",
  "position": 1,
  "title": "Registered Nurse / RN - Labor and Delivery / L&D",
  "company": "Solomon Page",
  "location": "New York, NY",
  "via": "LinkedIn",
  "postedAgo": "6 hours ago",
  "postedAt": "2026-11-17T16:10:11+00:00",
  "salary": null,
  "jobType": "Contractor",
  "degree": "No Degree Mentioned",
  "otherTags": [
    "Dental insurance",
    "Health insurance"
  ],
  "applyOptions": [
    {
      "source": "LinkedIn",
      "url": "https://www.linkedin.com/jobs/view/registered-nurse-rn-labor-and-delivery-l-d-at-solomon-page-4491581477",
      "domain": "linkedin.com",
      "direct": false
    },
    {
      "source": "BeBee",
      "url": "https://bebee.com/us/jobs/registered-nurse-labor-and-delivery-ld-rn-36-12-holy-redeemer-new-york--lensa-7428_b49d0d20db42334741408ccf256d0a195c6ca6894a7a94765fe6effec1b44942",
      "domain": "bebee.com",
      "direct": false
    }
  ],
  "highlights": {
    "qualifications": [
      "Current New York license",
      "Excellent interpersonal skills including patience, empathy, and compassion",
      "Effective communication skills, including active listening, writing, speaking and reading comprehension",
      "… 3 more"
    ],
    "benefits": [
      "Estimated Gross Weekly Pay: $2,837",
      "Estimated Weekly Stipend: $1,967",
      "Offering a comprehensive benefits package, travel nurses have immediate access to medical coverage and ReviveHealth virtual care",
      "… 2 more"
    ],
    "responsibilities": [
      "Shift: 3x12 Nights",
      "More job highlights"
    ]
  },
  "description": "Our client is looking to add a Registered Nurse to their team.\nJob Details:\n• Location: Bronx, New York\n• Duration: 13 Weeks\n• Start Date: 12/09/2026\n• Shift: 3x12 Nights\n• Estimated Gross Weekly Pay: $2,837\n• Estimated Weekly Stipend: $1,9…",
  "googleJobId": "vM-UmBytgiYzR1wLAAAAAA==",
  "applyUrl": "https://www.linkedin.com/jobs/view/registered-nurse-rn-labor-and-delivery-l-d-at-solomon-page-4491581477",
  "scrapedAt": "2026-11-17T22:10:11+00:00"
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
