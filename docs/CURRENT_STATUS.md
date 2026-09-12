# Current Status

Last updated: **2026-09-12**

## Phase

**Foundation / Week 0 → Week 1 transition**

## What exists

- public repository;
- 13-week charter and roadmap;
- explicit success/failure criteria;
- evaluation and runtime-memory standards;
- experiment logging protocol;
- learning path;
- architecture direction;
- reproducibility/IP/community policies;
- minimal `qlab doctor` CLI skeleton.

## What does not exist yet

- no custom quantization method;
- no benchmark suite implementation;
- no 4× result;
- no 5× result;
- no 99% or 99.9% retention claim;
- no validated multi-model support;
- no external reproduction.

That absence is intentional. The repo begins by recording the real starting point rather than pretending the ending already happened.

## Immediate next milestone

**M1: First reproducible local baseline**

Acceptance:

- one small open-weight model selected;
- exact revision recorded;
- baseline runs on the M4/16 GB machine;
- weight size, peak runtime memory, latency, and throughput measured;
- one existing quantized variant measured under the same workload;
- experiment committed using the research template.

See [`../research/week-01.md`](../research/week-01.md).
