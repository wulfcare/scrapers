"""Run any Wulfcare Data scraper on Apify from Python and get its results as a list of dicts.

    pip install apify-client
    export APIFY_TOKEN=...   # https://console.apify.com/settings/integrations

    from wulfcare import run
    rows = run("wulfcare/google-trends-scraper", {"searchTerms": ["coffee, tea"]})
"""

from __future__ import annotations

import os

from apify_client import ApifyClient


def run(actor: str, run_input: dict, token: str | None = None) -> list[dict]:
    """Run an Actor (e.g. "wulfcare/google-trends-scraper"), wait for it to finish, return its dataset items."""
    client = ApifyClient(token or os.environ["APIFY_TOKEN"])
    result = client.actor(actor).call(run_input=run_input)
    if result is None:
        raise RuntimeError(f"{actor}: run did not start")
    dataset_id = result["defaultDatasetId"] if isinstance(result, dict) else result.default_dataset_id
    return list(client.dataset(dataset_id).iterate_items())
