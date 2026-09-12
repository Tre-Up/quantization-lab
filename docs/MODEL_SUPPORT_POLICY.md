# Model Support Policy

v0.1 should generalize across model families without pretending every architecture is identical.

## Support tiers

### Tier A — validated
A model family is Tier A only when:

- baseline loads reproducibly;
- quantization path is supported;
- held-out evaluation completes;
- runtime metrics are collected;
- known caveats are documented.

### Tier B — experimental
The model can be quantized/run, but full held-out or runtime validation is incomplete.

### Tier C — unsupported
The architecture contains unsupported layers/behavior or cannot be tested reliably with available hardware/tooling.

## Initial family strategy

Choose families that:

- have open weights under workable terms;
- have small variants suitable for local iteration;
- also have larger variants useful for scale validation;
- are supported by practical Apple Silicon tooling where possible.

Candidate families may include Qwen, Llama-family derivatives where licensing permits, Gemma, Mistral, or others selected after compatibility checks.

The final three-family set should be chosen because it tests generalization, not because all three happen to give flattering results.

## Exact revision rule

Never write only “Qwen 7B” or “Gemma” in a scientific result. Record the exact repository/model identifier and revision.

## Architecture assumptions

Every custom method must document assumptions such as:

- dense transformer vs MoE;
- supported linear-layer types;
- tied embeddings;
- attention variant;
- quantized vs unquantized output head;
- backend-specific kernel requirements.

A method that silently skips half a model is not broad model support. It is a magic trick with a stack trace waiting backstage.
