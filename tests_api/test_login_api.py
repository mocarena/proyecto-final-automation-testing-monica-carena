
import pytest
from utils.api_utils import BASE_URL_REQRES, api_post


@pytest.mark.api
@pytest.mark.parametrize(
    "email, password, expected_status",
    [
        ("eve.holt@reqres.in", "cityslicka", 200),
        ("peter@reqres.in", None, 400),
    ],
)
def test_login_api(email, password, expected_status):
    url = f"{BASE_URL_REQRES}/api/login"

    payload = {"email": email}

    if password:
        payload["password"] = password

    response = api_post(url, payload)

    assert response.status_code == expected_status

    if expected_status == 200:
        data = response.json()
        assert "token" in data
        assert data["token"]
    else:
        data = response.json()
        assert "error" in data
