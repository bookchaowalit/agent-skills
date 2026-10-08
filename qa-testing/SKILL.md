---
name: qa-testing
description: Plan and evidence software quality for Solo Empire systems — test strategy, test levels, environments, test cases with expected results, entry/exit criteria, defect records, UAT scripts, and quality-gate evidence linked to requirements. Use when designing tests or UAT for a system, writing a test-uat document, assessing release readiness from test evidence, or reconciling test results with the RTM.
---

# QA and Testing

Make quality claims traceable: every priority requirement maps to a test,
every test to evidence, and every gap to an owner.

## Workflow

1. Read the system's requirements (SRS/FR-xx, user stories) and RTM, plus
   existing tests in the owning repository (unit, integration, E2E, smoke).
2. Run the existing suites when they are local and safe; record the command,
   date, and pass/fail counts as evidence. Never claim a run you did not do.
3. Write the test strategy: levels, scope per level, environments and data,
   tools, entry/exit criteria, defect severity and triage rules — base it on
   `templates/development-cycle/test-strategy.md` or
   `templates/positions/qa-test-engineer/quality-assurance-plan.md`.
4. Write TC-xx cases (precondition, steps, expected result, linked FR-xx,
   status, evidence) and a UAT script for business testers.
5. Record defects with `templates/development-cycle/defect-record.md` and
   update the RTM status column through `business-analysis`.
6. Check release readiness against `templates/development-cycle/quality-gate-pack.md`.

## Decision rules

- Distinguish developer retest, automated tests, client UAT, and business
  acceptance; only the client signs acceptance.
- Untested or blocked cases stay visible with a reason; never drop them.
- Production data or real payments in tests → stop for explicit approval.

## Handoff

Report suites run with results, TC coverage of priority requirements, open
defects by severity, UAT status, exit-criteria verdict, and next action.
