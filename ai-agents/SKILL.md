---
name: ai-agents
description: Build and operate AI agents that use Solo Empire tools safely. Use when a task involves agent workflows, tool selection, MCP tools, CLI automation, structured tool results, agent memory, RAG, AI logs, or connecting AI behavior to the Solo Empire infrastructure layer.
---

# AI Agents — Solo Empire

## Overview

Use this skill to design and operate AI agents that follow a reliable tool-use
loop. Treat `skills/` as the agent instruction layer and `infra/` as the
implementation and tool layer: invoke existing CLI commands, scripts, MCP
tools, and tests before adding new mechanisms.

## Workflow

### 1. Establish context

- Read `dashboard/CURRENT-STATE.md`, `docs/ARCHITECTURE.md`,
  `docs/AI-AGENT-GUIDE.md`, and `infra/README.md` before substantial work.
- Read the relevant `docs/operations/` or `docs/integrations/` document when
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

Prefer the narrowest existing command or script. Use MCP tools when an MCP
server is connected and the task is an AI-facing database operation; otherwise
use the documented local CLI or script. Keep tool inputs explicit and bounded,
and use structured results rather than scraping human-formatted output when a
structured interface exists.

### 3. Make the change safely

- Keep implementation in `infra/`; do not put runtime code in this skill.
- Use `apply_patch` for source and documentation edits.
- Back up the database before schema or data migrations:
  `npm --prefix infra run db:backup`.
- Keep credentials in the documented environment or secret store. Never print,
  copy, or commit values from `infra/.env`, tokens, cookies, or private data.
- Treat `data/`, generated reports, backups, and nested repositories as separate
  boundaries.
- For external services, verify that the required credential is available and
  report it as unavailable instead of asking the user to paste a secret.

### 4. Verify proportionally

Run the narrowest relevant checks, then the repository checks required for the
change:

- General changes: `npm --prefix infra test`,
  `npm --prefix infra run typecheck`, and
  `npm --prefix infra run docs:check`.
- Database changes: relevant tests under `infra/tests/`, plus
  `npm --prefix infra run db:verify`.
- Platform changes: `npm --prefix infra run test:platform` and the relevant
  validation scripts under `infra/platform/`.
- MCP changes: `npm --prefix infra run test:mcp`.
- Go task-sync or notifier changes: `npm --prefix infra run test:go`.
- Python automation changes: `npm --prefix infra run test:python` and the
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
- Need durable operational policy or a runbook → update `docs/operations/` or
  the relevant documentation boundary, not this skill alone.
- Need a blank reusable document or artifact → copy from `templates/` into its
  owning workspace and leave the source template unchanged.
- Need to update learning progress → use the existing skills CLI or MCP tool;
  do not confuse database-tracked learning skills with this AI skill package.

## Handoff

Report the files changed, commands and tests run, important outputs or failures,
credential/service limitations, and any follow-up task. Do not commit or push
unless the user explicitly requests it.
