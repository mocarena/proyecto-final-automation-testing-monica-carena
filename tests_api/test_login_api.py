
import pytest
import requests

BASE_URL = "https://reqres.in"


@pytest.mark.api
@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("eve.holt@reqres.in", "cityslicka", 200),
        ("peter@reqres.in", None, 400),
    ],
)
def test_login_api(email, password, expected_status):
    url = f"{BASE_URL}/api/login"

    payload = {"email": email}

    if password:
        payload["password"] = password

    response = requests.post(url, json=payload)

    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert "token" in data
        assert data["token"]
    else:
        data = response.json()
        assert "error" in data
