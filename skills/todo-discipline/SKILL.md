---
name: todo-discipline
description: Keep task-list state aligned with completed work.
version: 1.0.0
author: Frank Riemer / GenCreator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [todo, task-management, discipline, verification]
    related_skills: []
    provenance: frankx-public
    tier: free
---

# Todo Discipline (Free)

Agents often create task lists, do the work, then conclude while the UI still shows **0/N done**. This skill makes **task state = reality** a hard gate.

## Purpose

Reconcile the task list with completed work before handing off or claiming completion.

## When to Use

- Complex tasks with 3+ steps  
- Multi-agent or long sessions  
- Before any “done”, handover, or “battle-tested” claim  

**Don't use for:** single-step Q&A.

## Inputs

- The current task list and its item identifiers
- Evidence of which tasks are complete, active, or blocked

## Outputs

- Updated statuses for completed items
- A fresh read of the task list confirming the final state

## Required tools

- The host's task-list tool, with item-level status updates and a read-back operation

## Safety boundaries

- Preserve existing items and history; update only items whose state changed.
- Never clear a list by sending an empty replacement or merge payload.
- Do not mark work complete without evidence or claim the list is verified without reading it back.
- Use only operations supported by the host; argument names and merge behavior vary.

## Hard gate

Before any concluding message:

1. Update **every** finished item to completed (merge, don’t wipe history)  
2. **Immediately read** the task list again (no-args read)  
3. Only then write the final summary  

Treat the **read result** as ground truth if merge responses echo stale state (common in long/headless runs).

## Rules

- Prefer merge over full replace  
- Only one item `in_progress` at a time  
- Never pass an empty todos array on merge (can clear the list)  
- Supply full id + content + **new** status for items you change  

## Verification checklist

- [ ] All finished work marked completed  
- [ ] No stale in_progress when claiming done  
- [ ] Read-back confirmed  
- [ ] User-visible task counter matches reality  

## Provenance

Frank Riemer / GenCreator, `frankx-public` free pack. The workflow is a portable checklist, not a Hermes engine feature guarantee.

## Related resources

- [Hermes skill authoring docs](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
- [Hermes operator guidance](https://github.com/frankxai/awesome-hermes-agents)

## License

MIT — Frank Riemer / GenCreator.
