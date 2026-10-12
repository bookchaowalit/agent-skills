# Agent-stack trial — interim evaluation (5 tasks)

Stack under trial (frozen 2026-10-09 at 0f343a7b): Opus orchestrator; Haiku (medium) default worker;
Sonnet (medium) for debugger/reviewer and, in this trial, for security-relevant implementation;
Codex gpt-6.1-sol (high) as the independent reviewer of medium/high-risk change sets.
Evaluated 2026-10-12 after 5 real backlog tasks. Escaped defects are a lagging metric:
task #175 (due 2026-10-22) checks them. Treat everything below as trends, not rates.

## Per-task record

| Task | Tier | Workers | Wall time | Review | First pass | Notes |
|---|---|---|---|---|---|---|
| #86 market log | low, research | Haiku | ~8 min | orchestrator spot-check (4/4 URLs real) | accepted | 6 sources blocked (Upwork, Reddit, IH); reported honestly |
| #87 shortlist | low, analysis | Opus only | ~3 min | none | n/a | |
| #88 offer | low, writing | Opus only | ~6 min | owner delegated choice | n/a | |
| #173 evidence pack | medium, public regulatory text | Haiku draft, Opus review | ~5 min + later fix | orchestrator review, web check | **not accepted** | 3 fixes at review; a later source check found Article 50(2) and the provider/deployer split missing |
| #174 MCP in 22 repos | high, auth surface | Sonnet (phases 1, 3), Haiku ×2 (phase 2), Opus fixes | ~2.5 h | Codex ×2 (~16 min) | **not accepted** (both Sonnet phases) | Codex found 5 + 2 blocking; Haiku caught sync overwriting deploy files before commit; orchestrator once committed with a failing test |

Subagent tokens (approximate, from handoffs): Haiku research 130k; Haiku docs 78k; Haiku rollout 74k + 55k;
Sonnet implementation 70k + 86k (fix) and 214k + 231k (fix); Codex reviews 23k + 23k.

## Findings

1. **Speed.** Low-risk research and writing finish in minutes. The large task is dominated by fix rounds, not first drafts.
2. **Quality by tier.**
   - Haiku is reliable on mechanical, well-specified rollouts. It follows a step list, restores files the procedure did not expect to change, and reports 403s and skips accurately.
   - Haiku is weak on domain correctness when the brief does not force verification: it left regulatory claims unverified.
   - Sonnet produced working security-relevant code, but both phases had blocking issues (error leaks, identity-named fields, idempotency, an outbound-message path) that only the independent review caught.
3. **Review overhead.** Codex took ~16 min of ~150 min on #174 (~11%) and found 7 blocking defects. That is the clearest net benefit in the trial.
4. **Reliability.** Two process slips:
   - A Haiku worker committed one cell before its read check finished.
   - The orchestrator chained `pytest | tail` with `&&` and committed with a failing test.
   Both were caught the same day.
5. **Haiku vs Sonnet in the same tier.** No same-tier comparison yet. Haiku worked only on low/mechanical tasks and Sonnet only on high-risk code. Do not draw a model-quality conclusion from this.

## Recommendations (no stack change yet)

- Keep the frozen stack. Run tasks 6–10 before changing anything, and include at least one medium-risk coding task done by Haiku so the tiers can be compared.
- Keep the Codex gate mandatory for anything touching auth, tokens, or outbound messages.
- Briefs for regulatory or public-facing text must require the worker to verify claims against primary or official sources and to cite them.
- Gate commits on the test command's own exit code (`cmd; rc=$?; [ $rc -eq 0 ] && git commit ...`), never on a pipeline's tail.
