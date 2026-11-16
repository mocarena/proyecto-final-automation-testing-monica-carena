
import pytest
from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    driver.maximize_window()

    yield driver

    driver.quit()
