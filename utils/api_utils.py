
import requests

# URLs base
BASE_URL_REQRES = "https://reqres.in"
BASE_URL_JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com"

# Tiempo máximo de espera
TIMEOUT = 10


def api_get(url, params=None):
    return requests.get(url, params=params, timeout=TIMEOUT)


def api_post(url, payload=None):
    return requests.post(url, json=payload, timeout=TIMEOUT)


def api_patch(url, payload=None):
    return requests.patch(url, json=payload, timeout=TIMEOUT)


def api_delete(url):
    return requests.delete(url, timeout=TIMEOUT)
