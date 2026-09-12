# Benchmark Plan

The benchmark system exists to answer a narrow question: **did quantization reduce measured capability, and by how much?**

## Phase A — development battery

Used during method development. It may influence engineering decisions.

Purpose:
- fast iteration;
- catch obvious regressions;
- compare candidate settings;
- diagnose which domains fail first.

Target size: enough examples to be useful without making each experiment painfully slow.

## Phase B — locked held-out battery

Never used to tune the quantizer.

Purpose:
- final evidence;
- compare baseline and final candidate;
- support release claims.

Target direction: **10k+ diverse evaluations** for v0.1 if compute permits, with expansion toward 30k–50k for stronger claims.

## Core domains

Initial design:

1. **Math** — exact-answer problems at multiple difficulty levels.
2. **Coding** — executable tests / pass@1 where licensing permits.
3. **Reasoning** — structured reasoning and multiple-choice tasks.
4. **Knowledge** — factual QA with deterministic scoring where possible.
5. **Instruction following** — constraint adherence and formatting behavior.

Optional diagnostic domains:

- long context;
- multilingual;
- safety/refusal behavior;
- retrieval-style tasks;
- perplexity / next-token likelihood.

## Benchmark selection rules

A benchmark should be included only if:

- its license permits our use;
- scoring is understandable;
- the model is not obviously optimized specifically for that test in a way that makes the comparison meaningless;
- we can freeze the exact version;
- it adds information not already duplicated by another test.

## Reporting

Every report must include:

- baseline score;
- quantized score;
- absolute delta;
- retention %;
- sample count;
- scorer/version;
- confidence interval when appropriate;
- decoding configuration;
- model revision;
- hardware/runtime configuration.

## Anti-gaming rule

If a quantized configuration performs badly on a locked domain, the response is to investigate the failure, not to remove the domain.
