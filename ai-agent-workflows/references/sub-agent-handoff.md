# Sub-agent Handoff Contract

The main agent owns planning, delegation, integration, final verification, and release approval. A sub-agent owns only the bounded role named in its handoff.

## Envelope

Every sub-agent returns one JSON object with this contract:

```json
{
  "contract": "solo-empire.subagent-handoff.v1",
  "role": "explorer|implementer|debugger|reviewer|security|data|ui-verifier",
  "status": "complete|blocked|needs_parent",
  "scope": "short description of the assigned slice",
  "summary": "one concise outcome",
  "files_read": ["workspace-relative/path"],
  "files_changed": ["workspace-relative/path"],
  "evidence": ["short evidence statements"],
  "tests": [{"command": "exact command", "status": "passed|failed|skipped", "notes": "brief result"}],
  "risks": ["remaining risk"],
  "blockers": ["unresolved blocker"],
  "next_action": "single safe action for the parent"
}
```

The JSON must not contain credentials, tokens, cookies, raw private payloads, or a copied transcript. Use workspace-relative paths and exact commands. An empty array is valid when a field has no entries.

## Role fields

- `explorer`: `findings`, `relevant_paths`, `hypothesis`, `recommended_change`
- `implementer`: `implementation`, `verification`
- `debugger`: `reproduction`, `hypothesis`, `root_cause`, `fix`, `verification`
- `reviewer`: `findings`, `disposition`, `residual_risks`
- `security`: `findings`, `exposure_paths`, `disposition`
- `data`: `findings`, `contracts_checked`, `disposition`
- `ui-verifier`: `observations`, `reproduction`, `disposition`

Security findings name the exposed path and kind of exposure, never the secret value. Reviewer, security, and data findings should include `severity`, `path`, `line` when available, `impact`, and `recommendation`. Verification entries must distinguish a passed check from an unavailable or skipped check.

## Stop conditions

Return `blocked` or `needs_parent` when the scope is ambiguous, required access is unavailable, evidence conflicts, an external action needs approval, or the change would cross a repository/data boundary. Do not guess missing tool results.
