# Learning Path

This path assumes a beginner starting point. Learn only what is needed to run the next experiment. Do not spend six weeks “preparing to begin.”

## Layer 1 — Python and numerical basics

You need to be able to:

- read and write Python comfortably;
- use virtual environments and install packages;
- understand arrays/tensors and shapes;
- write simple loops, functions, classes, and tests;
- load/save structured data such as JSON;
- use Git without destroying the repo.

Minimum math:

- fractions, percentages, powers of two;
- vectors and matrices;
- matrix multiplication intuition;
- mean, variance, percentiles;
- basic probability;
- confidence intervals at an intuitive level.

## Layer 2 — How model weights occupy memory

Understand:

- bit vs byte;
- FP32, FP16, BF16;
- integer representations;
- why 16-bit → 4-bit suggests a theoretical 4× weight-size reduction;
- why metadata/scales/runtime overhead mean actual deployment ratios differ.

You should be able to estimate rough weight memory by hand.

## Layer 3 — Quantization fundamentals

Learn:

- post-training quantization (PTQ);
- quantization-aware training (QAT), conceptually;
- scale and zero-point;
- symmetric vs asymmetric quantization;
- per-tensor, per-channel, and per-group quantization;
- group size;
- clipping;
- outliers;
- quantization error;
- dequantization;
- mixed precision / mixed bit-width.

Goal: explain each concept without jargon before using it in an experiment.

## Layer 4 — Transformer anatomy

Understand enough to locate the weights we are changing:

- token embeddings;
- attention projections;
- MLP/feed-forward blocks;
- normalization;
- output head;
- residual connections;
- KV cache and why it affects runtime memory separately from model weights.

No need to become a transformer theorist before running experiments.

## Layer 5 — Existing LLM quantization methods

Reproduce before inventing.

Study at least:

- GPTQ;
- AWQ;
- SmoothQuant;
- HQQ;
- modern low-bit methods such as QuIP#/AQLM as the project advances;
- llama.cpp / GGUF quantization behavior;
- MLX/MLX-LM quantization on Apple Silicon.

For each method answer:

1. What problem is it solving?
2. What information does it use?
3. What does it optimize?
4. What bit range does it target?
5. What quality/runtime tradeoff does it make?
6. What assumptions might fail on another model family?

## Layer 6 — Evaluation

Learn enough measurement to avoid fooling yourself:

- baseline vs treatment;
- train/calibration/development/held-out separation;
- deterministic scoring;
- benchmark leakage;
- macro vs micro averaging;
- paired comparisons;
- bootstrap confidence intervals;
- variance and repeated trials.

## Layer 7 — Systems / Apple Silicon

Learn as required:

- unified memory;
- memory-mapped model files;
- Metal/MLX execution basics;
- CPU/GPU memory behavior;
- model load vs generation memory;
- KV cache;
- latency vs throughput;
- why a tiny file can still have an ugly runtime footprint.

## Layer 8 — Original research

Only after the baseline stack is reliable:

- layer/tensor sensitivity measurement;
- Hessian/activation-inspired importance concepts;
- automatic bit allocation;
- constrained optimization;
- search algorithms;
- transfer of sensitivity priors across model families;
- failure analysis below 4 bits.

## Proof of learning

A topic is considered learned only when at least one is true:

- you can implement a toy version;
- you can explain it plainly from memory;
- you can predict how changing it should affect an experiment and then test that prediction.

Watching a video is not evidence of learning. Human civilization has suffered enough from completed progress bars.
