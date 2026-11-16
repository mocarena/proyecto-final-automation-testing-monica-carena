# Automation Testing - Monica Carena

## Propósito

Proyecto de automatización de pruebas desarrollado con Python, Pytest, Selenium WebDriver y Requests.

El objetivo es validar funcionalidades principales de una aplicación web mediante pruebas automatizadas y ampliar la cobertura con pruebas de servicios API.

Se aplican buenas prácticas de QA, reutilización de código, parametrización, manejo de datos externos y validaciones funcionales.

## Tecnologías

- Python 3
- Selenium WebDriver 4
- Pytest
- pytest-html
- Requests
- Faker
- Google Chrome
- Git / GitHub
- CSV y JSON para datos de prueba

## Estructura del proyecto

```text
pre-entrega-automation-testing-monica-carena/
|
|-- .github/
|   |-- workflows/
|       |-- pytest.yml
|
|-- datos/
|   |-- login.csv
|   |-- productos.json
|
|-- logs/
|   |-- .gitkeep
|
|-- reports/
|   |-- .gitkeep
|
|-- tests/
|   |-- test_saucedemo.py
|   |-- test_login_csv.py
|   |-- test_carrito_json.py
|
|-- tests_api/
|   |-- test_login_api.py
|   |-- test_users_api.py
|   |-- test_create_user_api.py
|   |-- test_post_lifecycle.py
|
|-- utils/
|   |-- api_utils.py
|   |-- driver_factory.py
|   |-- datos.py
|   |-- saucedemo_helpers.py
|
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/mocarena/pre-entrega-automation-testing-monica-carena.git
cd pre-entrega-automation-testing-monica-carena
```

### 2. Crear y activar un entorno virtual


## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/mocarena/pre-entrega-automation-testing-monica-carena.git
cd pre-entrega-automation-testing-monica-carena
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

En Windows:

```powershell
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Es necesario tener Google Chrome instalado para ejecutar las pruebas web.

## Ejecución de las pruebas

Ejecutar toda la suite:

```bash
python -m pytest tests/ tests_api/ -v
```

### Pruebas web con Selenium

Ejecutar los tests de login con datos CSV:

```bash
python -m pytest tests/test_login_csv.py -v
```

Ejecutar los tests del carrito con datos JSON:

```bash
python -m pytest tests/test_carrito_json.py -v
```

Ejecutar los tests generales de SauceDemo:

```bash
python -m pytest tests/test_saucedemo.py -v
```

### Pruebas de API

Las pruebas de API se realizan utilizando Requests y el servicio ReqRes.

Ejecutar todos los tests de API:

```bash
python -m pytest -m api -v
```

Ejecutar las pruebas de login:

```bash
python -m pytest tests_api/test_login_api.py -v
```

Ejecutar las pruebas de consulta de usuarios:

```bash
python -m pytest tests_api/test_users_api.py -v
```

Ejecutar las pruebas de creación de usuarios:

```bash
python -m pytest tests_api/test_create_user_api.py -v
```

### Prueba E2E de ciclo de vida

Ejecutar el test de ciclo de vida del recurso:

```bash
python -m pytest -m e2e -v -s
```

Este escenario utiliza Faker para generar datos dinámicos y valida las operaciones:

- POST: creación de un recurso.
- PATCH: actualización del título.
- DELETE: eliminación del recurso.

Se comprueban los códigos de respuesta, los datos devueltos, los tipos y el tiempo total de ejecución.

Para este ejercicio se utiliza JSONPlaceholder, que simula las operaciones de escritura sin persistir realmente los cambios en una base de datos.


### 4. Configurar la API Key de ReqRes

Para ejecutar las pruebas contra ReqRes es necesario configurar una API Key.

En PowerShell (Windows):

```powershell
$env:REQRES_API_KEY = "TU_API_KEY"
```

La clave se utiliza mediante la variable de entorno `REQRES_API_KEY` y no debe incluirse directamente en el código ni publicarse en GitHub.

Esta configuración se mantiene durante la sesión actual de PowerShell.

### Pruebas smoke

Ejecutar las pruebas marcadas como smoke:

```bash
python -m pytest -m smoke -v
```


## Generación del reporte HTML

El proyecto utiliza pytest-html para generar automáticamente un reporte autocontenido con los resultados de toda la ejecución.

Para ejecutar las pruebas:

```bash
python -m pytest
```

El reporte se genera en:

```text
reports/report.html
```

Luego, abrir `report.html` en el navegador para consultar los resultados de la ejecución, el estado de cada test y los posibles errores.

## Casos de prueba implementados

### 1. Login y navegación

Se validan:

- Inicio de sesión con credenciales válidas.
- Redirección al inventario.
- Título de la página.
- Visualización del catálogo.
- Comportamiento ante credenciales inválidas y usuarios con restricciones.

### 2. Pruebas de login basadas en CSV

Los escenarios de autenticación se cargan desde `datos/login.csv`.

Se utiliza parametrización de Pytest para ejecutar múltiples casos con diferentes usuarios, contraseñas, resultados esperados y descripciones.

Esto facilita agregar nuevos escenarios sin duplicar la estructura del test.

### 3. Catálogo de productos

Se validan:

- Existencia de productos.
- Nombre y precio del primer producto.
- Presencia del menú.
- Presencia del selector de ordenamiento.

### 4. Carrito con datos desde JSON

Los productos se cargan desde `datos/productos.json`.

Se valida:

- Selección del botón correspondiente a cada producto.
- Incorporación del producto al carrito.
- Actualización del badge.
- Navegación a la página del carrito.
- Correspondencia entre el producto seleccionado y el producto agregado.

Los casos se parametrizan para reutilizar el mismo test con distintos productos.

### 5. Pruebas smoke

Se incluyen pruebas básicas para verificar rápidamente funcionalidades esenciales, como el login y el agregado de productos al carrito.

### 6. Login API

Se validan los escenarios de autenticación mediante POST:

- Login exitoso con credenciales válidas.
- Respuesta con token.
- Login fallido por falta de contraseña.
- Código de respuesta y contenido JSON.

### 7. Consulta de usuarios API

Se utiliza GET para consultar usuarios y validar:

- Código de respuesta.
- Existencia de datos.
- Campos obligatorios de cada usuario.
- Tipos y formato de los datos devueltos.

### 8. Creación de usuarios API

Se utiliza POST para crear usuarios con diferentes combinaciones de nombre y trabajo.

Los datos se parametrizan con Pytest y se validan:

- Código HTTP 201.
- Nombre y trabajo enviados.
- Identificador del usuario.
- Fecha de creación.

### 9. Ciclo de vida de un recurso API (E2E)

Se implementa un flujo completo utilizando POST, PATCH y DELETE sobre un mismo recurso.

Para generar los datos se utiliza Faker.

Se valida:

- Creación del recurso y obtención del ID.
- Actualización del título a "Título actualizado por QA".
- Respuesta de eliminación.
- Esquema y tipos de datos.
- Tiempo total del ciclo, con un límite de 3 segundos.

El test está identificado con el marcador `@pytest.mark.e2e`.

## Estrategias de localización y sincronización

El proyecto utiliza distintos localizadores de Selenium:

- `By.ID`
- `By.NAME`
- `By.CSS_SELECTOR`
- `By.XPATH`

Se emplean esperas explícitas con `WebDriverWait` y condiciones esperadas para sincronizar las acciones con el estado de la interfaz, evitando depender exclusivamente de esperas fijas.

## Reutilización y aislamiento

Las funciones auxiliares centralizan acciones comunes, como el inicio de sesión y las solicitudes HTTP.

El módulo `utils/api_utils.py` reúne las funciones utilizadas para realizar operaciones GET, POST, PATCH y DELETE, evitando repetir código en los tests de API.

Los fixtures de Pytest administran la preparación y limpieza del navegador, favoreciendo la independencia entre los tests.

Los datos de prueba se mantienen separados del código para facilitar su mantenimiento y ampliación.

## Consideraciones sobre los servicios API

ReqRes es un servicio externo y puede limitar temporalmente la cantidad de solicitudes recibidas.

En esos casos puede responder con HTTP 429 (Too Many Requests). Esta respuesta corresponde a una limitación del servicio y no reemplaza los códigos esperados definidos en los escenarios de prueba.

JSONPlaceholder se utiliza para practicar operaciones de escritura y ciclo de vida de recursos, aunque no persiste realmente los cambios.


## Evidencias de ejecución

El proyecto genera distintas evidencias para facilitar el seguimiento y análisis de las pruebas:

- **Reporte HTML:** resumen de los resultados de la ejecución, generado en `reports/report.html`.
- **Capturas de pantalla:** se guardan cuando una prueba UI falla.
- **Logs:** registro de la ejecución en `logs/suite.log`, con información sobre pruebas aprobadas, fallidas y salteadas.
- **GitHub Actions:** ejecución automatizada de las pruebas UI y API ante cada push o pull request a la rama main.
- **Artifacts:** reportes, capturas y logs disponibles para consultar desde las ejecuciones de GitHub Actions.

## Objetivos de aprendizaje

Este proyecto integra prácticas de automatización orientadas a:

- Diseño y ejecución de pruebas funcionales.
- Uso de Selenium WebDriver.
- Automatización de servicios API con Requests.
- Parametrización con Pytest.
- Generación de datos dinámicos con Faker.
- Gestión externa de datos con CSV y JSON.
- Sincronización mediante esperas explícitas.
- Reutilización de funciones y fixtures.
- Pruebas E2E de ciclo de vida de recursos.
- Generación de reportes y evidencias.
- Control de versiones con Git y GitHub.

## Repositorio

**Proyecto:** Automation Testing - Monica Carena

Repositorio: https://github.com/mocarena/pre-entrega-automation-testing-monica-carena