"""Verify the synthetic default-output redaction boundary.

This is a fixture verifier, not a usage collector. It intentionally projects
only aggregate-safe fields from synthetic records and asserts that the default
aggregate contains no prompt text, paths, session IDs, or credential hints.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "ai-usage-telemetry-redaction-fixture.json"
SENSITIVE_FIELDS = ("prompt_text", "file_path", "session_id", "credential_hint")


def aggregate(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Return the intentionally narrow default aggregate projection."""
    totals: dict[tuple[str, str, str], dict[str, int]] = defaultdict(
        lambda: {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0}
    )
    for record in records:
        key = (record["date"], record["agent"], record["model"])
        for field in ("input_tokens", "output_tokens", "cached_tokens"):
            totals[key][field] += int(record[field])

    rows = [
        {
            "date": date,
            "agent": agent,
            "model": model,
            **values,
        }
        for (date, agent, model), values in sorted(totals.items())
    ]
    dates = sorted(record["date"] for record in records)
    return {
        "collection_window": {"start": dates[0], "end": dates[-1]},
        "records_included": len(records),
        "by_date_agent_model": rows,
    }


def main() -> None:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    records = fixture["records"]
    output = aggregate(records)

    if output != fixture["expected_default_aggregate"]:
        raise AssertionError("Aggregate differs from the checked synthetic expectation")

    rendered = json.dumps(output, sort_keys=True)
    for record in records:
        for field in SENSITIVE_FIELDS:
            value = record[field]
            if value in rendered:
                raise AssertionError(f"Sensitive {field} leaked into default output")

    print("PASS: default aggregate matches fixture and excludes all sensitive fields")


if __name__ == "__main__":
    main()
