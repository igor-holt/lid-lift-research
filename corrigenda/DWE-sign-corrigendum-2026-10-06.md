# Corrigendum: DWE retention polarity

**Date:** 2026-10-06
**Corrects:** Igor Holt, *Dissonance-Weighted Eviction: A Hybrid LRU Protocol for Long-Horizon Agent Memory*, Zenodo v1, 10.5281/zenodo.17784838 (2025-12-02)
**Status:** formula correction. No new experiment. Not a replacement of the working paper.

## Error

Version 1 defines alignment as

- D = 1 if the fragment entails the plan
- D = 0 if neutral
- D = -1 if the fragment contradicts the plan

and retention as

S(m_i) = (1 / Δt^α) * (1 - λ * D(m_i, P))

with example λ = 2.5.

That expression does the opposite of the stated policy. A contradiction (D = -1) raises S to 1 + λ. Entailment lowers S to 1 - λ, which is negative at the example λ. The prose says a recent contradiction should be evicted. The equation keeps it.

A second defect: Δt ≈ 0 makes the reciprocal unbounded.

## Correction

Keep the published label D. Change the sign inside the penalty, and floor age:

S(m_i) = 1 / (Δt + ε)^α * (1 + λ * D(m_i, P))

ε > 0 (use 1 in the same time unit as Δt). α = 1 unless tuned. Evict lowest S.

At λ = 2.5:

- entails plan, D = 1, factor 3.5, retained
- neutral, D = 0, factor 1, age only
- contradicts plan, D = -1, factor -1.5, evicted first

Equivalent form, if a later implementation stores conflict as a non-negative score c in [0, 1]:

S(m_i) = 1 / (Δt + ε)^α * (1 - λ * c(m_i, P))

Do not mix that c with the signed D from v1.

## What this is not

Not a measured reduction in oscillation. v1 reported none. Do not ship Active purge on this score until a trace store can show the would-be evictions against invoices. Shadow may score; it must not delete.

## Provenance

Public series repo: https://github.com/igor-holt/lid-lift-research
Parent DOI: https://doi.org/10.5281/zenodo.17784838
