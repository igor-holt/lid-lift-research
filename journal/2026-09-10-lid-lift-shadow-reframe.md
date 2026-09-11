# LID-LIFT Journal — 2026-09-10

**Record type:** execution-plan-trace / commercial reframe  
**Author:** Igor Holt (ORCID: 0009-0008-8389-1297)  
**System:** LID-LIFT Orchestrator v1.4  
**Evt:** `evt_lidlift_tunnel_maru_20260911T0210Z`  
**Maru:** `maru-reframe-lidlift-gtm-20260911` (R = 0.62, `#!nox`)

## Papers

- WP-001 Beyond Retry — DOI [10.5281/zenodo.17784144](https://doi.org/10.5281/zenodo.17784144)
- WP-002 The Landauer Context — DOI [10.5281/zenodo.17784836](https://doi.org/10.5281/zenodo.17784836)
- WP-003 Dissonance-Weighted Eviction — companion markdown in this repository

## What was reviewed this cycle

1. Core engine (four-stage recovery; stages still mocked).
2. Production Dockerfile (Uvicorn API layout; package tree not present in the reviewed drop).
3. Enterprise licensing YAML ($0 Shadow / $7,000 Standard / $70,000 OEM).
4. Hardened bridge (Shadow / Active / Bypass + Landauer USD estimator).
5. Outbound ICP + Touch 1–2 draft (FinOps wedge).
6. Market scan of North American agent observability and AI FinOps (2026).

## Maru finding

Selling a $7k–$70k “control plane” into a category where buyers already pay $29–$249/mo (or self-host) for traces, cost, evals, and gateways is a no-win if Shadow cannot reconcile waste to invoices.

**Reframe:** do not compete as another observability platform. Compete as a deadlock classifier that reads existing traces (OpenTelemetry / Langfuse / LangSmith / gateway logs) and emits an attested waste line. Keep Active (prompt rewrite) off until Shadow survives finance review.

## Commercial constraints (public)

- Do not lead outbound with an unsourced industry waste percentage.
- Shadow Mode must not emit a repacked prompt.
- USD waste = provider list price × tokens on deadlock-classified spans only — not the whole window scaled to a 43,200-minute month.
- $7,000/mo is a floor for accounts with large existing LLM opex, not a default list price.
- Landauer / η_therm is research reporting, not the buyer-facing metric.

## Next tunnel steps

1. Hard-disable Active in every customer-facing PoV.
2. Replace substring deadlock detection (`"retry"` in prompt) with repeated tool+error / span-loop signatures.
3. Qualify accounts on 90-day LLM API spend plus an existing trace store.
4. Rewrite Touch 1 as “we annotate deadlock spans on traces you already have.”
5. Convert only when attested savings clear the fee.

## Provenance

- Public research repo: https://github.com/igor-holt/lid-lift-research
- MCP control-plane repo: https://github.com/igor-holt/lidlift-mcp
- Operator: https://github.com/igor-holt
- Site: https://www.genesisconductor.io
