# Usage efficiency

How a research session spends its context and effort. Roles and limits are in [AGENT_CONFIGURATION.md](AGENT_CONFIGURATION.md), and the order of work is in [RESEARCH_WORKFLOW.md](RESEARCH_WORKFLOW.md).

## 1. Models

- **Main:** Sonnet 5.5, high effort.
- **Subagents:** Haiku 5.5, high effort.

## 2. Effort policy

| Effort | Use for |
|---|---|
| low | Listing files, simple `rg` searches, repetitive checks |
| medium | JSON formatting, routine documentation, ordinary validation |
| high | Main research and technical interpretation (the default) |
| xhigh | Complex architectural ambiguity and conflicting primary evidence |
| max | Exceptional cases only, where a measurable quality gain justifies the cost |

Do not enable xhigh or max globally. Raise effort for one task, then lower it again, and report the change in one line.

## 3. Context efficiency

- Check `/context` at major milestones, not after every action.
- Use `/compact` only when the active context becomes large. Preserve the current task, the exact target, completed phases, modified files, the current commit and CI state, unresolved findings, declined operations, safety rules and the next action.
- Use `/clear` only when switching to an unrelated task. Use `/resume` to continue an existing research session.
- Keep summaries concise, and carry unresolved questions across compaction.
- Do not re-read complete reports. Use `rg` to find a term or ID and `jq` to read one record. Read a file by line range when it is large.
- Filter logs and show failures only, for example `rg -n -C 3 'ERROR|Exception|failed' <log>`. Keep full output locally when it is evidence.
- Do not repeat a search that is already recorded. Check the claim and source databases first.

## 4. Tools and MCP

- Keep the reduced MCP configuration as it is. Do not add MCP servers or plugins.
- Prefer `git`, `gh`, `rg`, `jq` and Python. Do not use a GitHub MCP when the `gh` CLI is enough.
- Enable web access only when current primary-source research needs it, and use exact URLs and immutable commit references.
- Do not load tool definitions that the task does not need.

## 5. Subagents

- At most two, and one concurrent by default. Delegate only independent work that does not need the whole conversation.
- Require a concise summary (20 lines or fewer). No recursive spawning.

## 6. Stop conditions

- At most **two** reasonable attempts to retrieve an unavailable primary source. Then record `SOURCE_UNAVAILABLE`.
- At most **three** attempts at the same technical operation. Then change route or record `UNRESOLVED`.
- Do not continue a repetitive search without a new lead. Do not invent tasks to fill a report. If nothing changed, record `NO MATERIAL CHANGE`.
