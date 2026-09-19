# Failure Modes

The project should try to disprove itself before strangers do it for us.

## Scientific failure modes

### Benchmark leakage
Final held-out data influences quantization, residency, cache, prefetch, or candidate selection.

**Mitigation:** strict separation between profiling/calibration, development evaluation, and locked final evidence.

### Aggregate-score camouflage
Strong domains hide a serious collapse elsewhere.

**Mitigation:** publish per-domain scores and macro aggregates.

### Tiny test set
A precise headline percentage comes from too few examples.

**Mitigation:** publish sample counts, uncertainty, and expand evidence before stronger claims.

### Judge noise
A judge-based metric moves because the judge is noisy.

**Mitigation:** deterministic scorers where possible; repeated/calibrated judging only when necessary.

### Non-equivalent baselines
Baseline and candidate differ in prompts, context, decoding, runtime, or workload.

**Mitigation:** frozen configs and explicit exceptions.

## Quantization failure modes

### Outlier destruction
A small set of large/important weights or activation channels is damaged by aggressive low-bit representation.

### Expert sensitivity mismatch
A bit width that is safe for most experts is catastrophic for a small subset.

### Below-4-bit collapse
Average bit width looks impressive while difficult tasks degrade sharply.

### Calibration overfitting
The policy performs well on calibration-like text but generalizes poorly.

### Proxy failure
Reconstruction error or another sensitivity proxy fails to predict task-level quality.

## MoE / routing failure modes

### Workload-specific routing
An expert looks cold only because the profiling workload is narrow.

### Router-policy interaction
Quantization or runtime changes alter routing behavior enough to invalidate the original profile.

### Frequency-only caching
Frequently routed experts are kept resident while rare but latency-critical experts cause severe stalls.

### Cache thrashing
The resident set is too small or badly chosen, causing repeated expert loads.

### Prefetch misprediction
Prefetch increases traffic or memory pressure without reducing latency.

### Expert fragmentation overhead
Many individually small experts create metadata, allocation, or transfer overhead that erases theoretical savings.

## Runtime failure modes

### Small file, large runtime
Compact weights expand, dequantize, or require large temporary buffers.

### KV-cache dominance
Long-context memory remains dominated by KV cache even after expert-weight compression.

### Kernel mismatch
Low-bit representation saves memory but lacks an efficient execution kernel.

### SSD / storage bottleneck
Offloaded experts fit the memory budget but storage transfer makes interactive inference unusable.

### Memory pressure / swapping
A configuration technically loads but becomes unusably slow under pressure.

### Thermal benchmarking
Early runs look fast while sustained runs throttle.

## Research/product failure modes

### “Works on my Mac” syndrome
No independent reproduction.

### Vanity metrics
Stars increase without successful external use.

### Premature originality claims
Existing work is rediscovered and presented as novel.

### Premature disclosure
A genuinely novel patentable mechanism is published before IP options are evaluated.

### Scope explosion
The project expands into pruning, distillation, speculative decoding, training, and scheduling before the core hypothesis is tested.

**Mitigation:** v0.1 remains focused on post-training quantization, MoE profiling, expert residency/offload, and measured local inference.
