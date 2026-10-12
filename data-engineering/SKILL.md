---
name: data-engineering
description: Design, implement, review, and operate governed Solo Empire data products and lake-first pipelines. Use for source intake, ingestion, Parquet or Iceberg, schemas and contracts, quality, lineage, replay or backfill, access, retention, release, incidents, or deprecation; do not use for generic database CRUD or AI-agent orchestration without a data-product boundary.
---

# Data Engineering

Turn a data request into a bounded, replayable data product with explicit
ownership, contracts, quality evidence, lineage, and operating controls.

## Context routing

Role, process, learning, and workspace documents (`roles/`, `learning/`, `projects/`,
`knowledge/`, `quiz/`) live in the `bookchaowalit/knowledge-base` repository, not in
this one. Read them from that checkout (set
`SOLO_KNOWLEDGE_ROOT`; default is the `knowledge-base` sibling of this checkout); the relative paths below are relative to its root.
Data-lake code lives in `bookchaowalit/data-lake` (override `SOLO_DATA_LAKE_ROOT`).

- Always read [`roles/data-engineering/README.md`](../../roles/data-engineering/README.md)
  for the role boundary and gates.
- Read [`roles/data-engineering/PROCESS.md`](../../roles/data-engineering/PROCESS.md)
  for a new or changed data product, pipeline, release, incident, or retirement.
- Read [`roles/data-engineering/PROCESS-REGISTER.md`](../../roles/data-engineering/PROCESS-REGISTER.md)
  only when selecting subprocess artifacts or templates.
- Read [`systems/ai-data/data-lake-architecture.md`](../../systems/ai-data/data-lake-architecture.md)
  for ingestion, lake layers, storage, streaming, or downstream projections.

## Workflow

1. Define the consumer decision, measurable outcome, data owner, producer,
   consumers, grain, source permission, privacy class, retention, volume, and
   freshness. Stop if ownership, permission, or permitted use is unknown.
2. Select the smallest subprocess and copy only its required blank templates
   from `templates/roles/data-engineering/` into the owning data-product
   workspace; never edit a source template in place.
3. Preserve exact source bytes and checksum in immutable landing storage when
   the lake contract applies. Produce a versioned Bronze manifest before any
   SQLite, dashboard, API, MCP, analytics, or AI projection.
4. Version schemas and contracts. Make transforms deterministic, idempotent,
   bounded, observable, and safe to retry, quarantine, backfill, and replay.
   Never let a producer write directly into another application's operational
   store or silently discard invalid records.
5. Verify source-to-target reconciliation, quality thresholds, lineage,
   consumer compatibility, access, retention, recovery, cost, and rollback.
   A breaking contract change or production release requires accountable owner
   and affected-consumer approval.
6. Handoff the decision, artifacts, commands, evidence, exceptions, owners,
   approval points, rollback/replay path, and next review. Report missing
   controls as gaps instead of claiming readiness.

## Verification

Run the narrow data tests first, then repository checks when tracked files
change:

```bash
# data-lake code lives in bookchaowalit/data-lake; run its suite (see its README):
# cd "${SOLO_DATA_LAKE_ROOT:-../data-lake}" && for t in $(find infra/tests -name '*_test.py' | sort); do .venv/bin/python "$t" || echo "FAIL $t"; done
task contracts:check
task docs:check
```
