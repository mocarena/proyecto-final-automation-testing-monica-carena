
import logging
import re
from pathlib import Path
from datetime import datetime

from utils.driver_factory import create_driver

logger = logging.getLogger(__name__)


def before_scenario(context, scenario):
    """Start a new browser for each scenario."""
    logger.info("Iniciando escenario BDD: %s", scenario.name)
    context.driver = create_driver()
    context.driver.maximize_window()


def after_step(context, step):
    """Take a screenshot when a step fails or raises an error."""
    if step.status in ("failed", "error"):
        screens_dir = Path("reports/screens")
        screens_dir.mkdir(parents=True, exist_ok=True)

        scenario_name = re.sub(
            r"[^a-zA-Z0-9_-]", "_", context.scenario.name
        )
        step_name = re.sub(
            r"[^a-zA-Z0-9_-]", "_", step.name
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{scenario_name}_{step_name}_{timestamp}.png"
        screenshot_path = screens_dir / filename

        if getattr(context, "driver", None):
            context.driver.save_screenshot(str(screenshot_path))
            logger.error("Captura guardada: %s", screenshot_path)


def after_scenario(context, scenario):
    """Close the browser after each scenario."""
    driver = getattr(context, "driver", None)

    if driver:
        driver.quit()

    logger.info("Finalizó escenario BDD: %s", scenario.name)
