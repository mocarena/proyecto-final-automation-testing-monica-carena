
import logging
from pathlib import Path

import pytest
from pytest_html import extras

from utils.saucedemo_helpers import save_screenshot

import base64

# Configuracion del logging
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "suite.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("automation")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)

    if report.when == "call":
        if report.passed:
            logger.info("TEST PASSED: %s", item.nodeid)

        elif report.failed:
            logger.error("TEST FAILED: %s", item.nodeid)

            driver = item.funcargs.get("driver")

            if driver:
                try:
                    screenshot_path = save_screenshot(
                        driver, item.name
                    )

                    image_data = base64.b64encode(
                        Path(screenshot_path).read_bytes()
                    ).decode("utf-8")

                    report.extras = getattr(report, "extras", [])
                    report.extras.append(
                       extras.image(image_data, mime_type="image/png")
                    )

                except Exception:
                    logger.exception(
                        "No se pudo adjuntar la captura: %s",
                        item.nodeid
                    )

        elif report.skipped:
            logger.warning("TEST SKIPPED: %s", item.nodeid)

def pytest_html_report_title(report):
    report.title = "TalentoLab - Resumen de ejecucion"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata["Description"] = "Suite de pruebas UI y API"
    metadata["Author"] = "Monica Carena"