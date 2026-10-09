---
name: subagent-orchestration
description: Plan and delegate work as the Opus orchestrator by breaking a request into goal, tasks, and subtasks, routing each subtask to the right Solo Empire sub-agent and model, writing a detailed delegation brief, integrating the structured handoffs, and closing with an external review-and-fix loop. Use before spawning any solo-* sub-agent, when a request spans several files or steps, or when Haiku workers need precise instructions.
---

# Subagent Orchestration

The main agent (Opus 5.5) is the planner and orchestrator. It owns the goal,
the decomposition, every delegation brief, integration, final verification, and
release approval. Sub-agents get one bounded subtask each and return the
`solo-empire.subagent-handoff.v1` contract in
`skills/ai-agent-workflows/references/sub-agent-handoff.md`.

## When not to delegate

- One known file, symbol, or fact → read or search it directly.
- The next step depends on a result you can get in one or two tool calls.
- The work needs the full conversation context or a user decision.
- The work is a release, push, deploy, spend, or external message; only the
  main agent does those.

## Workflow

1. **Frame the goal.** Write the user outcome in one sentence, measurable
   success criteria, constraints (repository boundaries, approvals, secrets),
   and explicit non-goals. Stop and ask when the outcome is a user decision.
2. **Decompose.** Build a `Goal → Task → Subtask` tree with the plan template in
   [`references/delegation-brief.md`](references/delegation-brief.md). A task is
   one verifiable outcome; a subtask is one role, one scope, and one
   deliverable that fits a single sub-agent run. Record dependencies and mark
   which subtasks can run in parallel.
3. **Route.** Pick the role and model per subtask with the routing table below.
   Keep subtasks the main agent will do itself in the same tree.
4. **Brief.** Write one delegation brief per subtask with every field of the
   brief template. Haiku workers get exact paths, search patterns, line
   ranges, expected counts, and the output shape; never "look around".
5. **Dispatch.** Send independent subtasks in one message so they run
   concurrently. Run dependent subtasks only after their inputs return.
6. **Integrate.** Validate each handoff: contract fields present, evidence is
   concrete (paths, lines, command output), tests distinguish passed from
   skipped. Re-run the decisive verification yourself; never forward a
   sub-agent claim as fact. Re-brief or escalate on `blocked`/`needs_parent`.
7. **Review loop.** After implementation passes focused checks, commit the
   scoped change and run the external reviewer on that commit:
   `codex review --commit <sha> -c review_model='"gpt-6.1-sol"' -c model='"gpt-6.1-sol"' -c model_reasoning_effort='"high"'`.
   Verify each finding, fix the real ones with a regression test, commit, and
   review the new commit. Stop when a review reports no confirmed finding.
8. **Report.** Summarize the tree status, what changed, verification evidence,
   review rounds and their findings, and residual risks.

## Routing table

| Subtask kind | Role | Model / effort |
| --- | --- | --- |
| Locate files, map call paths, collect evidence | `solo-explorer` | Haiku, `medium` |
| Schema, contract, lineage, query audit | `solo-data` | Haiku, `medium` |
| Browser rendering and interaction checks | `solo-ui-verifier` | Haiku, `medium` |
| Bounded code or docs change | `solo-implementer` | Haiku, `medium` |
| Reproduce and root-cause a failure | `solo-debugger` | Sonnet, `medium` |
| In-session diff review when Codex is unavailable | `solo-reviewer` | Sonnet, `medium` |
| Secrets, permissions, MCP, privacy audit | `solo-security` | inherit Opus |
| Independent review of every committed change | Codex CLI (step 7) | `gpt-6.1-sol`, `high` |

Models and efforts come from `claude_model` and `claude_effort` in
`.github/agents/roles.yaml`; change them there and run `task subagents:sync`.
Override per call with the Agent `model` parameter when a subtask is harder or
easier than its role default.

## Risk-based routing

| Task kind | Primary | Review gate |
| --- | --- | --- |
| Rename, formatting, boilerplate | Haiku implementer | Focused tests and lint |
| CRUD, API, UI component in known patterns | Haiku implementer | Tests, typecheck, static analysis |
| Multi-file feature or large refactor | Implementer with `model: sonnet` | Codex review |
| Complex debugging | Sonnet debugger; escalate to Opus | Codex review |
| Architecture or cross-system design | Opus (main agent) | Codex review |
| Security, migration, payment, data deletion | Opus security plus implementer with `model: sonnet` or `opus` | Codex review and tests; release approval stays with the user |

Automated checks (tests, lint, typecheck, CI) are always the first gate; the
Codex review never replaces them.

## Escalation rule

- A Haiku worker gets at most two attempts at the same subtask. After the second
  failed verification, re-dispatch with `model: sonnet` and the failure
  evidence in the brief.
- A Sonnet worker gets at most two attempts; then the main agent takes the
  subtask itself or asks the user.
- Never loop a worker on the same failing check without new evidence.

## Brief quality bar

- The brief stands alone: a worker with no conversation history can finish it.
- Scope lists files or directories in and out, plus what must not change.
- Acceptance criteria are checkable statements, not adjectives.
- Verification names exact commands and the expected result.
- Budget caps files read and tool calls so a worker stops instead of wandering.
- Stop conditions say when to return `blocked` or `needs_parent`.
- No credentials, tokens, cookies, or private payloads in the brief.

## Handoff

Return the goal tree with each subtask's status, the briefs that were sent,
integrated evidence, verification commands and results, review rounds, open
risks, and the single next safe action.
