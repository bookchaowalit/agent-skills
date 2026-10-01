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
| Skills | `.claude/skills/` (local links) | `.agents/skills/` (local links) | `.github/skills/` | `.agents/skills/` (local links) |
| Sub-agents | `.claude/agents/solo-*.md` (generated) | `.codex/agents/solo_*.toml` (generated) | `.github/agents/solo-*.agent.md` | `.gemini/agents/solo-*.md` (generated) |
| Hooks | `.claude/settings.json` via `harness_hooks.py --harness claude` | `.codex/hooks.json` via `harness_hooks.py --harness codex` | `.github/hooks/solo-empire-lifecycle.json` | `.gemini/settings.json` via `harness_hooks.py --harness gemini` |
| Project MCP | `.mcp.json` (`solo-empire`, approval per server) | user `~/.codex/config.toml` from setup | client config | `.gemini/settings.json` `mcpServers` |
| Destructive command | `ask` (human approval prompt) | `deny` (Codex has no hook `ask`) | `deny` | `deny` (`BeforeTool` has no `ask`) |
| Secret paths | `deny` | `deny` | `deny` | `deny` |
| Completion gate | `Stop` hook, honours `stop_hook_active` | `Stop` hook | `agentStop` hook | `AfterAgent` hook (`deny` retries the turn) |
| Headless loop dispatch | `task book-dev:dispatch:claude` (`claude -p`, tool allowlist) | `task book-dev:dispatch:codex` (`codex exec`, sandbox) | not a dispatch target | not a dispatch target |
| Profiles | project settings + local `settings.local.json` | `solo-audit` / `solo-write` profiles | role `tools` lists | role `tools` lists |
| UI design check | impeccable skill | impeccable hook | impeccable hook | not wired |

Roles: explorer, implementer, debugger, reviewer, security, data, and
ui-verifier. Only implementer and debugger can edit; the rest are read-only.

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

## Engineering loop

```text
book-dev:loop (deterministic scan) → execution ticket
  → book-dev:dispatch:{grok,codex,claude}
  → harness session with shared hooks + sub-agents
  → focused checks → commit → push → documented deploy → evidence
```

## Maintenance

- After changing `roles.yaml` or a Copilot agent body: `task subagents:sync`,
  then `task subagents:check` (regenerates Claude, Codex, and Gemini agents).
- After adding, renaming, or retiring a skill: `task skills:link`.
- After changing the policy engine or an adapter: `task test:agent`.
- Gate mode: `SOLO_EMPIRE_HOOK_GATE=focused` (default), `strict`, or `off`.
- Hook runtime records stay under `data/runtime/agent-hooks/` and are never
  committed. They hold event metadata only, never prompt text or command output.
