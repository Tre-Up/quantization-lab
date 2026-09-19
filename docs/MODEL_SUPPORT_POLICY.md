# Model Support Policy

v0.1 should test generalization without pretending every MoE architecture is interchangeable.

## Support tiers

### Tier A — validated

A model family or architecture variant is Tier A only when:

- baseline loads reproducibly;
- expert structure and router behavior can be identified;
- quantization path is supported;
- routing/runtime instrumentation works;
- locked held-out evaluation completes;
- required runtime metrics are collected;
- caveats are documented.

### Tier B — experimental

The model can be loaded and partially profiled or quantized, but one or more validation requirements are incomplete.

### Tier C — unsupported

The architecture contains unsupported layers/routing behavior, cannot be instrumented reliably, or cannot be tested with available hardware/tooling.

## Initial selection strategy

Prefer open-weight models that:

- have workable licenses;
- expose a clear MoE structure;
- have variants small enough for local iteration or partial profiling;
- are supported by practical Apple Silicon tooling where possible;
- differ enough to test whether the policy generalizes.

The final validation set should be chosen to challenge assumptions, not to maximize flattering results.

## Exact revision rule

Scientific results must record:

- exact model identifier;
- model revision/commit;
- tokenizer revision;
- runtime/backend version.

“Model X 7B” is not sufficient provenance.

## Required architecture metadata

For MoE models, document where relevant:

- total experts per layer;
- experts selected per token;
- shared experts;
- router type and routing output;
- expert hidden size / MLP structure;
- attention variant;
- tied embeddings;
- output head behavior;
- expert weight naming/layout;
- backend-specific kernel assumptions.

## Unsupported assumptions

A method must fail loudly if it cannot safely interpret the model structure.

Silently skipping experts, layers, or unsupported tensors is not broad support. It is invalid evidence with better typography.
