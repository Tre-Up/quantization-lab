# Evaluation Standard

This document defines measured capability retention for baseline-vs-candidate comparisons.

## Core definition

For each benchmark/domain where higher is better:

```text
retention_i = candidate_score_i / baseline_score_i
```

Report both:

- **absolute score delta**: `candidate_score - baseline_score`
- **retention percentage**: `candidate_score / baseline_score × 100`

Metrics where lower is better must be transformed carefully or reported separately rather than forced into this formula.

## Aggregate quality

The headline aggregate is a **macro average across domains**, not a raw average across all examples. This prevents a large easy dataset from hiding collapse in a smaller difficult domain.

Candidate domains may include:

- mathematics;
- coding;
- reasoning;
- factual/knowledge QA;
- instruction following;
- language modeling/perplexity where appropriate;
- long-context or retrieval behavior where feasible.

Exact composition and versions are frozen before final evaluation.

## Data separation

Three roles are distinct:

```text
profiling / calibration data
development evaluation
locked final held-out evaluation
```

The locked final set must not be used to:

- choose bit widths;
- tune scales or group size;
- select layers/experts to protect;
- choose resident/offloaded experts;
- tune cache or prefetch rules;
- stop search early;
- choose the winning candidate.

Routing profiles used by the optimizer must also be identified explicitly so workload-specific tuning is visible.

## Determinism

Where possible:

- temperature = 0;
- fixed prompt templates;
- fixed tokenizer/model revision;
- fixed max tokens/context;
- fixed scorer;
- fixed seed where stochasticity remains.

If a task/runtime is inherently stochastic, repeated runs and variance must be reported.

## Statistical reporting

For final headline results, report uncertainty where supported. Preferred defaults:

- 95% bootstrap confidence interval over evaluation items;
- paired baseline/candidate comparison when possible;
- sample counts per domain.

A score difference inside measurement noise is not a meaningful gain or loss merely because the third decimal changed.

## High-retention wording

“99.9% measured quality retention” is allowed only when:

1. locked aggregate retention is at least 99.9%;
2. raw per-domain scores are published;
3. no core domain shows a material hidden regression;
4. protocol and model revisions are reproducible;
5. the result is scoped to the tested evaluation battery.

The same rule applies to a measured 100% retention result: it means **no measured score loss on the locked protocol**, not universal equivalence on every possible prompt.

## Exact-output agreement is separate

Two systems may receive the same task score while producing different text. Diagnostic metrics may include:

- answer exact match;
- token/output agreement under deterministic decoding;
- logit/distribution divergence when practical;
- pairwise disagreement rate;
- router/expert-selection disagreement where relevant.

These diagnostics do not replace task-level quality.

## Core principle

**The baseline defines the behavior being preserved. The candidate is evaluated on what the measurement can establish, not on vague claims about “intelligence.”**
