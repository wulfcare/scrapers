# Google Jobs API (salaries, descriptions and apply links)

Google has no public API for the job listings it shows in search ("Google for Jobs"). The [Google Jobs Scraper on Apify](https://apify.com/wulfcare/google-jobs-scraper) returns them as JSON: title, company, location, salary, job type, posted date, full description, highlights and **every apply link** (LinkedIn, Indeed, the company's own site...). Up to 200 unique jobs per search, 27 countries.

```python
from wulfcare import run   # ../wulfcare.py

jobs = run("wulfcare/google-jobs-scraper", {
    "queries": ["data analyst jobs london", "nurse jobs new york"],
    "country": "US",
    "maxJobsPerQuery": 100,
})
for j in jobs:
    print(j["title"], "|", j["company"], "|", j.get("salary"), "|", j["applyUrl"])
```

Each job: `title`, `company`, `location`, `via`, `postedAt`, `salary`, `jobType`, `applyUrl`, `applyOptions`, `highlights`, `description`, `googleJobId`.

**Cost:** $0.004 per unique job. Duplicates and searches with no jobs are never charged.
