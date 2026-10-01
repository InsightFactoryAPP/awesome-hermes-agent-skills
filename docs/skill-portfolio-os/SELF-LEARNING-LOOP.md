# Self-Learning Loop (Absorb → Improve → Promote)

Self-learning is **not** optional. Every hard session must leave the system smarter. Hermes already supports skills as procedural memory; this OS makes the loop **explicit, tier-aware, and scalable**.

## The loop (tight)

```
RUN WORK
  → HIT FRICTION / WIN / CORRECTION
    → CAPTURE (failure mode, recipe, decision)
      → ABSORB (patch skill / new reference / new skill)
        → CLASSIFY (T0–T5)
          → PROMOTE (free) | GATE (premium) | KEEP (private)
            → VERIFY (checklist + next-run use)
              → LOG (this file + optional memory one-liner)
```

## When absorb is mandatory

| Trigger | Minimum absorb |
|---------|----------------|
| Same error twice | Pitfall + fix in skill |
| User correction of preference | Memory (durable) + skill if procedural |
| New CLI flag / version break | Leaf skill patch |
| Successful multi-step workflow (5+ tools) | Skill or reference |
| Cron/headless failure | todo-discipline / cron reference |
| Phone Link or host incident | path-safety skill immediately |
| Great multi-agent pattern | coding-agents or agentic-orchestration |
| Product boundary decision | CLASSIFICATION + PRODUCT-MAP |

## Session end protocol (agents)

Before any “work complete” (with todo-discipline):

1. List **what we learned** (3 bullets max if none).  
2. For each learning: **patch** skill OR **write** reference OR **create** skill.  
3. Classify promote path: free / gated / private.  
4. If free-worthy: open item in promote queue (`registry/PROMOTE-QUEUE.md`).  
5. Update todos merge+read.  

## Absorb targets by learning type

| Learning type | Write to | Tier default |
|---------------|----------|--------------|
| Host/Windows quirk | windows-phone-link-search-safety or frank-overlay | T0 / sanitized T1 |
| Multi-CLI routing | coding-agents | T4 + sanitized T1 |
| Single CLI flags | claude-code / codex / opencode | Official-aligned T1 |
| Completion discipline | todo-discipline | T1 core + T4 logs |
| Empire/strategy process | empire-planning | T4 |
| Awesome curation | awesome-list-maintenance | T1 process |
| Product packaging | skill-portfolio-ops + this OS | T4 process / T1 templates |
| Brand creative production | design-swarm / brand-image-system | T3 |
| Fitness N-of-1 | velora private instance | T4 / product T5 |

## Promote vs gate (after absorb)

```
Is the learning portable without Frank secrets?
  YES → sanitize → T1 free pack → public repo / hub
  NO  → does it power a paid SKU?
          YES → T3 vault / product docs
          NO  → T4 private only
```

## Self-evolution tooling (use, don’t wait)

| Tool | Role |
|------|------|
| `skill_manage(patch)` | Same-session improve |
| `hermes curator` | Lifecycle of agent-created skills |
| `skill-portfolio-ops` | Classification + promote gate |
| gencreator-swarm-evolver | Scheduled TEST/EVAL/EVOLVE cycles |
| multi-llm-arena | Measure agent/prompt quality |
| session_search | Mine past wins/failures |
| Optional: hermes-agent-self-evolution (DSPy/GEPA) | Evolve skill text when available |

## Weekly learning review (Queen / Frank)

1. session_search: “failure OR patch OR lesson OR pitfall”  
2. Diff skills touched this week  
3. Any skill patched ≥3 times → refactor (too much sediment)  
4. Any skill never loaded → archive candidate  
5. Promote queue: ship 1 free skill/pack per week minimum  

## Metrics that matter

| Metric | Target |
|--------|--------|
| Time-to-patch after failure | Same session |
| Free promotes / month | ≥4 high-quality |
| Orphan stubs (v0.1 no refs) | ↓ toward 0 |
| Description bloat (catalog) | Keep triggers short |
| Repeat user corrections | ↓ (memory + skills) |
| Public pack install health | CI green |

## Anti-patterns

- “We’ll write it up later” → lost learning  
- Patching only memory with procedures → wrong store (skills are procedures)  
- Promoting private failure logs with PII  
- Creating new skill instead of patching umbrella  
- Evolving skill text without verification checklist  

## Absorb log (append)

### 2026-07-15 — Skill Portfolio OS foundation

- Established dual-tree maintenance + T0–T5 classification  
- Rule: official leaves refreshable; Frank umbrellas local; free = sanitized  
- Self-learning mandatory session-end protocol  
- Products mapped open-core (not all-free, not all-gated)  
- Created `skill-portfolio-ops` Hermes skill + universe strategies package  

### 2026-07-15 — Wave 2 execution

- Absorbed MCR/AGY-MCR/SI into coding-agents; stubs are redirects  
- Free packs shipped; CSL PR #21; CoE kit SKU private outline  
- frank-overlay for claude-code leaf rebase  
- Funnel doc + weekly cron already scheduled  
- Learning: never push FrankX branches that inherited `.asph-wip` multi-100MB patches — branch from origin/main with pathspec commits only  

- 2026-08-03 — Weekly review: curator status still reported only `coding-agents` pinned after two local pin commands reported success; treat runtime-pin persistence as a T0/T4 operational verification item, not as a public-pack change.
- 2026-08-05 — Weekly review: curator again reported only `coding-agents` pinned while the registry requires five pins; retain this as a T0/T4 runtime-verification backlog, keep the three absorb-complete redirect stubs as documented aliases, and leave the sanitized Windows project-scoped search note as the active T1 promotion candidate.
- 2026-08-06 — Weekly review: curator still reports only `coding-agents` pinned (38 stale, none archived); public-pack scan found no redirect stubs, while the registry retains the three absorbed runtime aliases, so keep runtime-pin persistence as T0/T4 verification and the sanitized project-scoped-search note as the active T1 promotion candidate.
- 2026-08-10 — Weekly review: confirmed the three documented runtime redirects remain intentional; absorbed the duplicate `daily-building-in-public` surface into `build-in-public` as a T0 compatibility redirect, while the sanitized project-scoped-search note remains the active T1 promotion candidate.
- 2026-08-17 — Weekly review: curator reports 32 stale/0 archived and only `coding-agents` pinned; this cron also could not load its referenced bootstrap and path-safety skills. Classify pin/skill-registration verification as T0/T4 runtime work; retain the sanitized project-scoped-search note as the active T1 promotion candidate.
- 2026-08-28 — Weekly review: Hermes v0.20.6 is current; curator reports 2 managed agent-created skills with 0 stale/0 archived and 8 zero-activity unmanaged skills pending adoption review. No documented redirect stubs were found in active/public skill trees; the sanitized project-scoped-search note remains the active T1 promotion candidate, while missing runtime safety/process skills and pin-registration verification remain T0/T4 backlog.
- 2026-09-14 — Weekly review: patched `todo-discipline` to require tool discovery before declaring task-state verification unavailable; curator confirms only eligible agent-created skills can be pinned, so absent runtime safety/process pins remain T0/T4 remediation rather than a false compliance claim.
- 2026-09-14 — Weekly review: registry-marked MCR/AGY/SI and daily-building aliases remain installed as full legacy runtime skills rather than redirect stubs; re-open compatibility replacement after re-absorption, and extract only a provider-neutral, tool-verified T1 telemetry draft from the branded token-tracker candidate.
- 2026-09-14 — Weekly review: advanced the generic T1 project-scoped-search note into a sanitized draft; curator usage reports 31 agent-origin skills but only 3 curator-managed, so zero activity alone is not archive eligibility, while missing runtime pins and legacy full-copy candidates remain T0/T4 remediation.
- 2026-09-14 — Weekly review: curator reported 61 active skills, 3 agent-created, and two pins (`coding-agents`, `todo-discipline`); no MCR/AGY/SI/daily-building candidate path was found in the configured or default runtime roots, so retain the registry’s re-absorb queue for a profile-specific audit. The sanitized project-scoped-search note and provider-neutral telemetry foundation remain T1 candidates.
- 2026-09-14 — Weekly review: run curator status and dry-run with the active profile environment; the active profile had 60 managed skills with no proposed transitions and none of the registry’s legacy alias paths installed, so preserve the re-absorb queue as profile-specific remediation rather than claiming redirect-stub compliance.
- 2026-09-14 — Weekly review: resolve curator and candidate checks from the live `$HERMES_HOME` rather than the scheduled profile label; the shell selected `ethics-guardian`, where the dry-run proposed no transitions, required portfolio pins were absent, and no registry alias was installed. Keep re-absorption as an explicit T0/T4 backlog and report the scope.
- 2026-09-14 — Weekly review: resolve curator scope by explicitly setting and echoing the target `$HERMES_HOME`; the inherited cron environment pointed at another profile, while the target profile’s 60 managed skills had no dry-run transitions and none of the registry alias candidates, so this guard belongs in the weekly checklist rather than a speculative candidate merge.
- 2026-09-14 — Weekly review: curator dry-run’s “candidate skill(s)” count is the evaluated pool, not archive eligibility; only an explicit proposed transition authorizes an archive decision.
- 2026-09-14 — Weekly review: the public catalog has two packs and no public redirect stubs; target-profile candidate claims require exact installed-path evidence, so absent MCR/AGY/SI/daily-building aliases remain T0/T4 provisioning and re-absorption work rather than claimed redirect compliance.
- 2026-09-14 — Weekly review: target-profile curator dry-run proposed no transitions; pin flags were verified from `.usage.json`, `todo-discipline` and `coding-agents` were pinned, and the identical `daily-building-in-public` copy was reduced to a compatibility redirect to canonical `build-in-public`; MCR/AGY/SI and telemetry remain re-absorption/sanitization backlog.
- 2026-09-14 — Weekly review: exact target-profile inspection proved MCR/AGY/SI and `daily-building-in-public` are full legacy pages (the daily page differs from canonical `build-in-public`), never redirect compliance; require a portable, provenance-reviewed source before re-absorption and retain these as T0/T4 migration work.
- 2026-09-14 — Weekly review (data-guardian): explicitly scoped curator to `C:/Users/frank/AppData/Local/hermes/profiles/data-guardian`; its dry-run evaluated 60 skills but proposed no transitions, while none of the registry alias paths existed. Treat absent aliases as profile-scoped T0/T4 migration work and record checksums only when a legacy page is actually present.
- 2026-09-14 — Weekly review (frankx): explicitly scoped curator to `C:/Users/frank/AppData/Local/hermes/profiles/frankx`; its dry-run evaluated 62 skills with no transitions, `coding-agents` was read-back pinned, required safety/process skills and every registry alias/token candidate were absent, so no redirect or absorption claim is warranted beyond profile-scoped T0/T4 remediation.
- 2026-09-14 — Weekly review (gencreator): explicitly scoped the target profile before curator and alias checks; dry-run proposed no transitions and no queued alias or token-tracker source was installed, so no redirect or re-absorption claim is valid. Treat an available-but-unapplied Hermes update as a trigger to record, not proof that official leaves or overlays were rebased.
- 2026-09-14 — Weekly review (governance-guardian): scope curator and registry-candidate checks to the explicit profile; only agent-created installed skills are eligible for curator pins, and an absent candidate or a dry-run with no transition is T0/T4 remediation—not evidence of a redirect stub, absorption, or archival action.
- 2026-09-14 — Weekly review (income): explicit `$HERMES_HOME` scope showed 60 managed skills and no dry-run transitions; pin only eligible agent-created skills (`coding-agents`), while missing safety/process aliases and absent registry candidates remain profile-scoped T0/T4 remediation rather than claims of redirect or absorb compliance.
- 2026-09-14 — Weekly review (mind): explicit target-profile scope yielded 60 dry-run candidates with no proposed transition; `.usage.json` showed every required pin absent or `pinned: false`, while all registry alias paths were absent, so curator summaries never establish pin, redirect, or re-absorption compliance.
- 2026-09-14 — Weekly review (reality): explicit `HERMES_HOME` dry-run evaluated 60 skills with no transition; all five portfolio pin flags were absent or false, and every registry alias/telemetry path was absent, so no redirect-stub, re-absorption, or archive claim is valid—retain profile-scoped T0/T4 remediation.
- 2026-09-14 — Weekly review (research): target-profile curator dry-run evaluated 60 skills but proposed no transition; `.usage.json` marks `coding-agents` and `hermes-agent` unpinned and has no required safety/process entries, while registry aliases are absent, so keep pin and re-absorption claims as profile-scoped T0/T4 remediation.
- 2026-09-14 — Weekly review (starlight): explicitly scoped curator evaluated 60 skills with no proposed transition; `coding-agents` was read-back pinned, every required legacy alias was absent, and a branded local MIT telemetry source was reduced to a provider-neutral T1 foundation with per-runtime support and redaction gates.
- 2026-09-14 — Weekly review (strategy-guardian): explicitly scoped curator to the target profile; dry-run proposed no transitions, all five registry pin flags were absent or false, registry aliases were absent, and a 868-commit-behind Hermes update remains deferred rather than evidence of leaf or overlay rebase.
- 2026-09-14 — Weekly review (talent-guardian): explicit target scope evaluated 60 skills with no dry-run transition; `coding-agents` was read-back pinned, all seven registry alias/token candidate paths and the three required safety/process skill paths were absent, so retain missing registrations and re-absorption as profile-scoped T0/T4 remediation—not redirect, absorption, or archive compliance.
- 2026-10-01 — Weekly review (6pillar-guardian-factory): a synthetic telemetry fixture plus stdlib verifier now proves default aggregates exclude prompt text, paths, session IDs, and credential hints; keep standalone packaging blocked pending current parser-support and license evidence.
- 2026-10-01 — Weekly review (aicoe): explicitly scoped curator checks found no transition and no registry aliases; refreshed ccusage’s MIT app-license and experimental Hermes adapter evidence, so retain the T1 foundation but gate standalone packaging on a reproducible offline parser-support check.
- 2026-10-01 — Weekly review (anime): an unattended cron may approval-block a read-only shell wrapper, so weekly runtime evidence must fall back to direct readers or targeted profile-path checks; scoped curator dry-run proposed no transitions, candidate aliases were absent, and only eligible `coding-agents` was read-back pinned.
- 2026-10-01 — Weekly review (arcanea): explicitly scoped Curator allowed the eligible `coding-agents` pin to be remediated and read back from `.usage.json`; absent required aliases remain T0/T4, while the T1 telemetry source was corrected to canonical `ccusage/ccusage` and its synthetic default-redaction proof re-ran cleanly.
- 2026-10-01 — Weekly review (arcanea-chief-of-staff): explicit curator scope evaluated 60 skills with no proposed transition; `coding-agents` was read-back pinned, while bundled `hermes-agent` is ineligible and the three remaining required skills plus all registry alias candidates are absent. Keep pin/re-absorption work profile-scoped T0/T4; the available Hermes update is deferred, not evidence of an official-leaf refresh.
- 2026-10-01 — Weekly review (arcanea-content-operator): explicitly scoped curator evaluated 60 skills with no dry-run transition; `.usage.json` shows all five required pin flags false or absent, and exact `SKILL.md` front-matter checks found all seven registry alias/token candidates absent. No redirect, absorption, archive, or pin-compliance claim is valid; Hermes v0.21.3 reports 11,170 commits behind and remains a deferred runtime signal. The T1 synthetic redaction verifier passed.
- 2026-10-01 — Weekly review (arcanea-finance-operator): scope Curator and registry checks with an explicit profile home; its dry-run proposed no transitions, the only eligible core pin (`coding-agents`) was remediated and read back, and all seven legacy/telemetry candidate aliases were absent. A candidate count or missing page is never redirect, absorption, or archive compliance; retain missing skills and re-absorption as profile-scoped T0/T4 work.
- 2026-10-01 — Weekly review (ethics-guardian): with the profile home set explicitly, curator dry-run proposed no transition; the initial five-pin check was false or absent, then eligible agent-created `coding-agents` was pinned and read back true. `todo-discipline` remains false, bundled `hermes-agent` is ineligible and false, and `windows-phone-link-search-safety` plus `skill-portfolio-ops` are absent; all seven alias/telemetry candidates were absent. Treat this as profile-scoped T0/T4 remediation—not evidence of redirect, re-absorption, archive, or full pin compliance—and retain the verified synthetic T1 redaction fixture as the free-pack-in-progress gate.
- 2026-10-01 — Weekly review (technology-guardian): explicit `HERMES_HOME` scope yielded 60 managed skills and a dry-run with no transition; the eligible `coding-agents` pin was remediated and read back true, while `todo-discipline` remains false, bundled `hermes-agent` is ineligible, and the required safety/process skills plus all seven registry alias/telemetry candidates are absent. This is profile-scoped T0/T4 remediation—not redirect, re-absorption, archive, or full pin compliance; the Hermes update remains deferred.
- 2026-10-01 — Weekly review (arcanea-growth-operator): explicit `HERMES_HOME` Curator dry-run evaluated 60 skills with no transition; the eligible `coding-agents` pin was remediated and read back, while `todo-discipline`, `windows-phone-link-search-safety`, and `skill-portfolio-ops` are absent and bundled `hermes-agent` remains unpinned. No registry-listed legacy stub, alias, or telemetry candidate is installed, so retain this as profile-scoped T0/T4 remediation—not redirect, re-absorption, archive, or full-pin compliance; the synthetic T1 redaction verifier passes but standalone packaging remains gated on offline parser-support proof.
- 2026-10-01 — Weekly review (arcanea-product-operator): explicit profile scope yielded 60 curator-managed skills and no dry-run transition; `coding-agents` was pin-remediated and read back true, while `todo-discipline`, `windows-phone-link-search-safety`, and `skill-portfolio-ops` are absent and bundled `hermes-agent` is ineligible/unpinned. All registry legacy-alias and telemetry candidates are absent, so no redirect, checksum, absorption, or archive claim is valid; retain re-absorb work as profile-scoped T0/T4 backlog. The synthetic T1 redaction verifier passed, but standalone packaging remains blocked on offline parser-support proof.
- 2026-10-01 — Weekly review (c940-queen): explicit scope found 76 curator-managed skills with no dry-run transition and only `coding-agents`/`todo-discipline` pinned; `daily-building-in-public` is a minimal compatibility redirect, while MCR/AGY/SI are full legacy pages and both telemetry skills remain source candidates. Retain re-absorption as T0/T4 work pending provenance and command-safety review; Hermes v0.21.3 is 11,257 commits behind, a deferred runtime signal.
- 2026-10-01 — Weekly review (command-center): explicit scope found 76 curator-managed skills and no dry-run transition; `coding-agents`/`todo-discipline` are read-back pinned, the three runtime safety/process skills are absent, and exact nested front-matter checks found no registry alias or telemetry candidate. Candidate absence is profile-scoped T0/T4 remediation—not redirect, absorption, archive, or full-pin compliance; Hermes v0.21.3 remains a deferred runtime signal.
- 2026-10-01 — Weekly review (data-guardian): explicit target scope found 60 curator-managed skills and no dry-run transition; only eligible `coding-agents` was read-back pinned, while loadable `todo-discipline` has `created_by: null`/`pinned: false` and the required safety/process skills are absent, so loader availability, curator eligibility, and registry state must be recorded separately rather than inferred as pin or redirect compliance.
- 2026-10-01 — Weekly review (frankx): explicit `HERMES_HOME` scope found 62 managed skills and no dry-run transition; only `coding-agents` was read-back pinned, all registry alias/token candidates were absent, and the synthetic T1 telemetry redaction verifier passed, so missing safety/process registrations and re-absorption remain profile-scoped T0/T4 work rather than redirect, archive, or pin-compliance claims.
