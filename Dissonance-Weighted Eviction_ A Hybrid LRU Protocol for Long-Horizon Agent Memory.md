# **Dissonance-Weighted Eviction: A Hybrid LRU Protocol for Long-Horizon Agent Memory**

**DOI:** 10.5281/zenodo.17784838

**Date:** December 2025

**Version:** 1.0 (Version of Record)

**Author:** Igor Holt

**System:** LID-LIFT Orchestrator v1.4

**Series:** Part 3 of the LID-LIFT Technical Suite

## **Abstract**

Long-horizon autonomous agents suffer from "context drift"—the accumulation of contradictory or obsolete information within the sliding context window. Traditional Least Recently Used (LRU) policies preserve data based on temporal recency, regardless of its semantic validity. This paper introduces **Dissonance-Weighted Eviction (DWE)**, a core component of the **HMIC-PPT Memory Model**. By multiplying temporal decay with a "Semantic Dissonance" coefficient (derived from entailment scoring against the active plan), DWE proactively purges conflicting data. We demonstrate that this hybrid policy significantly reduces "agent schizophrenia" (the oscillating behavior between two contradictory instructions) in constraints-heavy environments.

## **1\. Introduction: The Context Hygiene Problem**

In Large Language Model (LLM) orchestration, the "Hot Context" (the immediate token window) is a scarce resource. Standard cache management algorithms fail to account for the *meaning* of the data:

* **LRU (Least Recently Used):** Assumes recent \= relevant.
* **LFU (Least Frequently Used):** Assumes popular \= relevant.

Neither algorithm detects **Semantic Dissonance**: when a recent memory fragment ($m\_t$) logically contradicts the system's current Single Source of Truth ($SSOT$) or confirmed objective.

## **2\. The DWE Algorithm**

The **Dissonance-Weighted Eviction** protocol replaces the standard eviction score with a hybrid metric.

### **2.1 Defining Dissonance**

We define Dissonance ($D$) not merely as "low similarity," but as "high contradiction." Let $P$ be the current active Plan and $m\_i$ be a memory fragment in the Hot Ring. The dissonance score is derived from a Natural Language Inference (NLI) entailment check:

$$D(m\_i, P) \= \\begin{cases} 1 & \\text{if } m\_i \\text{ entails } P \\\\ 0 & \\text{if neutral} \\\\ \-1 & \\text{if } m\_i \\text{ contradicts } P \\end{cases}$$

### **2.2 The Eviction Function**

The priority score $S$ for retaining an item in memory is calculated as:

$$S(m\_i) \= \\frac{1}{\\Delta t^\\alpha} \\cdot (1 \- \\lambda \\cdot D(m\_i, P))$$
Where:

* $\\Delta t$: Time since last access (LRU component).
* $\\alpha$: Decay factor (typically 1.0).
* $\\lambda$: The **Dissonance Penalty** coefficient (tunable, e.g., 2.5).

If a memory fragment $m\_i$ is highly recent ($\\Delta t \\approx 0$) but effectively contradicts the plan ($D \\approx \-1$, creating a positive penalty addition), the score $S$ drops precipitously, triggering eviction despite the item's recency.

## **3\. Implementation in HMIC-PPT**

This logic is enforced within the **HMIC-PPT** (Hierarchical Memory) structure. When the **LID-LIFT Dynamic** (see 10.5281/zenodo.17784144) triggers a "Rebuild", it runs the DWE algorithm across the Hot Ring.

1. **Freeze:** The context is locked.
2. **Scan:** Every memory chunk is scored against the *new* Abstracted Objective ($O'$).
3. **Purge:** Items with high dissonance (e.g., failed code snippets from the previous attempt) are evicted regardless of timestamp.

## **4\. Conclusion**

Memory is not just storage; it is a filter. Dissonance-Weighted Eviction transforms the context window from a passive log of events into an active, self-correcting semantic buffer, essential for maintaining coherence in autonomous systems running over extended timeframes.

*© 2025 Igor Holt. This work is licensed under CC BY 4.0.*