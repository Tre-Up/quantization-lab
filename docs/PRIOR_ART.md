# Prior-Art Discipline

This project must distinguish **integration**, **engineering improvement**, and **research novelty**.

## Rule

No technique is described as novel until relevant prior work has been searched, read, and compared against the actual mechanism being claimed.

## Areas that require prior-art review

At minimum, review work related to:

- post-training LLM quantization;
- mixed-bit / mixed-precision allocation;
- sensitivity-aware quantization;
- MoE routing and expert specialization;
- expert caching and residency;
- CPU/GPU/NPU expert placement;
- SSD / storage-backed expert offload;
- expert prefetch and routing prediction;
- constrained-device / Apple Silicon inference;
- joint memory / latency / quality optimization.

## Record format

For each directly relevant work, record:

```text
Citation / link:
Problem:
Core mechanism:
Signals used:
Optimization target:
Hardware/runtime assumptions:
What overlaps with this project:
What is materially different:
What experiment would distinguish the two:
```

## Claim categories

### Reproduction
An existing method is implemented or rerun under our protocol.

### Integration
Known techniques are combined into one system without claiming the combination itself is new.

### Engineering contribution
The implementation, measurement system, runtime behavior, or deployment path improves practical use in a defensible way.

### Research contribution
A mechanism or empirical finding is materially different from known work and survives fair baseline comparison.

The category must be chosen from evidence, not ambition.

## Disclosure discipline

Potentially novel mechanisms should be reviewed for prior art and IP implications before broad public disclosure. This repository should never use “first,” “novel,” or equivalent language merely because the author had not seen the idea before.
