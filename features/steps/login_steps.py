
import logging

from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

logger = logging.getLogger(__name__)


@given("que estoy en la página de login de SauceDemo")
def step_open_login(context):
    logger.info("Abriendo la página de login")
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('ingreso el usuario "{usuario}" y la contraseña "{password}"')
def step_enter_credentials(context, usuario, password):
    logger.info("Ingresando credenciales")

    if usuario == "VACIO":
        usuario = ""

    if password == "VACIO":
        password = ""

    context.login_page.enter_username(usuario)
    context.login_page.enter_password(password)


@when("presiono el botón de login")
def step_click_login(context):
    logger.info("Presionando el botón de login")
    context.login_page.click_login()


@then("debería ingresar al catálogo de productos")
def step_validate_inventory(context):
    logger.info("Validando acceso al catálogo")
    context.inventory_page = InventoryPage(context.driver)

    assert context.inventory_page.is_loaded()
    assert context.inventory_page.get_product_title() == "Products"


@then('debería ver el mensaje de error "{mensaje}"')
def step_validate_error(context, mensaje):
    logger.info("Validando mensaje de error")
    actual = context.login_page.get_error_message()

    assert actual == mensaje
