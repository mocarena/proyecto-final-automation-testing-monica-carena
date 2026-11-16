
import pytest
import requests

BASE_URL = "https://reqres.in"


@pytest.mark.api
def test_get_users():
    url = f"{BASE_URL}/api/users?page=1"

    response = requests.get(url)

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
