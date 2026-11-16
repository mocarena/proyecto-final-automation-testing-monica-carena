
import os
import time
import requests

# URLs base
BASE_URL_REQRES = "https://reqres.in"
BASE_URL_JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"

# Tiempo máximo de espera
TIMEOUT = 10

# Cantidad máxima de intentos ante una respuesta 429
MAX_RETRIES = 3


def request_with_retry(method, url, **kwargs):
    """Realiza solicitudes HTTP y reintenta ante respuestas 429."""

    headers = kwargs.pop("headers", {}).copy()

    if BASE_URL_REQRES in url:
        api_key = os.getenv("REQRES_API_KEY")

        if api_key:
            headers["x-api-key"] = api_key

    for attempt in range(MAX_RETRIES):
        response = requests.request(
            method,
            url,
            headers=headers,
            timeout=TIMEOUT,
            **kwargs
        )

        if response.status_code != 429:
            return response

        if attempt < MAX_RETRIES - 1:
            retry_after = response.headers.get("Retry-After")

            try:
                wait_time = float(retry_after) if retry_after else 2 ** attempt
            except ValueError:
                wait_time = 2 ** attempt

            time.sleep(min(wait_time, 10))

    return response


def api_get(url, params=None):
    return request_with_retry("GET", url, params=params)


def api_post(url, payload=None):
    return request_with_retry("POST", url, json=payload)


def api_patch(url, payload=None):
    return request_with_retry("PATCH", url, json=payload)


def api_delete(url):
    return request_with_retry("DELETE", url)
