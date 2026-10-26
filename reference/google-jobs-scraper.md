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
  "query": "remote software engineer",
  "searchUsed": "remote software engineer",
  "country": "US",
  "position": 1,
  "title": "Full-Stack Software Engineer (New Grad) - Remote",
  "company": "SpruceID",
  "location": "Anywhere",
  "via": "ZipRecruiter",
  "postedAgo": "8 days ago",
  "postedAt": "2026-10-17T10:01:13+00:00",
  "salary": "110K-140K a year",
  "jobType": "Full-time",
  "degree": null,
  "otherTags": [],
  "applyOptions": [
    {
      "source": "ZipRecruiter",
      "url": "https://www.ziprecruiter.com/c/SpruceID/Job/Full-Stack-Software-Engineer-Remote/-in-Remote,US?jid=19daffea3bfe03e5",
      "domain": "ziprecruiter.com",
      "direct": false
    },
    {
      "source": "Jobgether",
      "url": "https://jobgether.com/offer/6a7bdabf490731f1e196f124-full-stack-software-engineer---remote-services",
      "domain": "jobgether.com",
      "direct": false
    },
    {
      "source": "JobLeads",
      "url": "https://www.jobleads.com/us/job/full-stack-software-engineer-new-grad-remote--united-states--e458dc7a885af25429cd861e8c385462b",
      "domain": "jobleads.com",
      "direct": false
    },
    "… 5 more"
  ],
  "highlights": {
    "qualifications": [
      "This is an ideal role for a recent graduate who wants to grow quickly while working on technology that matters",
      "We're not looking for someone who already knows everything",
      "We're looking for someone eager to learn, humble enough to ask questions, and motivated to do meaningful work",
      "… 15 more"
    ],
    "benefits": [
      "Dedicated mentorship from senior engineers who will guide your technical development"
    ],
    "responsibilities": [
      "You'll work alongside experienced engineers and directly with state governments, public sector partners, and enterprise clients to help design, build, and deploy impactful identity solutions",
      "You'll gain hands-on experience across the full stack, learn from senior engineers, and contribute to systems that serve millions of people",
      "Collaborate with customer delivery leads, engineers, and UX designers on real-world deployments",
      "… 11 more"
    ]
  },
  "description": "About SpruceID\nSpruceID builds privacy-preserving, standards-based digital identity and credentialing solutions that give individuals control of their information while enabling governments and enterprises to deliver secure, interoperable s…",
  "googleJobId": "UsmJK6H351WAV-x4AAAAAA==",
  "applyUrl": "https://www.monster.com/job-openings/full-stack-software-engineer-new-grad-remote-beverly-hills-ca--706c9c1e-bef1-4862-823f-d1bfce004f9a",
  "scrapedAt": "2026-10-25T10:01:13+00:00"
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
