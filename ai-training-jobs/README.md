# AI training jobs from 15 platforms in one feed (free)

AI trainer, AI tutor and data-annotation jobs are spread over a dozen sites, each with its own job board. The [AI Training Jobs Scraper](https://apify.com/wulfcare/ai-training-jobs-scraper) collects them into one list with pay as numbers: **Mercor, Alignerr, Outlier, DataAnnotation, Mindrift, Meridial (Invisible), Turing, micro1, Welo Data, OneForma, xAI, Handshake AI, Appen, Remotasks, HumanSignal**.

Free: no per-job charge, only Apify's tiny platform usage (a full run of every platform used about $0.001).

```python
from wulfcare import run   # ../wulfcare.py

jobs = run("wulfcare/ai-training-jobs-scraper", {
    "keywords": ["python", "math"],
    "minHourlyRate": 30,
    "remoteOnly": True,
    "onlyNewJobs": False,   # True: only jobs earlier runs with the same filters have not returned
})
for j in jobs:
    print(j["platform"], j["title"], j["payText"], j["url"])
```

Each job: `platform`, `title`, `company`, `category`, `skills`, `payMin`, `payMax`, `payCurrency`, `payPeriod`, `hoursPerWeek`, `location`, `eligibleCountries`, `postedAt`, `url`, `description`, `isNew`.

Run it on an Apify schedule with `onlyNewJobs` for a daily alert of new postings.
