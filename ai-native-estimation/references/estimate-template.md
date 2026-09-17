# AI-Native Estimate Template

Use one record per bounded delivery slice. Keep the original estimate
immutable; add actuals after the work finishes.

## Estimate record

| Field | Value |
| --- | --- |
| Estimate ID | `<project>-<slice>-<date>` |
| Source/baseline | `<requirement, plan, or decision link and version>` |
| Owner/approver | `<accountable person>` |
| Prepared | `<date>` |
| Delivery tier | `visual mock / clickable prototype / sandbox pilot / production` |
| Target window | `<constraint, if any>` |
| Estimate status | `discovery / draft / committed / actualized` |
| Parallel capacity | `<agents, reviewers, environments, provider limits>` |
| Historical calibration | `<actual record or none>` |

## Scope contract

**Outcome:**

**In scope:**

**Out of scope:**

**Assumptions:**

**Acceptance and exit criteria:**

## Question rounds and completeness

Ask no more than eight high-impact questions per round. Record answers and
assumptions instead of repeatedly asking for the same context.

| Round | Purpose | Questions sent | Answer status | Blocking unknowns | Next action |
| --- | --- | --- | --- | --- | --- |
| 0 | `extract known evidence` | `<sources inspected>` | `confirmed / assumed / unknown` | `<...>` | `<...>` |
| 1 | `baseline` | `<scope, owner, tier, target, acceptance>` | `<...>` | `<...>` | `<...>` |
| 2 | `module contracts` | `<module-specific questions>` | `<...>` | `<...>` | `<...>` |
| 3 | `execution readiness` | `<data, access, environment, test, UAT, release>` | `<...>` | `<...>` | `<...>` |
| 4 | `critical blockers only, if needed` | `<...>` | `<...>` | `<...>` | `<...>` |

Use `CONFIRMED`, `ASSUMED`, `UNKNOWN`, or `BLOCKED` for each cell below. A
module is estimate-ready only when critical unknowns are answered or converted
into an owned wait state.

| Module | Scope | Contract/data | Owner | Access/environment | Test/UAT | Release | Completeness | Critical unknown or assumption |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<M-01>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<% or ready/not ready>` | `<...>` |

## Module map

Use one row per bounded business capability or technical boundary, not one row
per screen. Link each module to its contract, owner, acceptance evidence, and
readiness gate.

| Module | Outcome | In scope / out of scope | Inputs / outputs | Upstream / downstream | Owner | Acceptance evidence | Readiness gate | P50 | P80 | P95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `M-01` | `<user/business outcome>` | `<...>` | `<...>` | `<...>` | `<...>` | `<test/demo/metric>` | `SCOPE_READY` | `<...>` | `<...>` | `<...>` |

## Workstreams and parallel plan

Use one unit consistently within the estimate. Each O/M/P value means
optimistic / most likely / pessimistic. Separate effort from elapsed wait.

| ID | Module | Workstream | Input -> output | Wave | AI O/M/P | Human O/M/P | Verify/rework O/M/P | Can run with | Blocked by | Integration owner | Gate evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `W-01` | `M-01` | `contract / UX / backend / frontend / data / integration / test / ops` | `<...>` | `0` | `<...>` | `<...>` | `<...>` | `<workstream IDs>` | `<dependency IDs>` | `<person/team>` | `<test/demo/evidence>` |

For each task, calculate the transparent planning heuristic:

```text
expected lane value = (optimistic + 4 * most_likely + pessimistic) / 6
```

## Dependency graph

| Dependency | From | To | Type | Owner | Needed by | Status | Fallback or escalation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `D-01` | `<module/workstream>` | `<module/workstream>` | `data / decision / access / contract / environment / provider` | `<...>` | `<date or gate>` | `open / ready / blocked` | `<...>` |

## Wait-state ledger

Waiting is elapsed calendar time, not AI effort. Add only the non-overlapping
portion to the critical path and record work that remains unblocked.

| Wait ID | Module/workstream | State | Blocked task | Owner | Requested | SLA | Wait O/M/P | Unblock evidence | Work that can continue | Escalation date | Critical-path portion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `WT-01` | `<...>` | `WAIT_DATA / WAIT_BUSINESS_DECISION / WAIT_CONTRACT / WAIT_ACCESS / WAIT_ENVIRONMENT / WAIT_TEST_FIXTURE / WAIT_PROVIDER / WAIT_LEGAL_SECURITY / WAIT_REVIEW / WAIT_UAT / WAIT_RELEASE_APPROVAL / WAIT_REWORK` | `<...>` | `<...>` | `<date>` | `<hours/days>` | `<...>` | `<file/decision/access/test>` | `<workstream IDs>` | `<date>` | `<...>` | `open / absorbed / cleared / escalated` |

## Calendar model

| Wave | Parallel work | Capacity limit | Review/integration gate | Blocking dependency or wait | Expected elapsed |
| --- | --- | --- | --- | --- | --- |
| 0 | `<scope, data, design, or contract>` | `<agents/reviewers>` | `<decision>` | `<owner/date>` | `<...>` |
| 1 | `<backend/frontend/content/test lanes>` | `<agents/reviewers>` | `<review>` | `<wait ID>` | `<...>` |

**Critical path:** `<ordered modules, workstreams, waits, and gates>`

**Work that continues while waiting:** `<workstream IDs and why they are
unblocked>`

**Readiness milestones:**

| Milestone | Exit evidence | Modules/gates included | Target range | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| `M0 SCOPE_READY` | `<approved scope and acceptance>` | `<...>` | `<...>` | `<...>` | `<...>` |
| `M1 BUILD_READY` | `<contracts, access, environment, fixtures>` | `<...>` | `<...>` | `<...>` | `<...>` |
| `M2 INTEGRATION_READY` | `<integrated slice and automated checks>` | `<...>` | `<...>` | `<...>` | `<...>` |
| `M3 UAT_READY` | `<reviewer, data, scenarios, defect process>` | `<...>` | `<...>` | `<...>` | `<...>` |
| `M4 RELEASE_READY` | `<security, operations, recovery, approval>` | `<...>` | `<...>` | `<...>` | `<...>` |

**Human review capacity:** `<hours or days available per week>`

**Effort total:** `<AI + human + verification; do not confuse with elapsed>`

**Overlap-adjusted wait total:** `<elapsed wait on the critical path only>`

## Range and confidence

| Scope | P50 | P80 | P95 | Main driver |
| --- | --- | --- | --- | --- |
| `<module or overall delivery>` | `<...>` | `<...>` | `<...>` | `<critical module/wait/gate>` |

| Case | Calendar range | Meaning |
| --- | --- | --- |
| P50 | `<...>` | likely case if assumptions hold |
| P80 | `<...>` | normal planning/commitment range |
| P95 | `<...>` | contingency for material uncertainty |

**Confidence:** `high / medium / low`
**Why:** `<evidence and uncertainty drivers>`

**Range movers:** `<decision, dependency, scope, or quality change that moves the estimate>`

## Risks and gates

| Risk/gate | Trigger | Owner | Effect | Decision date |
| --- | --- | --- | --- | --- |
| `<provider/legal/security/etc.>` | `<what must happen>` | `<owner>` | `<time/scope effect>` | `<date>` |

## Actuals and calibration

Complete after delivery without overwriting the estimate above.

| Field | Actual |
| --- | --- |
| Started/finished | `<dates>` |
| AI execution time | `<...>` |
| Human decision/review time | `<...>` |
| Verification/rework time | `<...>` |
| External waiting time | `<...>` |
| Scope changes | `<...>` |
| Outcome | `<accepted, partial, or failed>` |
| Variance cause | `scope / dependency / agent / human / verification / rework / wait` |
| Calibration lesson | `<what changes next estimate>` |
