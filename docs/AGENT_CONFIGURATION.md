# Agent configuration

How AI agents are intended to be configured for work in this repository. The rules in `CLAUDE.md` apply to every agent. This page covers roles, models and limits only. It stores no credentials, tokens or personal data.

## 1. Roles

| Role | Model | Default effort | Responsibilities |
|---|---|---|---|
| Main agent | Sonnet 5.5 | high | Orchestration, technical reasoning, evidence assessment, compatibility decisions, integration of local static-analysis results, documentation, publication |
| Subagents | Haiku 5.5 | high | Isolated tasks that save main-context space: primary-source verification, manifest metadata inspection, repetitive evidence classification, small read-only audits |

- At most **two** subagents exist, and **one** runs at a time by default. Two run together only when their tasks are independent.
- No agent teams. No recursive spawning. Subagents do not commit, push, publish or touch any device.
- Subagents return a concise evidence summary, not a source dump. The agent definitions below cap output at 20 lines.

**Not delegated:** final security conclusions, device compatibility verdicts, repository publication, and anything involving a physical device.

## 2. Project agents

Two read-only research agents are defined in `.claude/agents/`:

| File | Purpose | Tools |
|---|---|---|
| `primary-source-auditor.md` | Checks one narrowly scoped public claim against original sources in assigned snapshots | Read, Grep, Glob |
| `manifest-auditor.md` | Reviews existing manifest metadata and local summaries for consistency | Read, Grep, Glob |

Neither agent has shell, network or write tools, and neither loads an MCP server. They read files the main agent points them to. Do not add a third research agent without a stated need.

Both files use the frontmatter fields `model: haiku`, `effort: high` and `maxTurns: 8`. These fields are used where the installed Claude Code version supports them. If a field is unsupported, the agent still works from its instructions, and the difference is noted in the session report.

A newly created `.claude/agents/` directory may require restarting the session before the agents are discovered.

## 3. Verifying the actual model selection

- Do not assume that an alias resolves to a particular version. Check it.
- In a session, inspect `/model`, `/status` and the effort setting, and confirm that the main model and the subagent model are the intended ones.
- Use supported aliases (`sonnet`, `haiku`) in agent files, and do not hardcode a full model identifier that may be unavailable.
- If an intended model is unavailable, report that. Do not switch to another model automatically.

## 4. Effort selection

Default is high for both roles. Raise or lower it for a task, and restore it afterwards. The policy is in [USAGE_EFFICIENCY.md](USAGE_EFFICIENCY.md). Report each escalation in one line: model, previous effort, new effort, reason, whether it will be restored.

## 5. Subagent restrictions

- Read-only. No code execution, no download or build of exploit binaries, no device testing, no payloads, no bypass development.
- Scope given in the task: the files or URLs to read, the output format and the stop condition. No open-ended browsing.
- Findings are returned with source, date, evidence class, confidence, limitations and open questions. The main agent re-checks any high-impact finding before it is recorded.
- A subagent never makes the final compatibility decision.

## 6. Stop conditions

See [RESEARCH_WORKFLOW.md](RESEARCH_WORKFLOW.md), section 1. In short: one question, original source first, at most two corroborating sources, then stop and record the result or `SOURCE_UNAVAILABLE` / `UNRESOLVED`.
