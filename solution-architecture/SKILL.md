---
name: solution-architecture
description: Produce and review Solution Architect (SA) artifacts for Solo Empire systems — context and container architecture, tech-stack and ADR decisions, NFR targets, security and data boundaries, API and data-model TRDs, sequence diagrams, deployment topology, migration plans, and runbooks. Use when designing or documenting how a system is built, deployed, scaled, secured, or migrated, or when a docpack needs architecture, nfr-security, runbook, or trd-api-data documents.
---

# Solution Architecture

Turn requirements and existing code into a defensible, evidence-backed
architecture that delivery, operations, and the client can act on.

## Workflow

1. Read `dashboard/CURRENT-STATE.md`, `docs/ARCHITECTURE.md`,
   `systems/architecture/repository-boundaries.md`, and the system's rows in
   `repository-catalog/registries/runtime-boundaries.yaml` and
   `service-deployments.yaml`.
2. Inventory the as-built system from code: entry points, routes/controllers,
   models and migrations, integrations, config variable names, build and
   deploy files (Dockerfile, railway.toml, vercel.json, CI).
3. Model it: context diagram, containers/components, data stores, trust
   boundaries, deployment topology (mermaid flowchart/sequence/erDiagram).
4. Record decisions as ADR-xx (context, options, decision, consequences) using
   `templates/development-cycle/system-architecture-decision.md` when a
   standalone record is needed.
5. Set measurable NFR-xx targets (latency, availability, RPO/RTO, capacity,
   security controls, observability) with `templates/development-cycle/non-functional-requirements.md`;
   unknown targets become owner questions, not guesses.
6. For APIs and data, produce the TRD: endpoint table (method, path, auth,
   purpose), entity/ER model, integration contracts — see
   `templates/development-cycle/api-contract.md` and `technical-design.md`.
7. Write the runbook: environments, build/deploy, variable names, health
   checks, rollback, backup/restore, incident steps.
8. Review with `templates/positions/solution-architect/architecture-review-record.md`
   and hand security/privacy questions to `security-and-privacy`.

## Decision rules

- Describe the as-built system first; label target or proposed designs
  **[สมมติฐาน]** until approved.
- Hosting follows the recorded decision (Railway primary PaaS, Vercel for
  frontends) unless a client contract says otherwise; never invent a target.
- Secrets: variable names only, never values or provider IDs that grant access.
- Production changes, migrations, spending, or provider switches → explicit
  owner approval before acting; documents only describe the plan.

## Handoff

Report diagrams and ADRs produced, NFR targets with their source, open
architecture questions, risks (R-xx), and the verification run.
