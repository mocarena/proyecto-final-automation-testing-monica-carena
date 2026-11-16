
import logging

from behave import when, then
from pages.inventory_page import InventoryPage

logger = logging.getLogger(__name__)


@when('agrego el producto "{producto}" al carrito')
def step_add_product(context, producto):
    logger.info("Agregando producto al carrito: %s", producto)
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_product_to_cart(producto)


@then('el contador del carrito debería mostrar "{cantidad}"')
def step_validate_cart_badge(context, cantidad):
    logger.info("Validando contador del carrito")
    actual = context.inventory_page.get_cart_badge()

    assert actual == cantidad


@when("abro el carrito")
def step_open_cart(context):
    logger.info("Abriendo el carrito")
    context.inventory_page.open_cart()


@then('debería encontrar el producto "{producto}" en el carrito')
def step_validate_cart_product(context, producto):
    logger.info("Validando producto dentro del carrito")
    productos = context.inventory_page.get_cart_products()

    assert producto in productos
