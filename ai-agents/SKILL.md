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

- Read architecture guidance from `architecture-docs/docs/` (via
  `SOLO_ARCHITECTURE_ROOT` or `../architecture-docs`) and operational command
  ownership from `platform-ops-cli/README.md` (via `SOLO_OPS_ROOT` or legacy
  sibling `../ops-toolkit`). Neither checkout depends on the hub. Use focused
  `rg`/`sed` ranges rather than loading long documents.
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
| Tasks | Tasks API in `empire-platform` (`SOLO_PLATFORM_ROOT` or sibling `../empire-platform`); use its supported MCP/API interface or the `platform-ops-cli` task client |
| Health, skills, goals, projects, operational CLI | `platform-ops-cli/infra/cli.ts` and its owning services |
| Database schema or migration | the owning service/cell repository identified by architecture guidance; local SQLite task storage was retired |
| AI-facing tool or MCP behavior | `mcp-aggregator` (`SOLO_MCP_ROOT` or sibling `../mcp-aggregator`) |
| REST endpoint or client | the owning cell repository identified by architecture guidance; `infra/api/` was retired 2026-10-11 |
| Scheduled workflow or system automation | the `platform-ops-cli` checkout or the owning service repository |
| Kubernetes, GitOps, IaC, policies, onboarding | `bookchaowalit/platform-infra-kit` (ops-owned registries are in `platform-ops-cli/infra/platform/`) |
| Local services and homelab | `bookchaowalit/platform-homelab-infra` |
| System-wide verification | the checks documented by each owning repository |

Follow the tool-selection and context-efficiency policy in
`skills/ai-agent-workflows/SKILL.md`. Keep inputs explicit and bounded, and use
structured results rather than scraping human-formatted output when a
structured interface exists.

### 3. Make the change safely

- Keep implementation in its owning repository; do not put runtime code in this skill. Portable skills live in `agent-skills`.
- Use `apply_patch` for source and documentation edits.
- Follow the owning service repository's documented backup/restore procedure
  before schema or data migrations; the retired local SQLite backup command
  is unavailable.
- Keep credentials in the documented environment or secret store. Never print,
  copy, or commit values from the owning repository's `.env`, tokens, cookies,
  or private data.
- Treat `data/`, generated reports, backups, and nested repositories as separate
  boundaries.
- For external services, verify that the required credential is available and
  report it as unavailable instead of asking the user to paste a secret.

### 4. Verify proportionally

Run the narrowest relevant checks, then the repository checks required for the
change:

- General ops-toolkit changes: `task test`, `task typecheck`, and
  `task docs:check` from `platform-ops-cli`.
- Database changes: relevant checks from the owning service repository.
- Platform changes: `task test:platform` and the relevant
  validation scripts in `bookchaowalit/platform-infra-kit`.
- MCP changes: run the checks documented by `mcp-aggregator`.
- Python automation changes in ops-toolkit: `task test:python` and the
  focused test task listed in its Taskfile.

If a check cannot run because an external service, credential, or local daemon
is unavailable, record the exact limitation and do not hide the failure.

## Decision rules

- Need a new AI-facing capability → implement or extend an MCP tool in
  `mcp-aggregator`, then document its selection and safety rules here if it
  is reusable.
- Need a repeatable deterministic operation → implement or reuse a helper in
  the owning repository; do not embed it in `SKILL.md`.
- Need agent judgment, routing, or safety procedure → update this skill.
- Need durable operational policy or a runbook → update the relevant
  `architecture-docs/operations/` boundary, not this skill alone.
- Need a blank reusable document or artifact → copy from
  `architecture-docs/templates/` into its owning workspace and leave the
  source template unchanged.
- Need to update learning progress → use the existing skills CLI or MCP tool;
  do not confuse database-tracked learning skills with this AI skill package.

## Handoff

Report the files changed, commands and tests run, important outputs or failures,
commit/push/deploy evidence, credential/service limitations, and any follow-up
task. Follow the repository's automatic release closeout preference for scoped
Git and documented non-production deployment actions; retain approval gates for
production, destructive, paid, credential, and external-message actions.
