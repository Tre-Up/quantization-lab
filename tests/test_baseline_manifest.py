"""Deterministic contract tests with synthetic data (not benchmark results)."""

import json

import pytest

from quantization_lab.baseline import (
    ManifestError,
    load_and_validate_manifest,
    main,
    validate_baseline_manifest,
)


@pytest.fixture
def synthetic_record():
    return {
        "schema_version": 1,
        "experiment_id": "synthetic-contract-test",
        "timestamp_utc": "2026-10-10T00:00:00Z",
        "source_commit": "synthetic-test-sha",
        "model": {
            "id": "synthetic/model",
            "revision": "synthetic-revision",
            "tokenizer_revision": "synthetic-tokenizer",
            "license": "test-only",
        },
        "device": {"name": "synthetic-device", "memory_bytes": 16_000_000_000},
        "runtime": {
            "name": "synthetic-runtime",
            "version": "0.0",
            "quantization_format": "none",
        },
        "workload": {
            "dataset_id": "synthetic-dataset",
            "dataset_revision": "synthetic-revision",
            "decoding_config_id": "synthetic-decode",
            "context_tokens": 64,
            "generated_tokens": 32,
            "seed": 0,
        },
        "metrics": {
            "weight_storage_bytes": 200,
            "resident_memory_bytes": 400,
            "peak_memory_bytes": 500,
            "ttft_ms": 10.0,
            "tokens_per_second": 3.5,
            "repetitions": 3,
        },
    }


def test_valid_contract(synthetic_record):
    assert validate_baseline_manifest(synthetic_record) is synthetic_record


@pytest.mark.parametrize("field", ["id", "revision", "tokenizer_revision", "license"])
def test_missing_model_provenance_is_rejected(synthetic_record, field):
    del synthetic_record["model"][field]
    with pytest.raises(ManifestError, match=r"model\." + field):
        validate_baseline_manifest(synthetic_record)


def test_missing_workload_metadata_is_rejected(synthetic_record):
    del synthetic_record["workload"]["decoding_config_id"]
    with pytest.raises(ManifestError, match="decoding_config_id"):
        validate_baseline_manifest(synthetic_record)


def test_invalid_memory_comparison_is_rejected(synthetic_record):
    synthetic_record["metrics"]["peak_memory_bytes"] = 300
    with pytest.raises(ManifestError, match="peak_memory_bytes"):
        validate_baseline_manifest(synthetic_record)


@pytest.mark.parametrize("bad", [True, -1, float("inf"), float("nan")])
def test_invalid_metric_is_rejected(synthetic_record, bad):
    synthetic_record["metrics"]["ttft_ms"] = bad
    with pytest.raises(ManifestError, match="ttft_ms"):
        validate_baseline_manifest(synthetic_record)


def test_load_json(tmp_path, synthetic_record):
    file = tmp_path / "record.json"
    file.write_text(json.dumps(synthetic_record), encoding="utf-8")
    assert load_and_validate_manifest(file) == synthetic_record


def test_invalid_json(tmp_path):
    file = tmp_path / "bad.json"
    file.write_text("{not json", encoding="utf-8")
    with pytest.raises(ManifestError, match="invalid JSON"):
        load_and_validate_manifest(file)


def test_cli_success(tmp_path, synthetic_record, capsys):
    file = tmp_path / "record.json"
    file.write_text(json.dumps(synthetic_record), encoding="utf-8")
    assert main([str(file)]) == 0
    assert "structurally valid" in capsys.readouterr().out


def test_cli_rejects_missing_file(tmp_path, capsys):
    assert main([str(tmp_path / "missing.json")]) == 1
    assert "Invalid baseline record" in capsys.readouterr().err
