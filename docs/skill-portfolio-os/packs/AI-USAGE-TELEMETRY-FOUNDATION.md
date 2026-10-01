# Provider-Neutral AI Usage Telemetry Foundation

**Tier:** T1 sanitized reference — in progress, not yet a shipped skill
**Owner:** Shared Service / Skill Portfolio Ops
**Purpose:** A portable, privacy-first pattern for inspecting local AI-coding-agent usage without exporting session contents or treating estimated cost as a bill.

## What this reference standardizes

A future free telemetry skill may:

- read only the local usage records that a user explicitly authorizes;
- aggregate token counts by time period, agent, model, and project only where the selected parser declares support;
- emit local tables or JSON summaries with the data sources and collection window disclosed; and
- label every price calculation as an **estimate**, never as an invoice or subscription comparison.

It must not require a Starlight wrapper, brand identity, subscription details, local directory layout, credentials, or an upload/leaderboard account.

## Portable safety contract

1. **Read-only first.** Do not modify source logs, install persistent hooks, or transmit usage data by default.
2. **Explicit source support.** Detect a runtime only after the selected upstream parser documents it; a generic skill must not imply coverage from a similarly named tool.
3. **Private output.** Keep raw prompts, message text, file paths, account identifiers, and session IDs out of default reports. Aggregate counts are the portable output boundary.
4. **Honest cost language.** Model-price multiplication is an estimate that can differ from subscription, regional, cached-token, or invoice treatment.
5. **Review external execution.** A package runner or upstream binary is third-party code. Pin or review the version before a durable workflow, and never equate “local data reader” with a complete privacy guarantee.

## Minimal interface for a future skill

| Input | Validation | Output |
|---|---|---|
| Requested reporting window | Normalize timezone and state it in the report | Daily, weekly, monthly, or session aggregate |
| Selected agent/runtime | Confirm parser support from its current upstream documentation | Per-runtime inclusion/exclusion note |
| Local usage metadata | Redact identifiers and content before aggregation | Token totals, model breakdown, and optional estimated cost |
| Optional price table | Cite version/date and currency | Clearly marked estimate with assumptions |

## Upstream verification record — 2026-09-14

- [`junhoyeo/tokscale`](https://github.com/junhoyeo/tokscale) publishes an MIT license and currently documents Hermes Agent data support. Its optional public-submission capability is out of scope for this pattern.
- [`ryoppippi/ccusage`](https://github.com/ryoppippi/ccusage) publishes an MIT license and documents local usage analysis. Include it in a future implementation only after verifying the exact release supports each requested runtime; this reference makes no Hermes-coverage claim for it.

### Current evidence refresh — 2026-10-01

- `ccusage` release [`v20.0.26`](https://github.com/ryoppippi/ccusage/releases/tag/v20.0.26), published 2026-09-27, has an MIT application license at [`apps/ccusage/LICENSE`](https://github.com/ryoppippi/ccusage/blob/main/apps/ccusage/LICENSE). Its public [Hermes guide](https://ccusage.com/guide/hermes) documents the `hermes` source as **experimental**, reads local `$HERMES_HOME/state.db`, and exposes focused `daily`, `monthly`, and `session` reports. This is current parser-support evidence, not a stability or privacy guarantee.
- `tokscale` release [`v4.17.0`](https://github.com/junhoyeo/tokscale/releases/tag/v4.17.0), published 2026-09-15, retains an MIT repository license. This review did not retain a cite-ready current parser path for Hermes, so do not include it in a standalone Hermes implementation until that exact support evidence is independently re-verified.

### Weekly promotion checkpoint — 2026-09-21

**Owner:** Skill Portfolio Ops
**Done condition / proof:** a reproducible, synthetic redaction fixture runs locally and shows that default aggregate output excludes prompt text, paths, IDs, and credentials; current upstream evidence explicitly identifies every supported runtime.
**Decision / kill criterion:** ship a standalone T1 skill only if both proofs are present. Otherwise retain this reference as the portable artifact and close packaging work for this cycle—do not publish a collector based on inference from similarly named tools.

### Synthetic redaction proof — 2026-10-01

`fixtures/ai-usage-telemetry-redaction-fixture.json` contains synthetic-only source records with prompt text, paths, session IDs, and credential hints. Its stdlib-only verifier projects only date, agent, model, and numeric token totals, then proves the default aggregate matches the expected output while excluding every sensitive fixture value.

Run through `terminal`:

```python
terminal(command="python3 docs/skill-portfolio-os/packs/scripts/verify_ai_usage_telemetry_redaction.py")
```

A passing fixture closes only the reproducible-redaction-fixture sub-gate. It does **not** validate a live parser, establish current upstream runtime support, or authorize a standalone collector.

These projects are examples, not endorsed defaults. Re-check license, release, source coverage, data handling, and package integrity at implementation time.

## Promotion gate: standalone free skill

Before this reference becomes a distributed skill, provide:

- a reproducible test fixture with no real session data;
- current upstream license and runtime-support evidence for every suggested integration;
- a redaction test proving that default output excludes prompt text, paths, IDs, and credentials;
- an offline/read-only default; and
- a public README link plus tier-registry update.

Until then, this is a sanitized T1 foundation rather than an installable collector.
