---
name: ai-agents
description: Operate Solo Empire tools safely from an AI agent, including MCP servers, CLI automation, Task commands, structured tool results, AI logs, and infrastructure-layer integrations. Use when wiring or running an agent against existing Solo Empire tools or infra. Not for designing or evaluating agent loops, RAG, or memory — use ai-agent-workflows.
---

# AI Agents — Solo Empire

## Overview

Use this skill to design and operate AI agents that follow a reliable tool-use
loop. Treat `skills/` as the agent instruction layer and `infra/` as the
implementation and tool layer: invoke existing CLI commands, scripts, MCP
tools, and tests before adding new mechanisms.

## Response language

Use Thai for all human-facing agent responses by default. Keep code, commands,
paths, identifiers, logs, protocol fields, and quoted source text exact. Follow
another language only when the user explicitly requests it for the response or
artifact.

## Workflow

### 1. Establish context

- Read `dashboard/CURRENT-STATE.md` and the relevant sections of
  `docs/ARCHITECTURE.md`, `docs/AI-AGENT-GUIDE.md`, and `infra/README.md`
  before substantial work. Use focused `rg`/`sed` ranges or the bounded
  operator context pack instead of loading long documents in full unless the
  task needs their complete contract.
- Read the relevant `operations/` or `integrations/` document when
  the task concerns a documented platform or external integration.
- Inspect `git status --short` and preserve unrelated user changes. Do not use
  destructive Git commands.

For an agent feature, identify the complete loop before editing:

```text
request → agent instructions → tool selection → infra operation → structured result → next decision
```

### 2. Route to the existing capability

| Request | Primary boundary |
|---|---|
| Dashboard, health, skills, goals, projects, tasks | `infra/cli.ts` and the SQLite database |
| Database schema or migration | `infra/database/` and `infra/scripts/db/` |
| AI-facing tool or MCP behavior | `infra/mcp-server/` |
| REST endpoint or client | `infra/api/` |
| Scheduled workflow or system automation | `infra/scripts/` |
| Kubernetes, GitOps, IaC, policies, onboarding | `infra/platform/` |
| Local services and homelab | `infra/self-hosted-stack/` |
| System-wide verification | `infra/tests/` and `infra/package.json` |

Follow the tool-selection and context-efficiency policy in
`skills/ai-agent-workflows/SKILL.md`. Keep inputs explicit and bounded, and use
structured results rather than scraping human-formatted output when a
structured interface exists.

### 3. Make the change safely

- Keep implementation in `infra/`; do not put runtime code in this skill.
- Use `apply_patch` for source and documentation edits.
- Back up the database before schema or data migrations:
  `task db:backup`.
- Keep credentials in the documented environment or secret store. Never print,
  copy, or commit values from `infra/.env`, tokens, cookies, or private data.
- Treat `data/`, generated reports, backups, and nested repositories as separate
  boundaries.
- For external services, verify that the required credential is available and
  report it as unavailable instead of asking the user to paste a secret.

### 4. Verify proportionally

Run the narrowest relevant checks, then the repository checks required for the
change:

- General changes: `task test`, `task typecheck`, and `task docs:check`.
- Database changes: relevant tests under `infra/tests/`, plus
  `task db:verify`.
- Platform changes: `task test:platform` and the relevant
  validation scripts under `infra/platform/`.
- MCP changes: `task test:mcp`.
- Go task-sync or notifier changes: `task test:go`.
- Python automation changes: `task test:python` and the
  focused test for the affected workflow.

If a check cannot run because an external service, credential, or local daemon
is unavailable, record the exact limitation and do not hide the failure.

## Decision rules

- Need a new AI-facing capability → implement or extend an MCP tool under
  `infra/mcp-server/`, then document its selection and safety rules here if it
  is reusable.
- Need a repeatable deterministic operation → implement or reuse an
  `infra/scripts/` helper; do not embed it in `SKILL.md`.
- Need agent judgment, routing, or safety procedure → update this skill.
- Need durable operational policy or a runbook → update `operations/` or
  the relevant documentation boundary, not this skill alone.
- Need a blank reusable document or artifact → copy from `templates/` into its
  owning workspace and leave the source template unchanged.
- Need to update learning progress → use the existing skills CLI or MCP tool;
  do not confuse database-tracked learning skills with this AI skill package.

## Handoff

Report the files changed, commands and tests run, important outputs or failures,
commit/push/deploy evidence, credential/service limitations, and any follow-up
task. Follow the repository's automatic release closeout preference for scoped
Git and documented non-production deployment actions; retain approval gates for
production, destructive, paid, credential, and external-message actions.
