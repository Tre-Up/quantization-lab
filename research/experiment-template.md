# Experiment Record

## Metadata

- Experiment ID:
- Date:
- Commit SHA:
- Model + exact revision:
- Tokenizer revision:
- Architecture / MoE layout:
- Hardware:
- Runtime/backend + version:
- OS:
- Config path:

## Question

What single technical question is this experiment trying to answer?

## Hypothesis

State the expected outcome **before** running the experiment.

## Baseline

- Precision / quantization method:
- Residency policy:
- Context length:
- Prompt/workload identity:
- Decoding settings:
- Total weight size:
- Expert-weight size:
- Resident memory:
- Peak runtime memory:
- TTFT:
- Throughput:
- Quality scores:

## Candidate

- Quantization method:
- Bit width / mixed-bit policy:
- Group size:
- Protected tensors/experts:
- Residency/offload policy:
- Cache/prefetch policy:
- Calibration/profiling data:
- Development-evaluation split:
- Search settings:
- Other changed variables:

## MoE / transfer measurements

Where applicable:

- experts selected per token:
- routing-frequency summary:
- expert cache hit rate:
- bytes transferred:
- load/fetch stalls:
- resident expert set:

## Result

Record raw numbers and machine-readable artifact paths. Do not substitute adjectives for measurements.

## Comparison

- storage delta:
- resident-memory delta:
- peak-memory delta:
- TTFT delta:
- throughput delta:
- quality delta / retention:
- transfer/offload cost:

## Interpretation

What does the result suggest, and what does it **not** establish?

## Confounders / uncertainty

What could make the conclusion wrong?

Examples:

- thermal state;
- background processes;
- workload-specific routing;
- noisy scorer;
- cache warm-up;
- backend/kernel differences;
- insufficient sample count.

## Decision

- [ ] keep direction
- [ ] modify
- [ ] reject
- [ ] reproduce before deciding

## Next experiment

What is the smallest next experiment justified by this result?
