---
name: product-management
description: Own product and UX artifacts for Solo Empire systems — problem framing, personas, product vision, PRD with scope and prioritised features, success metrics, phased roadmap, screen inventory, user flows, and design-system notes. Use when defining what a product should do and for whom, writing or reviewing a PRD or roadmap, prioritising features, or producing UX flows and screen inventories; not for AI-specific delivery (ai-product-delivery) or detailed requirements and traceability (business-analysis).
---

# Product Management

Decide what to build, for whom, and how success is measured, and make the
user experience explicit enough to build and test.

## Workflow

1. Establish context: owner, users, current status, live evidence (usage,
   feedback, UAT findings, minutes) and the system's existing docpack.
2. Frame the problem: user pain, business outcome, constraints, non-goals.
3. Write the PRD (`01-prd.md` in the docpack or
   `templates/positions/product-manager/product-brief-and-roadmap.md`):
   personas, in/out scope, features with MoSCoW or P1/P2/P3 priority and
   phase, success metrics with baseline and target, assumptions, risks.
4. Roadmap: phases and milestones tied to outcomes; mark unapproved dates
   **[ต้องยืนยัน]**.
5. UX: build the screen inventory from actual routes/pages (ID, name, role,
   status) and draw the main user flows in mermaid; note design-system
   components in use. Use
   `templates/positions/ux-ui-designer/research-and-design-handoff.md` for a
   standalone design handoff.
6. Hand requirements detail and acceptance criteria to `business-analysis`,
   architecture to `solution-architecture`, and test design to `qa-testing`.

## Decision rules

- Prioritise by user outcome and evidence, not by feature count.
- Metrics need a baseline source or an explicit measurement plan.
- Pricing, contract scope, or client commitments are owner decisions; record
  them as open questions unless a signed record exists.
- Screens that exist only in design are labelled planned, not built.

## Handoff

Report the PRD version, prioritised scope, metrics, roadmap, screen/flow
coverage, open decisions, and who must approve them.
