import os
from selenium import webdriver


def create_driver():
    """Create and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--force-device-scale-factor=1")

    return webdriver.Chrome(options=options)
