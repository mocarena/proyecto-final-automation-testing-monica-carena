
Feature: Login en SauceDemo

  Background:
    Given que estoy en la página de login de SauceDemo

  @ui @smoke
  Scenario: Login exitoso con usuario estándar
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And presiono el botón de login
    Then debería ingresar al catálogo de productos

  @ui @regression
  Scenario Outline: Login rechazado con credenciales incorrectas o incompletas
    When ingreso el usuario "<usuario>" y la contraseña "<password>"
    And presiono el botón de login
    Then debería ver el mensaje de error "<mensaje>"

    Examples:
      | usuario          | password      | mensaje                                                       |
      | usuario_invalido | clave_invalida | Epic sadface: Username and password do not match any user in this service  |
      | locked_out_user  | secret_sauce  | Epic sadface: Sorry, this user has been locked out.                       |
      | VACIO            | VACIO         | Epic sadface: Username is required                          |