
Feature: Gestión del carrito de compras

  Background:
    Given que estoy en la página de login de SauceDemo
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And presiono el botón de login
    Then debería ingresar al catálogo de productos

  @ui @regression
  Scenario: Agregar un producto al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el contador del carrito debería mostrar "1"
    When abro el carrito
    Then debería encontrar el producto "Sauce Labs Backpack" en el carrito
