# Current Status

Last updated: **2026-09-19**

## Phase

**Foundation / baseline instrumentation**

The research direction has been narrowed to device-aware MoE inference: quantization precision, expert sensitivity, routing behavior, and expert residency/offload will be evaluated as a joint deployment problem.

## What exists

- public repository and research charter;
- explicit success/failure criteria;
- evaluation and runtime-memory standards;
- experiment logging protocol;
- hardware measurement standard;
- reproducibility, provenance, and contribution policies;
- architecture for profiling, sensitivity analysis, policy search, and evaluation;
- minimal `qlab doctor` CLI skeleton.

## What does not exist yet

- no custom adaptive quantization/residency method;
- no implemented MoE routing profiler;
- no expert sensitivity dataset;
- no automated residency/offload runtime;
- no benchmark-suite implementation;
- no 3×/4× headline compression result;
- no 99%/99.9% retention result;
- no multi-family validation;
- no external reproduction.

Those are open research objectives, not implied capabilities.

## Immediate milestone

**M0: Baseline contract and instrumentation**

Acceptance:

- first supported model/runtime path selected;
- exact model and tokenizer revisions recorded;
- baseline runs on the target Apple Silicon / 16 GB device where feasible;
- weight size, resident memory, peak memory, TTFT, and throughput measured;
- at least one established quantized baseline measured under equivalent settings;
- machine-readable experiment result committed;
- reproduction command documented.

See [ROADMAP.md](../ROADMAP.md).

## Research discipline

No adaptive policy, novelty claim, or headline efficiency claim should be promoted before comparable baselines and measurement tooling are established.
