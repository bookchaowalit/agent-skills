---
name: ai-agent-workflows
description: Design and evaluate reliable AI agent workflows for Solo Empire, including agent loops, tool routing, structured outputs, memory, retrieval/RAG, evaluations, approvals, scheduled automation, and safe failure handling. Use when designing, improving, or reviewing how an agent reasons and routes work. Not for operating specific Solo Empire tools, MCP servers, CLI, or infra integrations — use ai-agents.
---

# AI Agent Workflows

Design agent workflows that are useful, observable, bounded, and easy to recover when a tool or model fails.

## Response language

All human-facing workflow output must be Thai by default, including plans,
errors, approvals, and handoffs. Preserve technical identifiers, commands,
paths, code, logs, and quoted source text exactly. Use another language only
when the user explicitly requests it for the requested output.

## Tool selection and context efficiency

Choose one best interface for the source and action before calling tools. Do
not call each available interface in sequence just to compare them. Switch only
when the chosen interface is unavailable, cannot perform the action, or returns
materially incomplete or unusable results.

For Solo Empire local data and deterministic operations, prefer the narrowest
existing CLI, script, or database query that returns bounded structured output
(`--json` when available). Prefer a purpose-built MCP/API when it is the direct
supported interface for the target service or gives a tighter schema,
permission boundary, or result scope. Tool order is a tie-breaker only after
checking source of truth, authorization, result shape, and the context each call
adds; CLI is not automatically cheaper than MCP.

For public current information, use Web Search and open only relevant pages.
Use browser UI for signed-in or site-specific interactions and repeatable
browser tests when no direct API, CLI, or MCP covers the task. Use screenshots
or Computer Use only for visual-only state.

Reduce context tokens by bounding fields, records, page text, and command output
before each call. Summarize relevant evidence instead of repeating full
responses, and avoid screenshots or full page trees when text is enough. This
limits context use but does not guarantee lower provider billing; tool schemas,
caching, and provider accounting vary by client.

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
- Keep first-party project work in `projects/`; keep hired/client repository boundaries in the client's own `bookchaowalit-freelance/<client>` repository; do not blur either with `infra/` or nested repositories.
- Preserve an audit trail for approvals, external writes, and important decisions without logging tokens, credentials, or private payloads.

## Solo Empire handoff

Report the files changed, workflow contract, approval points, tests run, known failure modes, and the next safe action. Update the owning documentation when the workflow changes repository behavior.
