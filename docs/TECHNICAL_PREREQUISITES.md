# Technical Prerequisites

This document defines background knowledge required to work safely on the research codebase. It is not a project milestone or progress log.

Contributors working on quantization, MoE profiling, or evaluation should be comfortable with the following concepts.

## Numerical representation

- bits, bytes, integer ranges;
- FP32, FP16, BF16, and low-bit integer representations;
- scale and zero-point;
- symmetric and asymmetric quantization;
- per-tensor, per-channel, and per-group quantization;
- clipping, outliers, reconstruction error, and metadata overhead.

## Model structure

- tensors, shapes, and matrix multiplication;
- transformer linear projections;
- embeddings, attention, MLP blocks, normalization, and residual paths;
- model weights vs activations;
- KV cache and context-dependent memory;
- MoE routing, experts, shared experts, and active-vs-total parameters.

## Runtime measurement

- storage size vs resident memory vs peak memory;
- TTFT vs generation throughput;
- warm vs cold-cache behavior;
- repeated-run variance;
- memory bandwidth and transfer costs;
- thermal throttling as a potential confounder on laptops.

## Evaluation

- baseline vs treatment;
- calibration/development/held-out separation;
- deterministic scoring where possible;
- per-domain reporting;
- paired comparisons;
- uncertainty / confidence intervals;
- benchmark leakage and cherry-picking risks.

## Research practice

A technical claim should be supported by at least one of:

- a reproducible implementation;
- a controlled experiment;
- a falsifiable prediction followed by measurement;
- a prior-art citation plus independent reproduction.

Reading material is useful only when it improves an experiment, implementation, or mental model.
