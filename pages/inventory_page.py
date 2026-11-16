
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTS = (By.CSS_SELECTOR, "div.inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.url_contains("/inventory.html"))
        return self.driver.title == "Swag Labs"

    def get_product_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_TITLE)
        ).text

    def add_product_to_cart(self, product_name):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCTS)
        )

        for product in products:
            name = product.find_element(
                By.CSS_SELECTOR, ".inventory_item_name"
            ).text

            if name == product_name:
                product.find_element(By.CSS_SELECTOR, "button").click()
                return

        raise AssertionError(f"No se encontró el producto: {product_name}")

    def get_cart_badge(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def get_cart_products(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".cart_list")
            )
        )
        return [
            item.text
            for item in self.driver.find_elements(*self.CART_ITEMS)
        ]
