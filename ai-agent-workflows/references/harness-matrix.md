# AI Harness Matrix

Solo Empire keeps one source of truth for rules, roles, and policy, then maps
it onto each harness's native features. Change the source, not the per-harness
copy.

| Source of truth | Purpose |
| --- | --- |
| `AGENTS.md` | Repository rules, language policy, delivery preference |
| `skills/<name>/SKILL.md` | Repository-owned workflows (mirrored to `.agents/skills`) |
| `.github/agents/roles.yaml` + `solo-*.agent.md` | Sub-agent roles and boundaries |
| `infra/scripts/agent/copilot_hooks.py` | Lifecycle policy engine |
| `skills/ai-agent-workflows/references/sub-agent-handoff.md` | Sub-agent handoff contract |

## Feature map

| Capability | Claude Code | Codex CLI | GitHub Copilot |
| --- | --- | --- | --- |
| Instructions | `CLAUDE.md` imports `@AGENTS.md` | `AGENTS.md` | `AGENTS.md` |
| Sub-agents | `.claude/agents/solo-*.md` (generated) | `.codex/agents/solo_*.toml` (generated) | `.github/agents/solo-*.agent.md` |
| Hooks | `.claude/settings.json` via `harness_hooks.py --harness claude` | `.codex/hooks.json` via `harness_hooks.py --harness codex` | `.github/hooks/solo-empire-lifecycle.json` |
| Destructive command | `ask` (human approval prompt) | `deny` (Codex has no hook `ask`) | `deny` |
| Secret paths | `deny` | `deny` | `deny` |
| Completion gate | `Stop` hook, honours `stop_hook_active` | `Stop` hook | `agentStop` hook |
| Headless loop dispatch | `task book-dev:dispatch:claude` (`claude -p`, tool allowlist) | `task book-dev:dispatch:codex` (`codex exec`, sandbox) | not a dispatch target |
| Profiles | project settings + local `settings.local.json` | `solo-audit` / `solo-write` profiles | role `tools` lists |
| UI design check | impeccable skill | impeccable hook | impeccable hook |

Roles: explorer, implementer, debugger, reviewer, security, data, and
ui-verifier. Only implementer and debugger can edit; the rest are read-only.

Codex loads project hooks only after the owner trusts each hook in an
interactive Codex session (Codex stores the reviewed hook hash). Re-review
after `.codex/hooks.json` changes. Never enable `bypass_hook_trust` to skip
that review. Copilot hooks need the Copilot CLI or cloud agent.

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
  then `task subagents:check`.
- After changing the policy engine or an adapter: `task test:agent`.
- Gate mode: `SOLO_EMPIRE_HOOK_GATE=focused` (default), `strict`, or `off`.
- Hook runtime records stay under `data/runtime/agent-hooks/` and are never
  committed. They hold event metadata only, never prompt text or command output.
