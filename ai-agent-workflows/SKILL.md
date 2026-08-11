---
name: ai-agent-workflows
description: Design, implement, and review reliable AI agent workflows for Solo Empire, including tool routing, structured outputs, memory, retrieval, evaluations, approvals, scheduled automation, and safe failure handling. Use when building or improving an agent that connects user requests to repository tools or external services.
---

# AI Agent Workflows

Design agent workflows that are useful, observable, bounded, and easy to recover when a tool or model fails.

## Response language

All human-facing workflow output must be Thai by default, including plans,
errors, approvals, and handoffs. Preserve technical identifiers, commands,
paths, code, logs, and quoted source text exactly. Use another language only
when the user explicitly requests it for the requested output.

## Core workflow

1. Establish context. Read the relevant current-state, architecture, and AI-agent guidance, then inspect the owning workspace and its git status.
2. Define the loop as request → plan → tool call → result → decision. State the expected input, output, owner, and stop condition for every step.
3. Route each action to the narrowest existing capability. Prefer an existing `infra/` CLI, MCP tool, script, database query, or documented workflow over inventing a parallel integration.
4. Bound the agent. Allowlist tools, validate arguments, cap records and time, make retries idempotent, and separate read-only actions from writes.
5. Add approval boundaries. Require explicit confirmation before sending messages, publishing content, changing production systems, spending money, or deleting/overwriting data.
6. Return a structured result with status, completed work, evidence or provenance, errors, and the next action. Never fill missing tool data with guesses.
7. Add only the memory needed for the job. Keep transient context separate from durable records, define retention, and never store secrets or unnecessary personal data.
8. Evaluate the workflow with happy-path, missing-credential, malformed-output, partial-failure, duplicate-request, timeout, and permission-denied cases.
9. Run the relevant tests and documentation checks, then record limitations and any unavailable external service.

## Decision rules

- Put deterministic, repeated logic in code or an `infra/` script; use the model for interpretation, prioritization, or language generation.
- Add an MCP surface when an AI agent needs a reusable capability with a clear schema; keep the underlying operation testable without the model.
- Treat uncertain, conflicting, or incomplete tool results as an explicit unknown and ask for clarification when it affects an external action.
- Keep first-party project work in `projects/`; keep hired/client repository boundaries in `engagements/`; do not blur either with `infra/` or nested repositories.
- Preserve an audit trail for approvals, external writes, and important decisions without logging tokens, credentials, or private payloads.

## Solo Empire handoff

Report the files changed, workflow contract, approval points, tests run, known failure modes, and the next safe action. Update the owning documentation when the workflow changes repository behavior.
