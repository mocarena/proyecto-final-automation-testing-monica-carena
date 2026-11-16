
import pytest
from utils.api_utils import BASE_URL_REQRES, api_get


@pytest.mark.api
def test_get_users():
    url = f"{BASE_URL_REQRES}/api/users?page=1"

    response = api_get(url)

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0

    for user in data["data"]:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user
        assert user["avatar"].endswith(".jpg")
