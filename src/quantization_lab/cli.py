"""Small command-line utilities for the quantization-lab research repo.

The CLI intentionally starts tiny. Commands are added only when their behavior is
implemented and testable; placeholder quantization claims would defeat the point
of the project.
"""

from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass

from quantization_lab import __version__


@dataclass(frozen=True)
class DoctorReport:
    qlab_version: str
    python: str
    platform: str
    machine: str
    mac_model: str | None
    memory_bytes: int | None
    git_available: bool


def _sysctl(name: str) -> str | None:
    if platform.system() != "Darwin" or shutil.which("sysctl") is None:
        return None
    try:
        result = subprocess.run(
            ["sysctl", "-n", name],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    value = result.stdout.strip()
    return value or None


def collect_doctor_report() -> DoctorReport:
    memory_raw = _sysctl("hw.memsize")
    try:
        memory_bytes = int(memory_raw) if memory_raw is not None else None
    except ValueError:
        memory_bytes = None

    return DoctorReport(
        qlab_version=__version__,
        python=platform.python_version(),
        platform=platform.platform(),
        machine=platform.machine(),
        mac_model=_sysctl("hw.model"),
        memory_bytes=memory_bytes,
        git_available=shutil.which("git") is not None,
    )


def _format_bytes(value: int | None) -> str:
    if value is None:
        return "unknown"
    gib = value / (1024**3)
    return f"{gib:.2f} GiB ({value} bytes)"


def doctor(as_json: bool = False) -> int:
    report = collect_doctor_report()
    if as_json:
        print(json.dumps(asdict(report), indent=2, sort_keys=True))
        return 0

    print(f"quantization-lab {report.qlab_version}")
    print(f"Python:      {report.python}")
    print(f"Platform:    {report.platform}")
    print(f"Machine:     {report.machine}")
    print(f"Mac model:   {report.mac_model or 'n/a'}")
    print(f"Memory:      {_format_bytes(report.memory_bytes)}")
    print(f"Git:         {'available' if report.git_available else 'missing'}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qlab",
        description="Research utilities for quantization-lab.",
    )
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers(dest="command", required=True)
    doctor_parser = subparsers.add_parser(
        "doctor",
        help="Report the local environment and basic hardware information.",
    )
    doctor_parser.add_argument(
        "--json",
        action="store_true",
        help="Emit a machine-readable JSON report.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return doctor(as_json=args.json)

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
