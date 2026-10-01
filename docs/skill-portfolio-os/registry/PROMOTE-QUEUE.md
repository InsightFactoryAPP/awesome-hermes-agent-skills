# Promote Queue

## Ready to sanitize & ship (free)

1. **Windows project-scoped search note** — T1 generic one-page note (not an incident skill); sanitizer review and public discoverability links were completed on 2026-09-14 at `docs/skill-portfolio-os/packs/WINDOWS-PROJECT-SCOPED-SEARCH.md`. **Next:** package it as a standalone free skill only if its portable note format no longer meets the distribution need; otherwise retain it as the linked public note.
2. **Provider-neutral AI usage telemetry foundation** — **in progress**: sanitized T1 foundation added at [`packs/AI-USAGE-TELEMETRY-FOUNDATION.md`](../packs/AI-USAGE-TELEMETRY-FOUNDATION.md). A synthetic-only redaction fixture and stdlib verifier prove the default aggregate excludes prompt text, paths, IDs, and credential hints without touching live session data. **Advanced 2026-10-01:** refreshed `ccusage` evidence links its MIT app license and v20.0.26 Hermes adapter documentation; the Arcanea review re-ran the synthetic verifier and confirmed the maintained GitHub source is [`ccusage/ccusage`](https://github.com/ccusage/ccusage). That adapter is explicitly experimental and reads local `$HERMES_HOME/state.db`. Tokscale v4.17.0 retains an MIT repo license but lacks cite-ready Hermes parser evidence in this review. **Reverified 2026-10-01:** the synthetic redaction verifier passed again; this does not satisfy the parser-support gate. **Next:** add an explicit, offline parser-support check for the selected implementation and preserve the default read-only/redaction boundary before packaging a standalone free skill.

## Blocked (need more work)

| Item | Blocker |
|------|---------|
| Full starlight-queen | Brand/empire ops; needs heavy sanitize |
| Full multi-llm-arena | Productize first as SIS premium |
| Higgsfield full OS | Brand kits gated |

## Shipped

| Date | Pack | Repo | Notes |
|------|------|------|-------|
| 2026-07-15 | coding-agents-superpack | awesome-hermes-agent-skills | Sanitized free |
| 2026-07-15 | todo-discipline | awesome-hermes-agent-skills + claude-skills-library/free-skills | Generic free |

## Definition of shipped

- [ ] Public commit/PR merged  
- [ ] Sanitizer checklist green  
- [ ] Linked from ≥1 awesome or README  
- [ ] Tier registry updated  
