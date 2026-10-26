# AI Training Jobs: Mercor, Outlier, DataAnnotation, Alignerr +11

`wulfcare/ai-training-jobs-scraper`: AI trainer, AI tutor and data-annotation jobs from 15 platforms: Mercor, Alignerr, Outlier, DataAnnotation, Mindrift, Meridial (Invisible), Turing, micro1, Welo Data, OneForma, xAI, Handshake AI, Appen and more. Pay as numbers, location, date, apply link. Only-new-jobs mode.

**Use it for:**
- AI training, AI tutor and data annotation job listings (Mercor, Outlier, DataAnnotation, Alignerr, Turing and more)

- Store page: https://apify.com/wulfcare/ai-training-jobs-scraper
- OpenAPI spec: https://api.apify.com/v2/acts/wulfcare~ai-training-jobs-scraper/builds/default/openapi.json
- MCP: `https://mcp.apify.com?tools=wulfcare/ai-training-jobs-scraper`

**Price:**
- Free (only Apify platform usage, usually fractions of a cent)

## Call it

```bash
curl -X POST "https://api.apify.com/v2/acts/wulfcare~ai-training-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["python"], "minHourlyRate": 30}'
```

```python
from apify_client import ApifyClient
client = ApifyClient(APIFY_TOKEN)
run = client.actor("wulfcare/ai-training-jobs-scraper").call(run_input={"keywords": ["python"], "minHourlyRate": 30})
dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id  # apify-client 1-2 vs 3+
items = list(client.dataset(dataset_id).iterate_items())
```

## Input

| Field | Type | Required | Default | Allowed values | Description |
|---|---|---|---|---|---|
| `platforms` | array |  | ["mercor", "alignerr", "micro1", "xai", "handshake", "appen", "remotasks", "humansignal", "outlier", "dataannotation", "mindrift", "meridial", "welo", "turing", "oneforma"] |  | Platforms: Which AI-training platforms to read. Leave empty for all of them. |
| `keywords` | array |  |  |  | Keywords: Return only jobs that mention at least one of these in the title, category, skills or client name (e.g. 'law', 'medicine', 'python', 'spanish'). Whole words: 'law' does not match 'lawn'. End a word with * to allow endings ('math*' matches math and mathematics). Leave empty for every job. |
| `excludeKeywords` | array |  |  |  | Exclude keywords: Drop jobs whose title, category or skills mention any of these (e.g. 'audio', 'transcription'). |
| `searchDescriptions` | boolean |  | false |  | Also search job descriptions: Match keywords inside the full job description too. Finds more jobs but also loose matches (a physics job that mentions 'laws of motion' would match 'law'). |
| `minHourlyRate` | integer |  |  | 0– | Minimum hourly pay (USD): Keep only hourly jobs whose top rate is at least this much. Jobs paid per task, one-off or without a stated rate are dropped when this is set. |
| `remoteOnly` | boolean |  | false |  | Remote only: Keep only jobs listed as remote. |
| `postedWithin` | string |  |  |  | Posted within: Only jobs first posted in this period, e.g. '24 hours', '7 days', '2 weeks', or since a date like 2026-09-01. Alignerr dates come from each job page (needs 'Full job details'). |
| `onlyNewJobs` | boolean |  | false |  | Only new jobs (for schedules): Return, and charge for, only jobs that earlier runs with the same filters have not returned yet. Perfect for a daily schedule that feeds Slack, email or a sheet. The list of seen jobs is kept in a key-value store named 'ai-training-jobs-monitor' in your own account. |
| `monitorName` | string |  |  |  | Monitor name: Optional. Runs with the same monitor name share one 'already seen' list. By default the list is tied to your platform and filter choices. |
| `maxJobs` | integer |  | 1000 | 0– | Maximum jobs: Stop after this many jobs (newest first). 0 = no limit. All platforms together have about 1,350 distinct jobs (about 6,400 with every Alignerr city listing). |
| `includeDescriptions` | boolean |  | true |  | Include job descriptions: Full job description text in each row. Turn off for smaller rows. |
| `fullDetails` | boolean |  | true |  | Full job details (Alignerr, micro1): Open the page of each returned Alignerr and micro1 job. Alignerr's list has only a short summary and no date; micro1's list has no description or number of openings. Turn off for a faster run with less detail. |
| `alignerrAllLocations` | boolean |  | false |  | Every Alignerr city listing: Alignerr lists most remote roles once per city (one role can have 300+ identical copies). By default you get one row per role, with the number of copies in 'openings'. Turn on to get every copy as its own row (about 5,600). |

## Output: one dataset item (real run, long values trimmed)

```json
{
  "platform": "Mindrift",
  "jobId": "1CF04FF2E4",
  "title": "$110 for 90 Minutes of Conversation: Paid Research Study",
  "company": "Mindrift",
  "category": "Paid research study",
  "skills": null,
  "payMin": 110,
  "payMax": 110,
  "payCurrency": "USD",
  "payPeriod": "one-time",
  "payText": "$110 for 90 Minutes of Conversation: Paid Research Study",
  "hoursPerWeek": null,
  "commitment": "Part-time",
  "workArrangement": "onsite",
  "location": "San Mateo, California, United States",
  "eligibleCountries": [
    "United States"
  ],
  "postedAt": "2026-10-25T00:00:00Z",
  "url": "https://apply.workable.com/j/1CF04FF2E4",
  "description": "About the study\nMindrift is conducting an in-person research study exploring how people communicate and interact in everyday group conversations.\nWe're looking for adults in the Santa Clara Valley (South Bay) area to join a paid, guided con…",
  "referralBonus": null,
  "openings": null,
  "isNew": null,
  "scrapedAt": "2026-10-25T15:07:22Z",
  "error": null
}
```

Results are what the source showed at run time and can contain errors; check anything important before relying on it.
