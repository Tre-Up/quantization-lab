# Reproducibility Standard

A result is not complete when it works once. It is complete when another competent person can reproduce it from the repository.

## Every published experiment should pin

- model repository + exact revision/hash;
- tokenizer revision;
- calibration/search dataset identity and version;
- held-out benchmark identity and version;
- quantization backend + version/commit;
- all quantization parameters;
- random seed(s);
- decoding parameters;
- Python/package lock information;
- OS/runtime version;
- hardware description;
- context length and batch/concurrency settings.

## Result artifact

Each serious experiment should eventually produce a machine-readable record similar to:

```json
{
  "experiment_id": "...",
  "model": {"id": "...", "revision": "..."},
  "baseline": {
    "precision": "...",
    "weight_bytes": 0,
    "peak_memory_bytes": 0,
    "quality": {}
  },
  "candidate": {
    "policy": "...",
    "weight_bytes": 0,
    "peak_memory_bytes": 0,
    "quality": {}
  },
  "environment": {},
  "created_at": "..."
}
```

The schema will evolve, but raw evidence should remain machine-readable.

## Clean-room reproduction

Before v0.1:

1. clone into a fresh environment;
2. follow only public documentation;
3. run one baseline experiment;
4. run one quantized experiment;
5. reproduce the published metric within expected tolerance.

## Large artifacts

Do not commit giant model weights into Git.

Use model registries/releases/object storage where appropriate, and record immutable identifiers/checksums in the repo.

## Changes after publication

If a bug changes a published number:

- do not silently edit history;
- add a changelog entry;
- mark the old result superseded;
- publish the corrected run and reason.

Trust compounds slower than hype and evaporates faster. Annoying, but useful.
