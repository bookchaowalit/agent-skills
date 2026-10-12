# Solo Empire Infra Command Catalog

Use this as a route lookup. Run commands from the repository root. Prefer the
narrowest check that answers the request; do not run all portfolio labs by
default.

## Context routes

| Need | Read first |
|---|---|
| Current state | `dashboard/CURRENT-STATE.md` |
| Architecture or boundary | `docs/ARCHITECTURE.md`, `docs/AI-AGENT-GUIDE.md` |
| Infra inventory | `infra/README.md` |
| Workspace location | `docs/WORKSPACE-STRUCTURE.md`, `docs/WORKSPACE-LOCATION-MAP.md` |
| New ingress/import | `systems/ai-data/data-lake-architecture.md`, `learning/platform-engineering/app-cli-data-lake-playbook.md` |
| AI/RAG/MLOps | `systems/ai-data/central-mlops-devsecops-pipeline.md`, matching `operations/` runbook |
| Documentation change | `docs/governance/DOCUMENTATION-STANDARDS.md`, `docs/governance/DOC-MAINTENANCE.md` |
| External identity | `accounts/README.md`, `accounts/ACCOUNT-REGISTRY.md` |

## Short-request route matrix

| Request shape | Route / specialist | First boundary |
|---|---|---|
| AI app, chatbot, AI feature | `ai-product` / `ai-product-delivery` | architecture + evaluation + security |
| Secret, permission, privacy, vulnerability | `security` / `security-and-privacy` | security audit + secret health |
| Gmail, GitHub, Jira, OAuth, webhook | `external-integrations` / `ai-agents` | MCP reference + credential status |
| Lead, CRM, outreach, sales | `crm` / `lead-research-and-crm` | CRM CLI + evidence rules |
| Proposal, SOW, scope, pricing | `proposals` / `client-discovery-and-proposals` | discovery + proposal boundary |
| Content, SEO, social, newsletter | `content` / `content-distribution` | content calendar + approval state |
| Pixiu Watch / Search Console / Ahrefs report | `client-seo` / `content-distribution` | `seo:report` monthly pack; no live-site fixes |
| Requirements, UAT, acceptance criteria | `business-analysis` / `business-analysis` | role process + traceability |
| Unmatched or ambiguous request | `unknown` / `solo-empire-operator` | clarify before side effects |

## Read-only health and orientation

```bash
git status --short
python3 infra/scripts/utils/system_health.py --quick
task health
task dashboard
task tasks
npx tsx infra/cli.ts skills
npx tsx infra/cli.ts projects
task agent:route -- "เช็กระบบและ AI pipeline" --json
task agent:operator -- "เช็กระบบและ AI pipeline" --json
task agent:context -- \
  dashboard/CURRENT-STATE.md docs/ARCHITECTURE.md --max-lines 80 --json

# Thin human-facing facade over the same Task boundary
./empire status
./empire doctor
./empire db migrate
./empire agent run "เช็กระบบและ AI pipeline" --json
```

Use `python3 infra/scripts/utils/system_health.py --quick` for a compact live
health signal. Use `npx tsx infra/cli.ts health` when the business-health
breakdown is needed.

## Verification ladder

Run the smallest applicable group, then the repository baseline for changes:

```bash
task test
task typecheck
task docs:check
task task:parity
task task:ownership -- --json
```

Focused checks:

```bash
task test:mcp
task test:database
# data-lake suite: run the tests in bookchaowalit/data-lake (see its README)
task test:python
task test:go
task test:platform
task test:workspace
task test:automation
task test:analytics
task test:seo-report
python3 infra/tests/security/security_test.py
```

Do not describe a check as passed when a credential, external service, or
optional daemon caused it to be skipped.

## Database and operational writes

```bash
task db:backup
task db:verify
task db:migrate
./empire db backup
./empire db verify
python3 infra/scripts/cli/ledger-cli.py clients
task media:stock -- --list --json
task media:stock -- "japanese temple" --json
task media:stock -- "japanese temple" --apply --limit 3
task media:stock -- --pack editor --apply
task catalog:art-pack -- --pack botanical-patterns --apply
task seo:report -- --json
task auth:google-search-console
task seo:report -- fetch --month 2026-08 --json
task seo:report -- fetch --month 2026-08 --apply --json
task seo:report -- report --month 2026-08 --gsc export.zip --ahrefs ahrefs.json --json
task seo:report -- report --month 2026-08 --gsc export.zip --ahrefs ahrefs.json --apply --json
task tasks
task tasks -- add --title "..."
task tasks -- update <id> --status in_progress
task tasks -- done <id>
task tasks -- sync
```

Back up before schema or migration changes. `dashboard/TASKS.md` is a
generated view; the task database/provider is canonical. Do not update a
generated dashboard file directly.

## MLOps/AI pipeline

The current pipeline is a local reference lifecycle, not hosted LLM
production. It covers candidate training, deterministic evaluation, local
registration, categorical drift monitoring, and manual promotion semantics.

```bash
python3 <mlops checkout>/infra/scripts/mlops/evaluate.py --json
python3 <mlops checkout>/infra/scripts/mlops/pipeline.py \
  --output-dir "$(mktemp -d)" \
  --registry-dir "$(mktemp -d)" \
  --json
python3 <mlops checkout>/infra/tests/mlops/mlops_pipeline_test.py
task agent:telemetry -- \
  --route ai-pipeline --provider example --model example-model \
  --input-tokens 900 --output-tokens 100 --token-budget 1200 \
  --input-rate-per-1k 0.15 --output-rate-per-1k 0.60 --record --json
task agent:telemetry -- --stats --stats-days 30 --json
task agent:model -- \
  "ทำให้ AI pipeline ประหยัด token" --operation change --token-budget 6000 --json
task agent:cache -- --stats --json
task agent:local -- \
  "ตรวจ AI pipeline แบบ local" --no-cache --json
```

For a real LLM/RAG change, additionally require:

```text
lake/source evidence → versioned dataset → prompt/model candidate
→ deterministic/offline eval → security/dependency gates
→ cost/latency/quality evidence → human promotion → runtime monitoring
```

The repository now provides a provider-neutral telemetry contract, an
idempotent local ledger, an abstract model-routing policy, a privacy-aware
prompt/result cache, and a deterministic local adapter boundary. These cover
counts, budget, cost estimate, cache hit, route, prompt version, and fallback
evidence without a provider call. It still does not provide hosted model
generation, provider failover, hosted model registry, or automatic production
rollback. Record real provider usage only after the provider adapter returns
usage metadata; never put prompt or response text in telemetry or cache
metadata.

## CI and security gates

```bash
task lint:secrets
task lint:paths
task contracts:check
task docs:check
```

Inspect `.github/workflows/ci.yml` when the user asks about CI/CD. Promotion
requires an immutable digest, evaluation evidence tied to the artifact and
dataset, security/supply-chain checks, restore evidence, and human approval.

## Command selection rules

- Health question → health command; do not edit state.
- Documentation or structure question → focused guards and docs; do not
  rewrite generated output unless the owning generator is used.
- AI behavior question → inspect the MCP/CLI/script boundary and evaluation
  tests before changing prompts.
- New external data → lake landing/Bronze first, then Silver/Gold and an Ops
  projection.
- Repeated deterministic work → add or reuse `infra/scripts/`, not a longer
  prompt.
- Broad “make it better” request → produce a prioritized gap list first, then
  implement only the approved, narrow slice.
