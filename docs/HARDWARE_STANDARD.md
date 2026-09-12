# Hardware & Runtime Measurement Standard

The project is deployment-oriented. File size alone is never enough.

## Primary constrained device

Main local development target:

- Apple Silicon
- MacBook Air M4
- 16 GB unified memory

Larger hardware may be used for baselines or larger-model experiments when the constrained device cannot hold the original model.

## Required runtime measurements

For every serious comparison, record:

1. **model weight bytes on disk**;
2. **peak runtime memory** under a fixed workload;
3. **idle memory after model load** where measurable;
4. **time to first token**;
5. **generation throughput** in tokens/second;
6. **context length**;
7. **prompt length**;
8. **generated-token count**;
9. **runtime/backend version**;
10. **OS and hardware metadata**.

## Fixed-workload rule

Baseline and quantized candidates must use the same:

- prompt set;
- context length;
- generation length;
- batch/concurrency setting;
- runtime backend where comparison is intended to be direct;
- power/thermal assumptions as far as practical.

## Effective compression

Report at least two compression ratios:

```text
weight_compression = baseline_weight_bytes / quantized_weight_bytes
runtime_memory_compression = baseline_peak_memory / quantized_peak_memory
```

Do not merge these into one number.

## When the baseline cannot fit locally

For a model too large for the target device:

- measure the baseline on hardware that can hold it;
- clearly mark that runtime-memory ratios are cross-device unless equivalent hardware measurements exist;
- do not imply a precise local peak-memory ratio that was never measured;
- still test whether the final quantized artifact can run on the target device.

## Thermal and repeatability note

Laptop inference can vary with temperature and background processes. Serious latency/throughput results should use repeated runs and report median plus variation rather than one heroic screenshot.
