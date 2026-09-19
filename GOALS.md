# Goals

## v0.1 primary goals

The v0.1 program targets the following evidence by **2026-12-19**.

### 1. Reproducible baselines

Establish and freeze:

- a full-precision or highest-practical-precision reference;
- at least one established quantized baseline;
- a comparable MoE runtime baseline;
- fixed prompts, context lengths, decoding, and hardware settings.

### 2. Multiple architectures

Attempt validation across **at least three open-weight model families or architecture variants**, subject to model availability and target-device feasibility.

Failures remain part of the record.

### 3. Meaningful compression

For the headline candidate:

- target **≥3× expert-weight storage compression** relative to FP16/BF16;
- report total model storage separately from expert-only storage;
- report resident and peak runtime memory separately;
- include metadata, scale, cache, and offload overhead where material.

### 4. High measured quality retention

Target **≥99% aggregate measured quality retention** on the locked held-out protocol.

No major domain may be hidden by an aggregate score. Per-domain deltas and uncertainty must be reported.

### 5. Joint precision + residency policy

Build an automatic policy that can consider:

- expert/tensor sensitivity;
- routing frequency;
- bit width / group size;
- resident vs offloaded experts;
- target memory budget;
- measured quality constraint.

It must be compared against simpler baselines such as uniform quantization and naive/frequency-only residency.

### 6. Real constrained-device evidence

On Apple Silicon / 16 GB unified memory, report where measurable:

- weight storage;
- resident memory;
- peak runtime memory;
- TTFT;
- tokens/second;
- expert transfer volume / cache behavior;
- sustained repeated-run behavior.

### 7. Reproducibility

Every headline number must map to:

- committed code;
- frozen config;
- exact model revision;
- hardware/runtime metadata;
- raw or immutably referenced result artifacts.

At least one technically competent external user should be able to reproduce a documented result without private instructions.

## Stretch goals

Not promised:

- approximately **4× or better expert-weight compression** with **≥99.9% measured quality retention**;
- measurable energy or sustained-thermal improvement versus a fair quantized baseline;
- effective expert prefetch that reduces stalls without unacceptable memory growth;
- larger-than-memory MoE inference with useful interactive performance;
- independent reproduction of the headline result.

## Non-goals

The project does not optimize for:

- GitHub stars over technical quality;
- benchmark gaming;
- one hand-picked model presented as universal evidence;
- vague “same intelligence” language;
- parameter-count claims based on lower-bit storage;
- file-size compression presented as runtime-memory compression;
- hidden cross-device comparisons;
- novelty claims unsupported by prior-art review.

## Long-term ambition

Build a trustworthy device-aware inference optimizer that treats **precision, memory residency, routing behavior, and measured capability** as one deployment problem rather than isolated knobs.
