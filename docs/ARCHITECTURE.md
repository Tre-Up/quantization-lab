# Architecture

This document describes the intended v0.1 architecture. Individual components may land incrementally.

## Design principles

1. **Measurement is independent from optimization.**
2. **Final held-out evidence is isolated from search.**
3. **Precision and residency are explicit policy decisions.**
4. **Runtime cost includes transfer, cache, KV-cache, and temporary-buffer effects where measurable.**
5. **Unsupported model structure fails loudly rather than being silently approximated.**

## Proposed pipeline

```text
ModelSpec + DeviceSpec
        ↓
Model Loader
        ↓
Runtime Profiler ───────────────→ Baseline Runtime Report
        ↓
MoE Routing Profiler
        ↓
Calibration / Development Data
        ↓
Expert + Tensor Sensitivity Analyzer
        ↓
Cost Model
        ↓
Candidate Policy Generator
        ↓
Quantization Backend(s)
        ↓
Residency / Offload Runtime
        ↓
Development Evaluation + Runtime Measurement
        ↓
Search / Selection
        ↓
Frozen Candidate
        ↓
Locked Held-out Evaluation
        ↓
Export + Reproducibility Report
```

## Core components

### 1. Model specification

Owns:

- model identifier and exact revision;
- architecture family;
- tokenizer revision;
- MoE structure and expert naming;
- trust-remote-code policy;
- baseline precision;
- model/license metadata.

### 2. Device specification

Owns target constraints such as:

- total unified/system memory budget;
- optional resident-weight budget;
- storage path / capacity constraints;
- runtime backend;
- concurrency/context assumptions.

v0.1 primarily targets Apple Silicon with 16 GB unified memory.

### 3. Model loader

Responsibilities:

- deterministic loading;
- explicit dtype/device/backend choices;
- version capture;
- supported-layer checks;
- model/expert inventory;
- failure on unsupported structures.

### 4. Runtime profiler

Measures where feasible:

- total and expert-only weight storage;
- memory after model load;
- resident memory during generation;
- peak runtime memory;
- TTFT;
- generation throughput;
- context-dependent memory;
- repeated-run variation.

### 5. MoE routing profiler

Records:

- experts selected per token;
- expert activation frequency;
- routing concentration / skew;
- co-activation patterns where useful;
- workload identity used to produce the profile.

Routing frequency is a measured signal, not a universal property of an expert.

### 6. Sensitivity analyzer

Estimates how quantization choices affect model behavior at expert/tensor granularity.

Candidate signals may include:

- reconstruction/quantization error;
- activation statistics;
- task-level development deltas;
- expert-specific perturbation experiments;
- architecture-specific importance proxies.

No single signal is assumed to be sufficient across all model families.

### 7. Cost model

Represents deployment costs relevant to policy search:

- storage bytes;
- resident-memory bytes;
- transfer/offload cost;
- metadata/scale overhead;
- runtime latency impact where measurable.

The cost model must distinguish measured values from estimates.

### 8. Candidate policy

A serializable policy may describe:

```text
expert/tensor → bit width
expert/tensor → group size
expert/tensor → quantization scheme
expert       → resident | offloaded
expert       → cache/prefetch priority
exceptions   → higher precision / pinned residency
```

Uniform INT4 with all experts resident is a baseline policy, not the architecture of the project.

### 9. Quantization backends

v0.1 should integrate established runtimes/backends before rewriting kernels. Candidate paths may include MLX/MLX-LM, llama.cpp/GGUF, or research backends as compatibility permits.

The project contribution, if supported by evidence, is expected to live primarily in profiling, policy construction/search, and device-aware execution rather than pretending established quantization primitives are novel.

### 10. Residency / offload runtime

Responsibilities may include:

- keeping selected experts resident;
- loading offloaded experts on demand;
- bounded caching;
- measuring transfer volume and stalls;
- optional prefetch experiments.

Correctness comes before clever prefetch.

### 11. Search engine

Objective:

```text
minimize measured/estimated deployment cost
subject to measured quality loss <= allowed threshold
and device memory constraints
```

Possible strategies, in increasing complexity:

- frequency-only baselines;
- sensitivity-ranked protection;
- greedy joint bit/residency allocation;
- budgeted local search;
- evolutionary/Bayesian search if justified by evidence.

Do not begin with the fanciest optimizer. Beat simple baselines first.

### 12. Evaluation runner

Runs development or locked held-out suites under frozen settings.

The search system must not query final held-out results.

### 13. Exporter

Produces:

- runnable artifact or reproducible build recipe;
- policy/config;
- model/source attribution;
- benchmark summary;
- hardware/runtime metadata;
- exact reproduction instructions.

## Data separation

These remain logically and operationally separate:

```text
calibration / profiling data
development evaluation
locked final held-out evaluation
```

## Open technical risks

- expert routing profiles may be workload-specific;
- low-bit experts may require kernels that erase theoretical gains;
- SSD/offload latency may dominate;
- caching may reduce memory savings;
- KV cache may become the dominant memory term;
- thermal throttling may distort laptop benchmarks;
- a policy may overfit one model family;
- sensitivity signals may fail to predict task-level regressions.

These risks are part of the research question, not inconveniences to hide.
