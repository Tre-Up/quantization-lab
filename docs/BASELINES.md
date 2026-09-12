# Baselines

Custom methods are judged against real baselines, not against naive quantization chosen to lose.

## Baseline ladder

### B0 — Original model
- native FP16/BF16 or published baseline precision;
- same tokenizer/prompt/runtime settings as candidate where feasible.

### B1 — Naive/simple low-bit baseline
- straightforward uniform quantization;
- establishes what happens without sensitivity-aware optimization.

### B2 — Practical established backend
At least one widely used practical path, depending on model/runtime compatibility, such as:
- MLX/MLX-LM quantization;
- llama.cpp/GGUF quantization;
- another established deployment backend.

### B3 — Research method baseline
As the project matures, compare against appropriate methods such as GPTQ, AWQ, HQQ, AutoRound, AQLM, QuIP#, or current equivalents where implementations and hardware allow a fair comparison.

## Fairness rules

When comparing methods:

- match effective bit budget as closely as practical;
- report metadata overhead;
- use the same evaluation split;
- separate quality comparison from kernel/runtime comparison if backends differ;
- do not claim a speed win caused only by comparing two unrelated runtimes;
- pin exact versions/commits.

## Improvement claim

A custom method should answer at least one of these:

- better quality at the same real memory budget;
- lower real memory at the same quality;
- faster search/calibration at comparable quality;
- better generalization across model families;
- better target-device usability.

“Different” is not an improvement metric.
