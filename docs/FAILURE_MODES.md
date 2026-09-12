# Failure Modes

This project should try to disprove itself before strangers do it for us.

## Scientific failure modes

### Benchmark leakage
The final evaluation data influences quantization search or hyperparameter choices.

**Mitigation:** strict split between calibration/development and held-out final evaluation.

### Aggregate-score camouflage
Strong domains hide a serious collapse in another domain.

**Mitigation:** publish per-domain scores and macro aggregates.

### Tiny test set
A headline percentage comes from too few examples to support the precision claimed.

**Mitigation:** report sample size, uncertainty, and expand the held-out set before strong claims.

### Judge noise
An LLM-as-judge score changes because the judge is noisy rather than because the quantized model changed.

**Mitigation:** deterministic scorers when possible; calibrated repeated judging only when necessary.

### Non-equivalent baselines
Baseline and quantized model use different prompts, context lengths, token limits, runtimes, or templates.

**Mitigation:** frozen experiment configs.

## Quantization failure modes

### Outlier destruction
A small set of large/important weights or activation channels is damaged by aggressive low-bit representation.

### Layer sensitivity mismatch
A uniform bit width is safe for most layers but catastrophically bad for a few.

### Below-4-bit collapse
Average bit-width looks impressive while language quality or difficult tasks degrade sharply.

### Architecture-specific assumptions
A method works on one transformer family but fails on another, especially MoE or unusual attention/MLP layouts.

### Calibration overfitting
The quantizer performs well on calibration-like text but generalizes poorly.

## Runtime failure modes

### Small file, large runtime
The stored weights are compact but the runtime expands/dequantizes them or allocates large temporary buffers.

### KV-cache dominance
Model weights shrink, but long-context inference is still dominated by KV-cache memory.

### Kernel mismatch
Low-bit representation reduces memory but lacks an efficient kernel, causing terrible speed.

### Memory pressure / swapping
A configuration technically loads on a 16 GB machine but becomes unusably slow because the OS is under severe memory pressure.

### Thermal benchmarking
A first run looks fast; later runs throttle.

## Product/research failure modes

### “Works on my Mac” syndrome
No external reproduction.

### Vanity metrics
Stars rise but nobody successfully quantizes or runs a model.

### Premature originality claims
A technique is presented as novel before a serious prior-art search.

### Premature disclosure
A genuinely novel potentially patentable mechanism is published before IP options are evaluated.

### Scope explosion
The project tries to solve quantization, pruning, distillation, speculative decoding, training, and datacenter scheduling at once.

**Mitigation:** v0.1 remains focused on post-training quantization and measured local inference.
