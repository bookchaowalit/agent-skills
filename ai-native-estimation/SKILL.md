---
name: ai-native-estimation
description: Estimate AI-assisted project delivery by decomposing modules, staging readiness questions, planning parallel workstreams, separating effort from human and external waits, modeling critical paths, uncertainty, and actual-vs-estimate calibration.
---

# AI-Native Estimation

Estimate delivery time for work where AI agents generate code, tests, content,
or analysis and humans still own scope, decisions, review, acceptance, and
external dependencies. Use this after a requirement or implementation plan is
clear enough to decompose, and before making a date commitment.

This skill complements business analysis, client proposals, product delivery,
Superpowers planning, and Impeccable UI work. It does not replace legal,
finance, security, product, or delivery-owner approval.

## Inputs

Gather the smallest useful evidence before estimating:

- outcome, users, scope, non-goals, and target delivery level;
- approved requirements or implementation plan, repository state, and known tests;
- team roles, human availability, agent/model/tool setup, and safe parallel capacity;
- quality bar, environments, release or pilot acceptance criteria;
- external dependencies, approval gates, provider readiness, and waiting time;
- prior estimates and actuals from comparable work, when available.

If the target or acceptance bar is missing, produce a discovery range and list
the decisions required before calling it a delivery estimate.

## Module-first protocol

Treat a module as a bounded business capability or technical boundary with its
own outcome, contract, owner, acceptance evidence, dependencies, and readiness
state. Do not use screen count or repository count as the module list.

For each module, create an inventory row and decompose it into independent
workstreams such as scope/contract, UX/content, backend/API, frontend/mobile,
data/migration, integration, test/fixtures, and operations/release. Every
workstream must state its input, output, dependency, owner, AI execution, human
gate, verification, and what can continue if another workstream is waiting.

Use this question protocol before making a committed estimate:

1. **Round 0 - extract.** Read the available requirements, plans, repository,
  tests, and decisions. Mark each needed fact `CONFIRMED`, `ASSUMED`,
  `UNKNOWN`, or `BLOCKED`; do not ask for facts already evidenced.
2. **Round 1 - baseline.** Ask for outcome, users, in/out scope, delivery tier,
  target window, accountable owner, acceptance bar, and non-negotiables.
3. **Round 2 - module contracts.** Ask only module-specific gaps: input/output,
  states and roles, data ownership, API or provider contract, security/legal
  constraints, test evidence, and upstream/downstream dependencies.
4. **Round 3 - execution readiness.** Ask who supplies data and decisions, when
  access/environment/test fixtures/UAT reviewers will be ready, the response
  SLA, release approvals, and what work is allowed while waiting.
5. **Stop or escalate.** Produce the estimate after Round 3 if critical fields
  are confirmed or explicitly assumed. Ask a fourth round only for unresolved
  critical blockers, and convert each unresolved answer into a wait-state
  risk with an owner, SLA, and escalation date.

Ask questions in batches of no more than eight high-impact questions per round.
Every question must map to a module, decision, dependency, or wait state. Show
question completeness and the assumptions that remain; never hide missing
answers inside a padded duration.

### Parallel execution and waiting

Parallel AI work is valid only when the workstreams have stable inputs, no
unowned write conflict, available review/integration capacity, and an explicit
integration owner. Assign work to waves and cap simultaneous work by the
available agents, human reviewers, environments, and provider rate limits.
Use `max()` for independent parallel work, then add sequential gates; do not
sum all AI task durations as if they were serial.

Track waiting as elapsed calendar time, separate from effort. Use explicit
states such as `WAIT_DATA`, `WAIT_BUSINESS_DECISION`, `WAIT_CONTRACT`,
`WAIT_ACCESS`, `WAIT_ENVIRONMENT`, `WAIT_TEST_FIXTURE`, `WAIT_PROVIDER`,
`WAIT_LEGAL_SECURITY`, `WAIT_REVIEW`, `WAIT_UAT`, `WAIT_RELEASE_APPROVAL`,
and `WAIT_REWORK`. For each state record the blocked work, owner, request date,
SLA, O/M/P duration, unblock evidence, escalation date, and work that can
continue. Add a wait to the critical path only for its non-overlapping portion;
show parallel work that absorbs it instead of double-counting it.

Use module readiness gates: `SCOPE_READY`, `BUILD_READY`,
`INTEGRATION_READY`, `UAT_READY`, and `RELEASE_READY`. A module is not
complete when code exists; it is complete when its current gate has acceptance
evidence and no unowned critical wait.

## Workflow

1. **Baseline the scope.** Record the source, version/date, delivery tier,
   assumptions, non-goals, and owner. Treat new requirements as change risk,
   not invisible buffer.
2. **Build the module map.** List bounded modules, their contracts, owners,
   acceptance evidence, readiness gates, upstream/downstream dependencies, and
   question completeness. Decompose each module into testable vertical slices
   and parallel workstreams.
3. **Classify execution and waits.** Mark separate lanes for AI execution,
   human decision/review, verification/rework, integration, and external
   waiting. Assign waves, concurrency limits, wait owners, SLAs, escalation
   dates, and work that remains unblocked.
4. **Use three-point estimates.** For each module and workstream, capture
   optimistic, most likely, and pessimistic values with one unit. Use
   `E = (O + 4M + P) / 6` as a transparent planning heuristic, not as
   statistical certainty.
5. **Model calendar time.** Group independent tasks into waves, identify the
   critical path through module gates, add integration/UAT/release work, and
   constrain the result by human review capacity and waiting SLAs. Do not sum
   parallel agent work as sequential time.
6. **Add uncertainty explicitly.** Separate effort from elapsed calendar time,
   dependency wait, approval wait, scope volatility, and expected rework. Show
   module-level P50/P80/P95 before rolling up the overall range.
7. **Report ranges.** Give P50, P80, and P95 calendar ranges, confidence level,
   assumptions, risks, dependency owners, readiness milestones, and the
   condition that would move the estimate. Call ranges heuristic when there is
   not enough historical data.
8. **Calibrate after delivery.** Record actual AI time, human time, wait time,
   rework, scope changes, and outcome against the original estimate. Explain
   variance before changing the next estimate.

Use `references/estimate-template.md` for the output shape.

## Delivery tiers

- **Visual mock:** static visual direction; no reliable behavior or integration.
- **Clickable prototype:** representative navigation, states, content, and
  responsive behavior; data and integrations may be mocked.
- **Sandbox pilot:** a bounded end-to-end slice that users can test with
  synthetic data or provider sandboxes, explicit limits, and a test environment.
- **Production release:** real data, security, operations, monitoring,
  recovery, support, provider contracts, and business acceptance.

Never use a prototype estimate as a production commitment. A sandbox pilot
must state what is simulated and what is deliberately disabled.

## Decision rules

- Unclear scope or acceptance → estimate discovery first; do not invent precision.
- UI-only work → estimate states, content, responsive behavior, accessibility,
  review, and test coverage, not just the number of screens.
- AI can reduce generation time → retain human review, integration, verification,
  debugging, and rework unless evidence shows they are unnecessary.
- Parallel work is valid only when dependencies, branch/review capacity, and
  integration ownership are available.
- Identity, financial, regulated, legal, or provider work → model approval and
  external wait as explicit gates; AI execution time is not the whole timeline.
- P50 is a likely planning case, P80 is the normal commitment range, and P95 is
  contingency. Do not label these statistically calibrated without actual data.
- A deadline set by someone else is a constraint to test against capacity, not
  evidence that the work fits.
- Scope changes after baseline → show the delta and re-estimate; do not hide it
  inside the original range.
- External communication, commercial commitment, production action, or regulated
  behavior → keep the estimate draft until the accountable owner approves it.

## Integration

- Use `business-analysis` for requirements, acceptance criteria, traceability,
  and change control before estimating a committed baseline.
- Use `client-discovery-and-proposals` when the estimate becomes a proposal,
  price, statement of work, or client commitment.
- Use `ai-product-delivery` for architecture, evaluation, rollout, security,
  and operational readiness after the delivery slice is selected.
- Use Superpowers brainstorming and writing-plans to produce the decomposed work
  input; use this skill to estimate it and calibrate the result.
- Use Impeccable for UI/UX quality and visual scope; do not treat visual polish
  as free work or let it silently expand the delivery tier.

## Calibration record

Create an estimate record before work starts and preserve the original values.
After completion, append actuals and classify variance as scope, dependency,
tool/agent execution, human review, verification, rework, or waiting. Do not
store raw prompts, secrets, private payloads, or provider credentials in the
record. Use the owning project or engagement evidence boundary.