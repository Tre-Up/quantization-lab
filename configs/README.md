# Configs

Frozen, machine-readable experiment configuration belongs here.

A config should make important comparison choices explicit, including where applicable:

- model and tokenizer revision;
- runtime/backend;
- baseline precision;
- quantization scheme, bit width, and group size;
- protected layers/experts;
- residency/offload policy;
- cache/prefetch settings;
- prompt/workload identity;
- context and generation lengths;
- calibration/development split identifiers;
- random seeds.

Final held-out data identifiers must not be exposed to policy-search code paths.
