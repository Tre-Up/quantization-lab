"""Validate provenance and measurement fields for reproducible baseline records.

This does not run benchmarks or assert a quantization result. It rejects records
missing enough context to compare an eventual measured baseline fairly.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


class ManifestError(ValueError):
    """The result record omits or misstates required measurement metadata."""


def _object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{path} must be an object")
    return value


def _text(obj: dict[str, Any], key: str, path: str) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{path}.{key} must be a non-empty string")


def _number(
    obj: dict[str, Any], key: str, path: str,
    *, integer: bool = False, positive: bool = True,
) -> None:
    value = obj.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ManifestError(f"{path}.{key} must be a number")
    if integer and not isinstance(value, int):
        raise ManifestError(f"{path}.{key} must be an integer")
    if not math.isfinite(value) or (positive and value <= 0) or (not positive and value < 0):
        raise ManifestError(
            f"{path}.{key} must be finite and {'positive' if positive else 'non-negative'}"
        )


def validate_baseline_manifest(payload: Any) -> dict[str, Any]:
    """Check that a baseline includes reproducible provenance and measured fields.

    Values are checked for completeness and basic consistency, not truthfulness.
    Model weights, runtime behavior and measurement methodology must still be
    independently verified on the target device.
    """
    record = _object(payload, "record")
    if record.get("schema_version") != 1:
        raise ManifestError("record.schema_version must be 1")
    for key in ("experiment_id", "timestamp_utc", "source_commit"):
        _text(record, key, "record")

    model = _object(record.get("model"), "model")
    for key in ("id", "revision", "tokenizer_revision", "license"):
        _text(model, key, "model")

    device = _object(record.get("device"), "device")
    _text(device, "name", "device")
    _number(device, "memory_bytes", "device", integer=True)

    runtime = _object(record.get("runtime"), "runtime")
    for key in ("name", "version", "quantization_format"):
        _text(runtime, key, "runtime")

    workload = _object(record.get("workload"), "workload")
    for key in ("dataset_id", "dataset_revision", "decoding_config_id"):
        _text(workload, key, "workload")
    for key in ("context_tokens", "generated_tokens", "seed"):
        _number(workload, key, "workload", integer=True, positive=(key != "seed"))

    metrics = _object(record.get("metrics"), "metrics")
    for key in (
        "weight_storage_bytes", "resident_memory_bytes", "peak_memory_bytes",
        "ttft_ms", "tokens_per_second",
    ):
        _number(metrics, key, "metrics")
    _number(metrics, "repetitions", "metrics", integer=True)
    if metrics["peak_memory_bytes"] < metrics["resident_memory_bytes"]:
        raise ManifestError(
            "metrics.peak_memory_bytes cannot be smaller than resident_memory_bytes"
        )
    return record


def load_and_validate_manifest(path: str | Path) -> dict[str, Any]:
    """Read and validate a UTF-8 JSON baseline record."""
    try:
        with Path(path).open("r", encoding="utf-8") as f:
            return validate_baseline_manifest(json.load(f))
    except json.JSONDecodeError as exc:
        raise ManifestError(f"invalid JSON: {exc.msg}") from exc


def main(argv: list[str] | None = None) -> int:
    """Validate a baseline record without running a model or modifying files."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", help="Path to a JSON baseline record")
    args = parser.parse_args(argv)
    try:
        load_and_validate_manifest(args.record)
    except (OSError, ManifestError) as exc:
        print(f"Invalid baseline record: {exc}", file=sys.stderr)
        return 1
    print(f"Baseline record is structurally valid: {args.record}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
