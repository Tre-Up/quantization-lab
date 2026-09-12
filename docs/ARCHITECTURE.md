# Architecture

This file describes the intended architecture. v0.1 may implement only part of it.

## Design principle

Separate **measurement**, **search**, **quantization**, and **export**. A method should not be able to quietly change the benchmark that judges it.

## Proposed pipeline

```text
ModelSpec
   ↓
Model Loader
   ↓
Profiler ───────────────→ Baseline Runtime Report
   ↓
Calibration / Search Data
   ↓
Sensitivity Analyzer
   ↓
Candidate Policy Generator
   ↓
Quantization Backend(s)
   ↓
Candidate Runtime + Development Evaluation
   ↓
Search / Selection
   ↓
Frozen Candidate
   ↓
Held-out Evaluation
   ↓
Export + Reproducibility Report
```

## Components

### 1. Model specification

Owns:
- model identifier;
- exact revision/hash;
- architecture family;
- tokenizer revision;
- trust-remote-code policy;
- baseline precision.

### 2. Model loader

Responsibilities:
- deterministic loading;
- explicit dtype/device choices;
- version capture;
- fail loudly when unsupported layers are encountered.

### 3. Runtime profiler

Measures:
- weight storage;
- load-time memory;
- peak runtime memory;
- latency;
- throughput;
- context-dependent memory where feasible.

### 4. Evaluation runner

Runs development or held-out suites without exposing the held-out set to the search algorithm.

### 5. Sensitivity analyzer

Future purpose:
- estimate which tensors/layers tolerate low precision;
- record error/activation/importance signals;
- create reusable sensitivity profiles.

It must not assume that every model family has identical sensitivity structure.

### 6. Candidate policy

A policy describes quantization choices such as:

```text
layer/tensor → bit width
layer/tensor → group size
layer/tensor → quantization scheme
exceptions → higher precision
```

Uniform INT4 is one valid policy, not the architecture of the project.

### 7. Quantization backends

v0.1 should initially integrate established backends rather than rewriting every kernel from scratch. Backends may include MLX/MLX-LM, llama.cpp/GGUF, and research methods as compatibility permits.

The research contribution can live above or inside those backends, especially in sensitivity analysis and policy search.

### 8. Search engine

Long-term objective:

```text
minimize real deployment cost
subject to measured quality loss <= allowed threshold
```

Possible search strategies, in increasing complexity:
- greedy layer protection;
- sensitivity-ranked bit allocation;
- budgeted local search;
- Bayesian/evolutionary search;
- learned policy transfer across related models.

Do not begin with the fanciest method. Establish a stupid baseline first.

### 9. Exporter

Produces:
- runnable artifact;
- config/policy;
- model/source attribution;
- benchmark summary;
- hardware/runtime metadata;
- exact reproduction instructions.

## Data separation

The architecture must keep these logically separate:

```text
calibration data
search/development evaluation
locked final held-out evaluation
```

No component that optimizes candidate policies should have routine access to final held-out results.

## Future moat candidates

If the project matures, defensibility is more likely to come from the combination of:

- model sensitivity data;
- device/runtime profiles;
- better policy search;
- highly reliable evaluation;
- optimized kernels/export paths;
- user-submitted reproduction data;

rather than one mysterious equation pasted into a README.
