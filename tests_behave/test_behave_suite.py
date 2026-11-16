
import subprocess
import sys
from pathlib import Path

import pytest


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"


def run_behave(tag, report_name):
    REPORTS_DIR.mkdir(exist_ok=True)

    report_path = REPORTS_DIR / report_name

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "behave",
            f"--tags=@{tag}",
            "--format=json",
            f"--outfile={report_path}",
            "--format=pretty",
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
    )

    pretty_path = REPORTS_DIR / report_name.replace(".json", ".txt")
    pretty_path.write_text(result.stdout, encoding="utf-8")

    assert result.returncode == 0, (
        f"Falló la ejecución Behave con el tag @{tag}\n"
        f"Salida:\n{result.stdout}\n"
        f"Errores:\n{result.stderr}"
    )


@pytest.mark.bdd
@pytest.mark.smoke
def test_behave_smoke():
    """Run the BDD smoke scenarios."""
    run_behave("smoke", "behave_smoke.json")


@pytest.mark.bdd
@pytest.mark.regression
def test_behave_regression():
    """Run the BDD regression scenarios."""
    run_behave("regression", "behave_regression.json")
