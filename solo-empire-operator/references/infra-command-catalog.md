# Solo Empire Infra Command Catalog

Use this as a route lookup. Run operational commands from `platform-ops-cli`
(`SOLO_OPS_ROOT`, legacy sibling `../platform-ops-cli`). Read architecture documents
from `architecture-docs` (`SOLO_ARCHITECTURE_ROOT`, sibling
`../architecture-docs`). Consult the hub catalog for registry and hub harness work;
registered systems are operated from their owning repositories. Prefer the
narrowest check that answers the request; do not run all portfolio labs by
default.

## Context routes

| Need | Read first |
|---|---|
| Architecture and repository ownership | `architecture-docs/docs/AI-AGENT-GUIDE.md` and owning repository READMEs |
| Architecture or boundary | `architecture-docs/docs/ARCHITECTURE.md`, `architecture-docs/docs/AI-AGENT-GUIDE.md` |
| Infra inventory | `platform-ops-cli/README.md` |
| Workspace location | `architecture-docs/docs/WORKSPACE-STRUCTURE.md`, `architecture-docs/docs/WORKSPACE-LOCATION-MAP.md` |
| New ingress/import | `architecture-docs/systems/ai-data/data-lake-architecture.md`, `architecture-docs/learning/platform-engineering/app-cli-data-lake-playbook.md` |
| AI/RAG/MLOps | `architecture-docs/systems/ai-data/central-mlops-devsecops-pipeline.md`, matching `architecture-docs/operations/` runbook |
| Documentation change | `architecture-docs/docs/governance/DOCUMENTATION-STANDARDS.md`, `architecture-docs/docs/governance/DOC-MAINTENANCE.md` |
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
task status
task dashboard
task tasks
task tasks:health
task agent:decision-context -- --json
```

Run these from the `platform-ops-cli` checkout. They are Taskfile-backed
operational interfaces; consult its Taskfile before using additional commands.

## Verification ladder

Run the smallest applicable group, then the repository baseline for changes:

```bash
task test
task typecheck
task docs:check
task task:parity
task task:ownership -- --json
```

Other Taskfile-backed focused checks:

```bash
task test:python
task test:platform
task test:workspace
task test:automation
task test:analytics
task test:seo-report
task contracts:check
task lint:secrets
task lint:paths
```

Do not describe a check as passed when a credential, external service, or
optional daemon caused it to be skipped.

## Database and operational writes

The live task source of truth is the Tasks API in `empire-platform`; the
ops-toolkit `task tasks` command is its operational client. If a supported task
MCP tool is unavailable, record the task/correlation ID in the bounded brief
or handoff and report the limitation. Do not create a shadow SQLite store or
request credentials to work around unavailable MCP access.

## MLOps/AI pipeline

The current pipeline is a local reference lifecycle, not hosted LLM
production. It covers candidate training, deterministic evaluation, local
registration, categorical drift monitoring, and manual promotion semantics.

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
