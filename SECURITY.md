# Security Policy

quantization-lab is an early research project and should not yet be treated as production security infrastructure.

## Report privately when possible

Do not publish an exploit or sensitive credential leak in a public issue.

Security-sensitive examples:

- arbitrary code execution through model loading or conversion;
- path traversal / unsafe archive handling;
- command injection;
- exposed API keys or credentials;
- malicious model metadata causing unintended execution;
- unsafe deserialization;
- supply-chain dependency compromise.

For now, use the repository owner's private GitHub contact channel if available. A dedicated security contact will be added before the first wider release.

## Model-loading policy

Treat downloaded model repositories as untrusted input.

Principles:

- avoid `trust_remote_code=True` by default;
- record when remote code is unavoidable;
- pin model revisions;
- prefer safe tensor formats;
- do not execute downloaded scripts merely to inspect a model;
- never commit secrets into configs, logs, or benchmark outputs.

## Result integrity

Manipulating benchmark files or result artifacts to change published claims is a research-integrity issue even when it is not a conventional security vulnerability.
