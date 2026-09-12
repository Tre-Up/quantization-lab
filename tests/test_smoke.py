from quantization_lab import __version__
from quantization_lab.cli import collect_doctor_report, main


def test_version_is_defined() -> None:
    assert __version__


def test_doctor_report_has_basic_environment() -> None:
    report = collect_doctor_report()
    assert report.python
    assert report.platform
    assert report.machine


def test_doctor_json(capsys) -> None:
    exit_code = main(["doctor", "--json"])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert '"python"' in output
    assert '"memory_bytes"' in output
