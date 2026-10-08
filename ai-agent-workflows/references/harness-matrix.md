# AI Harness Matrix

Solo Empire keeps one source of truth for rules, roles, and policy, then maps
it onto each harness's native features. Change the source, not the per-harness
copy.

| Source of truth | Purpose |
| --- | --- |
| `AGENTS.md` | Repository rules, language policy, delivery preference |
| `skills/<name>/SKILL.md` | Repository-owned workflows (linked into `.agents/skills` and `.claude/skills` by `task skills:link`) |
| `.github/agents/roles.yaml` + `solo-*.agent.md` | Sub-agent roles and boundaries |
| `infra/scripts/agent/copilot_hooks.py` | Lifecycle policy engine |
| `skills/ai-agent-workflows/references/sub-agent-handoff.md` | Sub-agent handoff contract |

## Feature map

| Capability | Claude Code | Codex CLI | GitHub Copilot | Gemini CLI |
| --- | --- | --- | --- | --- |
| Instructions | `CLAUDE.md` imports `@AGENTS.md` | `AGENTS.md` | `AGENTS.md` | `.gemini/settings.json` `context.fileName: ["AGENTS.md"]` |
| Skills | `.claude/skills/` (local links), role `skills` preload | `.agents/skills/` (local links) | CLI: `.github/skills/`, `.agents/skills/`, `.claude/skills/`; verify cloud/IDE discovery separately | `.agents/skills/` (local links) |
| Sub-agents | `.claude/agents/solo-*.md` (generated) | `.codex/agents/solo_*.toml` (generated) | `.github/agents/solo-*.agent.md` | `.gemini/agents/solo-*.md` (generated) |
| Sub-agent model | `claude_model`/`claude_effort` in `roles.yaml`: `haiku` + `medium` for explorer/data/ui-verifier; other roles inherit the orchestrator (Opus); briefs follow `subagent-orchestration` | profile default | client default | client default |
| Hooks | `.claude/settings.json` via `harness_hooks.py --harness claude` | `.codex/hooks.json` via `harness_hooks.py --harness codex` | `.github/hooks/solo-empire-lifecycle.json` | `.gemini/settings.json` via `harness_hooks.py --harness gemini` |
| Project MCP | `.mcp.json` (`solo-empire`, approval per server) | user `~/.codex/config.toml` from setup | client config | `.gemini/settings.json` `mcpServers` |
| Destructive command | `ask` (human approval prompt); `allow` in `bypassPermissions` unless `SOLO_EMPIRE_HOOK_BYPASS=enforce` | `deny` (Codex has no hook `ask`) | `deny` | `deny` (`BeforeTool` has no `ask`) |
| Secret paths | `deny`; `allow` in `bypassPermissions` unless `SOLO_EMPIRE_HOOK_BYPASS=enforce` | `deny` | `deny` | `deny` |
| Completion gate | `Stop` hook, honours `stop_hook_active` | `Stop` hook | `agentStop` hook | `AfterAgent` hook (`deny` retries the turn) |
| Headless loop dispatch | `task book-dev:dispatch:claude` (`claude -p`, tool allowlist) | `task book-dev:dispatch:codex` (`codex exec`, sandbox) | not a dispatch target | not a dispatch target |
| Profiles | project settings + local `settings.local.json` | `solo-audit` / `solo-write` profiles | role `tools` lists | role `tools` lists |
| UI design check | impeccable skill | impeccable hook | impeccable hook | not wired |

Roles: explorer, implementer, debugger, reviewer, security, data, and
ui-verifier. Only implementer and debugger can edit; the rest are read-only.
Copilot role sources opt into repository instructions with
`include-custom-instructions: true`. Claude preloads the registry's skill list
without enabling persistent memory writes. The main agent owns diary, durable
memory updates, final verification, and release actions.

Codex uses a read-only sandbox for audit roles. Claude hooks recognize native
`agent_type` metadata and limit audit-role shell calls to a narrow inspection
allowlist; verification scripts and browser runners go through the parent.
Gemini explicitly loads `infra/scripts/agent/policies/gemini-read-only.toml`
through `policyPaths`, denying shell and file-mutation tools to audit roles.
Workspace `.gemini/policies` auto-discovery is disabled in the current native
implementation; placing a file there alone is not enforcement. Verify policy
loading on the installed Gemini version before claiming native enforcement.

Skill discovery folders are gitignored, machine-local symlinks to `skills/`.
Run `task skills:link` after cloning or after adding or removing a skill
(`infra/scripts/setup/setup.sh` runs it too); `task skills:link:check` reports
missing, stale, or orphaned links. Nothing is copied, so `skills/` stays the
only source.

Gemini CLI fingerprints project hooks and warns before running new or changed
ones; review `.gemini/settings.json` hooks after each change. Gemini sets
`CLAUDE_PROJECT_DIR` as a compatibility alias, but it reads only
`.gemini/settings.json`, so the policy still runs once per harness.

Codex loads project hooks only after the owner trusts each hook in an
interactive Codex session (Codex stores the reviewed hook hash). Re-review
after `.codex/hooks.json` changes. Never enable `bypass_hook_trust` to skip
that review. Copilot hooks need the Copilot CLI or cloud agent.

Copilot CLI also loads `.claude/settings.json` hooks and runs them in
PowerShell on Windows, while Claude Code runs them in bash. The Claude hook
commands are therefore a single-quoted `python3 -c` program that parses in
both shells and exits quietly when `CLAUDE_PROJECT_DIR` is unset, so the
policy runs once per harness instead of twice under Copilot.

Grok is a dispatch target through `task book-dev:dispatch:grok`. Qoder reads
the same instructions through `.qoder/README.md`.
Grok dispatch uses `--no-subagents`; its support level differs from the four
native role mappings above.

## Engineering loop

```text
book-dev:loop (deterministic scan) → execution ticket
  → book-dev:dispatch:{grok,codex,claude}
  → supported harness hooks + native roles (Grok: no sub-agents)
  → focused checks → commit → push → documented deploy → evidence
```

## Maintenance

- After changing `roles.yaml` or a Copilot agent body: `task subagents:sync`,
  then `task subagents:check` (regenerates Claude, Codex, and Gemini agents).
- After adding, renaming, or retiring a skill: `task skills:link`.
- After changing the policy engine or an adapter: `task test:agent`.
- CI runs `task test:agent` and the offline shared evaluation on Linux and Windows.
- Gate mode: `SOLO_EMPIRE_HOOK_GATE=focused` (default), `strict`, or `off`.
- Hook runtime records stay under `data/runtime/agent-hooks/` and are never
  committed. They hold event metadata only, never prompt text or command output.

## Context, evaluation, and actual handoffs

The operator prioritizes the routed child skill and required contracts inside
the existing context budget. `context_selections` select Markdown sections or
line ranges; each included file reports source ranges in `provenance`.
`required_context_missing` and `summary.required_context_complete` distinguish
partial context from a complete input. A missing required contract is a reason
to read the named source before execution, not to silently increase the budget.

Run `task agent:evaluate -- --json` for local contract checks. This calls shared
implementations with synthetic inputs and temporary hook state, never providers.
The offline entrypoint does not load live configuration or open the database.
Its timings measure local checks, not model latency or intelligence.

Run `task agent:evaluate -- --cases` to export six shared synthetic tasks for
Claude, Codex, Copilot, and Gemini. A separately approved native run can submit
observations using `task agent:evaluate -- --runs-file /absolute/run.json --json`.
The file is a bounded JSON list of records with `harness`, semantic `version`,
`run_id`, and `cases`. Every case supplies `id` and structured `output`;
`latency_ms` is optional. `total_tokens` is optional and must come from actual
usage metadata. Missing, duplicate, unknown, or incorrect cases fail. Unknown
usage stays `null`. Reports omit outputs and hash run identifiers.

Submitted scores have `evidence_level: submitted_observations` and
`native_execution_verified: false`: the evaluator cannot establish their
provenance. Never present a fixture score as a provider-backed quality result.
Provider runs retain their existing approval, privacy, and spending boundaries.

Before integrating a child's report, run
`task subagents:handoff:check -- --handoff-file /absolute/handoff.json --role reviewer`.
The validator checks the actual envelope, role-specific fields, test statuses,
workspace-relative paths, and empty `files_changed` for read-only roles. It
returns only validation metadata and exits nonzero for an invalid payload.
Native `subagentStop` reminders alone do not prove that this check happened.

Native references: [Claude hooks](https://code.claude.com/docs/en/hooks),
[Claude skill preloading](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents),
[Copilot CLI customization](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference),
[Gemini policies](https://geminicli.com/docs/reference/policy-engine/), and
[Gemini settings](https://geminicli.com/docs/reference/configuration/).
