# Track your brand in ChatGPT, Gemini, Copilot and Google AI Mode answers

The OpenAI, Gemini and Bing APIs don't give you what people actually see in **ChatGPT search, Gemini, Microsoft Copilot or Google AI Mode**: the answer with its cited sources and recommended products. These Actors ask each one your prompts as a new, logged-out visitor and return the full answer, every source, and a brand report: is your brand mentioned, at what rank against your competitors, and is your site cited.

| Actor | Engine | Price per 1,000 answers |
|---|---|---|
| [ChatGPT Search Scraper](https://apify.com/wulfcare/chatgpt-search-scraper) | ChatGPT with web search (plus recommended products and follow-up questions) | $50 |
| [Gemini Search Scraper](https://apify.com/wulfcare/gemini-search-scraper) | Google Gemini | $1 |
| [Google AI Mode Scraper](https://apify.com/wulfcare/google-ai-mode-scraper) | Google AI Mode | $4.50 |
| [Copilot Search Scraper](https://apify.com/wulfcare/copilot-search-scraper) | Microsoft Copilot Search (Bing) | $8 (+$8 when the residential proxy is needed) |
| [AI Visibility Tracker](https://apify.com/wulfcare/ai-visibility-tracker) | ChatGPT + Gemini + Google AI Overviews in one run, with visibility score, share of voice and an HTML report | $40 |

All five take the same input:

```python
from wulfcare import run   # ../wulfcare.py

answers = run("wulfcare/gemini-search-scraper", {
    "prompts": ["What is the best CRM for a small business?"],
    "yourBrand": "HubSpot, hubspot.com",                  # names, then your website
    "competitors": ["Salesforce, salesforce.com", "Pipedrive, pipedrive.com"],
    "repeats": 1,                                         # ask each prompt N times (AI answers vary)
})
for a in answers:
    print(a["prompt"], a["yourBrandMentioned"], a["yourBrandRank"], a["yourBrandCited"])
    print(a["brandsMentioned"], a["citedDomains"])
```

Each answer: `answerText` (markdown), `sources`, `citedDomains`, `brandsMentioned` (in order), `yourBrandMentioned`, `yourBrandRank`, `yourBrandCited`, per-competitor `brands`. Prompts that weren't answered are free.

One report across engines:

```python
run("wulfcare/ai-visibility-tracker", {
    "yourBrand": "Pipedrive, pipedrive.com",
    "competitors": ["HubSpot, hubspot.com", "Salesforce, salesforce.com"],
    "category": "CRM for small business",   # it writes the prompts for you
    "promptCount": 10,
    "engines": ["chatgpt", "gemini", "google_ai_overview"],
})
```

AI answers can be wrong and change between runs; these Actors return exactly what each engine said at run time.
