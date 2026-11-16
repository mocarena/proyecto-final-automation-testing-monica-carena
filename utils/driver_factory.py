import os
from selenium import webdriver


def create_driver():
    """Create and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(options=options)
