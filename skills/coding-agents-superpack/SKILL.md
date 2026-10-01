---
name: coding-agents-superpack
description: Coordinate coding-agent CLIs with bounded, verified steps.
version: 1.0.0
author: Frank Riemer / GenCreator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Orchestration, Multi-CLI, Prompting, Free-Pack]
    related_skills: []
    provenance: frankx-public
    tier: free
---

# Coding Agents Superpack (Free)

Portable multi-CLI orchestration patterns for Hermes, Claude Code, Codex, OpenCode, Grok CLI, and similar agents.

**This free pack is sanitized.** Personal host quirks, private brand wiring, and machine-specific topology live in private overlays — not here.

## Purpose

Help an operator discover available coding-agent CLIs, choose a bounded workflow, and hand work between agents with verifiable artifacts.

## When to Use

- Multiple coding CLIs available; need discovery or comparison
- Designing structured prompts for autonomous coding agents
- Multi-agent collaboration with a shared board (Model Council pattern)
- Building hybrid “orchestrator drives + specialist CLI executes” workflows

**Don't use for:** single-CLI deep flags (load that vendor’s skill/docs); private multi-brand empire ops.

## Inputs

- The task, constraints, and acceptance checks
- Coding-agent CLIs available in the current environment
- A disposable worktree or temporary repository for trial runs

## Outputs

- A short comparison of available agents and relevant tradeoffs
- A scoped prompt or handoff artifact for each delegated task
- A verification report distinguishing completed work from pending work

## Required tools

- A terminal and filesystem tools for discovery and isolated trials
- Git for creating and inspecting a disposable worktree
- A shared board or explicit handoff artifact when agents collaborate

## Safety boundaries

- Verify each CLI's current help or vendor documentation before relying on flags; commands and approval options change.
- Do not enable always-approve or equivalent bypass flags by default.
- Use an isolated worktree for trials. Keep credentials out of prompts, logs, and shared boards.
- Require human approval for destructive changes, deployments, public posts, or spending.

## Discovery (run first)

Use a POSIX shell for these examples. On Windows, use WSL, Git Bash, or equivalent PowerShell checks.

```bash
command -v codex && codex --version
command -v claude && claude --version
command -v opencode && opencode --version
command -v grok && grok --version
# Check each installed CLI's current help for its diagnostics command.
```

Prefer **project-scoped** filesystem checks. Avoid recursive search from home or drive roots (slow, noisy, and unsafe on multi-device Windows setups).

Test agents in an isolated temp git repo:

```bash
TEST_DIR=$(mktemp -d)
cd "$TEST_DIR" && git init -q && echo "# test" > README.md && git add . && git commit -q -m init
```

## Non-interactive execution

Check each installed CLI's current help and vendor docs before choosing a non-interactive command or granting tools.

| Agent | Documentation |
|-------|---------------------------|
| Claude Code | Check the installed CLI's help and [current docs](https://docs.anthropic.com/en/docs/claude-code/cli-reference) |
| Codex | Check the installed CLI's help and [current docs](https://developers.openai.com/codex/cli) |
| OpenCode | Check the installed CLI's help and [current docs](https://opencode.ai/docs/cli/) |
| Other CLIs | Check the installed CLI's help and vendor docs; don't assume a shared headless syntax. |

## Universal prompt structure

```text
# Objective
Clear goal + measurable success criteria

# Context
1. Read these exact files first: …
2. Constraints: …

# Procedure
1. …
2. …

# Required Artifacts
- Files with exact paths
- Verification report

# Verification
Run tests/lint; report failures; do not claim done without evidence
```

## Model Council (lightweight multi-agent)

When agents must collaborate (not isolated one-shots):

1. Shared board file: `KANBAN_BOARD.md` (or Hermes kanban)
2. Shared state: `STATE.json` or equivalent
3. Role prompts force: **read board first**, **update board last**
4. Explicit handoff artifacts (`IMPLEMENTATION_BRIEF.md`, etc.)

Roles example: Chair · Planner · Implementer · Reviewer · Researcher

## Hybrid execution pattern

For large multi-repo work:

1. **Orchestrator** creates foundations with direct file/git ops (visible, fast)
2. **CLI specialists** get scoped tasks with the installed CLI's supported turn or budget limits
3. Publish a single **execution report** that separates *done* vs *delegated queue*
4. Never leave silent open tasks without a handoff document

## Safety & cost

- Cap turns/budget on headless runs  
- Restrict tools to what the task needs  
- Prefer print/one-shot modes for CI  
- Clean up tmux/sessions after interactive work  
- Never put secrets in prompts or board files  

## Verification checklist

- [ ] Discovery run; versions recorded  
- [ ] Prompt includes Objective/Context/Procedure/Verification  
- [ ] Headless flags set (max-turns/tools)  
- [ ] Artifacts exist on disk; tests/lint reported  
- [ ] Board updated if multi-agent  

## Related free resources

- [Hermes skill authoring docs](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills) and the [Hermes agents companion](https://github.com/frankxai/awesome-hermes-agents)
- Vendor documentation for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Codex](https://developers.openai.com/codex/cli), and [OpenCode](https://opencode.ai/docs/cli/)
- Workflow Tier plugin (MIT multi-agent workflows)  

## License

MIT — Frank Riemer / GenCreator. Upstream CLI behavior belongs to their vendors.

## Provenance

Frank Riemer / GenCreator, `frankx-public` free pack. CLI-specific commands are illustrative and must be checked against the installed vendor version.
