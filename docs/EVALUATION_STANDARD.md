# Evaluation Standard

This document defines what “measured quality retention” means in this repository.

## Core definition

For each benchmark/domain where higher is better:

```text
retention_i = quantized_score_i / baseline_score_i
```

The project reports both:

- **absolute score delta**: `quantized_score - baseline_score`
- **retention percentage**: `quantized_score / baseline_score × 100`

For metrics where lower is better, the metric must be transformed or reported separately rather than forced into the same formula.

## Aggregate quality

The headline aggregate is a **macro average across domains**, not a raw average across all questions. This prevents a large easy dataset from hiding a collapse in a smaller difficult domain.

Example domains:

- mathematics;
- coding;
- reasoning;
- factual/knowledge QA;
- instruction following;
- language modeling/perplexity where appropriate;
- long-context or retrieval behavior where feasible.

Exact domain composition will be versioned and frozen before final evaluation.

## Held-out rule

The final evaluation set must not be used to:

- choose bit widths;
- tune scales;
- select layers to protect;
- choose group size;
- stop search early;
- decide which candidate wins.

Calibration/search data and final evidence data are separate.

## Determinism

Where possible:

- temperature = 0;
- fixed prompt templates;
- fixed tokenizer/model revision;
- fixed max tokens/context;
- fixed scorer;
- fixed seed where stochasticity cannot be removed.

If the task is inherently stochastic, repeated runs and variance must be reported.

## Statistical reporting

For final headline results, report uncertainty where the metric supports it. Preferred default:

- 95% bootstrap confidence interval over evaluation items;
- paired comparison between baseline and quantized outputs when possible.

A tiny score difference inside measurement noise should not be marketed as a real gain or loss.

## “99.9% measured quality retention”

This phrase is allowed only when:

1. the locked aggregate retention is at least 99.9%;
2. raw per-domain scores are published;
3. no core domain shows a material hidden regression;
4. the protocol and model revisions are reproducible;
5. the result is explicitly scoped to the evaluation battery rather than all possible prompts.

## Exact-output agreement is a separate metric

Two models may receive the same task score while producing different text. Therefore the project may also report:

- answer exact match;
- token/output agreement under deterministic decoding;
- logit or distribution divergence when technically practical;
- pairwise disagreement rate.

These are useful diagnostics but do not replace task quality.

## Core principle

**The original model is the baseline. The quantized model is not asked to become perfect; it is asked to preserve the baseline as faithfully as the measurement can establish.**
