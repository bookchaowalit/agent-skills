---
name: solo-empire-operator
description: Operate, inspect, and improve the Solo Empire repository from short or vague requests. Use for repository-wide routing, infra health, CLI/MCP selection, documentation and workspace changes, AI agent workflows, RAG/LLM evaluation, token or cost optimization, MLOps/DevSecOps pipeline work, and safe verification or handoff.
---

# Solo Empire Operator

Use this as the repository-level router. Turn a short request into the
narrowest safe workflow, then delegate domain-specific judgment to the
matching skill instead of loading every document or inventing a new command.

## Operating loop

1. Read `dashboard/CURRENT-STATE.md` first. For code, infra, or agent work,
   also read `docs/ARCHITECTURE.md`, `docs/AI-AGENT-GUIDE.md`, and
   `infra/README.md`.
2. Inspect `git status --short`; preserve unrelated edits, generated files,
   backups, secrets, and nested repositories.
3. Classify the request as `inspect`, `operate`, `change`, or `plan`, and route
   it to the smallest existing CLI, script, MCP tool, document, or child skill.
   For a machine-readable pack, run `npm --prefix infra run agent:route --
   "<short request>" --json`.
   For one complete read-only decision, run `npm --prefix infra run
   agent:operator -- "<short request>" --json`.
   If the router returns `unknown` or `needs_clarification: true`, ask for the
   target domain before any side effect; never guess from the health route.
4. Build the loop as `request → context → plan → tool → evidence → verify →
   handoff`. Keep read-only checks separate from writes.
5. Ask for approval before external messages, publishing, production changes,
   spending, destructive operations, or any action requiring an unapproved
   credential.
6. Verify proportionally. For repository changes, run the required checks in
   the handoff and report exact warnings, unavailable services, and remaining
   gaps.

## Context and token policy

- Start with the current-state snapshot and a targeted `rg` search. Do not
  read the whole repository, all 45 workspaces, or all historical reports.
- Load only the relevant reference file from `references/infra-command-catalog.md`
  when a command route is needed; load domain docs only after classification.
- Prefer structured JSON, focused `sed` ranges, and test output over copying
  large files into context. Summarize evidence instead of repeating source.
- Use deterministic code for routing, validation, retries, idempotency, and
  cost limits; use the model for interpretation, prioritization, and language.
- Never claim that token accounting, prompt caching, model routing, or hosted
  LLM deployment exists unless the repository evidence shows it. The current
  central MLOps pipeline is a local/provider-neutral candidate lifecycle.
- For an AI feature, define a context budget, model/fallback policy, maximum
  output, latency/cost target, evaluation set, redaction rule, and rollback
  path. If those are not implemented, record them as gaps rather than hiding
  them in the prompt.
- Record provider usage through `npm --prefix infra run agent:telemetry -- ...`
  only after the provider returns usage metadata. Keep the prompt and response
  out of telemetry.
- Use `npm --prefix infra run agent:model -- ...` to build a provider-neutral
  routing plan. Abstract `fast`, `balanced`, and `quality` slots can be mapped
  to a provider later; the repository currently selects the local reference
  adapter because no external provider adapter is configured.
- Use `npm --prefix infra run agent:cache -- --stats --json` to inspect cache
  counters. The cache stores hashed keys and explicitly allowed
  `public/internal` results only; private or restricted data is never cached.
- Use `npm --prefix infra run agent:local -- "..." --json` for a deterministic
  local pipeline smoke run. It demonstrates routing, cache, token estimates,
  and telemetry without pretending to be hosted LLM generation.
- The operator façade now includes a bounded context pack from the routed files:
  `npm --prefix infra run agent:operator -- "..." --json`. The pack is capped
  by file/line/byte budgets, redacts credential-shaped values, and never loads
  sensitive paths such as `.env` or credentials directories.

## Routing map

- Agent/tool/MCP/RAG/memory/evaluation workflow → `ai-agents` or
  `ai-agent-workflows`.
- AI application/API/automation delivery → `ai-product-delivery`.
- Security, secrets, permissions, privacy, or boundary review →
  `security-and-privacy`.
- Client, lead, content, or proposal work → the matching business skill.
- New reusable agent procedure → `skill-creator`, then keep the implementation
  in `infra/` and the reusable instruction in `skills/`.

The deterministic router has explicit specialist routes for `ai-product`,
`security`, `external-integrations`, `crm`, `proposals`, `content`,
`business-analysis`, and `business`, in addition to health, AI pipeline, data
lake, database, documentation, and infra. Unmatched requests use an
`unknown` route with low confidence and a clarification stop condition.

## Safe completion

Return: outcome, files changed, commands/tests run, evidence, approval points,
known failures or service limitations, and the next safe action. Do not commit
or push unless explicitly requested. Do not log secrets or raw private
payloads. Read `references/infra-command-catalog.md` for the command matrix and
pipeline sequence.
