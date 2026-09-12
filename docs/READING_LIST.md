# Reading List

Read in the order the project needs the material. Do not turn this into a three-month literature-reading retreat.

## Start here

### Quantization basics

- PyTorch quantization documentation — concepts and terminology.
- Hugging Face quantization documentation — practical LLM workflows.
- MLX / MLX-LM documentation — Apple Silicon execution and quantization.
- llama.cpp quantization documentation — GGUF quantization types and practical deployment behavior.

## Core papers / methods

### GPTQ

**GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers**

Focus on:
- post-training weight quantization;
- second-order/Hessian-inspired error compensation;
- why sequential quantization can preserve quality better than naive rounding.

### AWQ

**AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration**

Focus on:
- activation-aware identification of important weights/channels;
- why not all weights matter equally;
- hardware-friendly low-bit deployment.

### SmoothQuant

**SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models**

Focus on:
- activation outliers;
- moving quantization difficulty between activations and weights;
- W8A8-style deployment thinking.

### HQQ

**Half-Quadratic Quantization (HQQ)**

Focus on:
- fast calibration-light weight quantization;
- low-bit experimentation;
- practical mixed configuration possibilities.

## Advanced low-bit work

Read after the basic reproduction stage:

- **SpQR** — sparse-quantized representation and outliers;
- **QuIP / QuIP#** — very low-bit quantization with incoherence processing;
- **AQLM** — additive quantization for LLM weights;
- **AutoRound** — optimization-based PTQ and practical low-bit workflows;
- recent mixed-precision / sensitivity-aware quantization papers.

## Different but relevant direction

### BitNet / ternary models

Useful for understanding what becomes possible when low precision is designed into training itself.

Important distinction: training a model from scratch in a low-bit architecture is **not the same problem** as post-training quantization of an existing model.

## Evaluation / systems

- EleutherAI `lm-evaluation-harness` documentation;
- MLX-LM benchmarking/runtime docs;
- llama.cpp performance/quantization docs;
- papers or docs on KV-cache quantization and context-memory scaling when that becomes part of the project.

## Reading-note template

For every serious source, write only:

```text
Problem:
Core idea:
Why it works:
What it costs:
Where it fails:
What experiment should we run because of it:
```

If a paper produces no experiment, engineering decision, or improved mental model, it probably does not deserve another three hours today.
