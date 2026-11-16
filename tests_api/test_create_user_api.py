
import pytest
import requests
from datetime import datetime

BASE_URL = "https://reqres.in"


@pytest.mark.api
@pytest.mark.parametrize(
    "name, job",
    [
        ("Monica", "QA Analyst"),
        ("Jorge", "QA Lead"),
        ("Yasmin", "Product Owner"),
        ("Josue", "Automation Tester"),
    ],
)
def test_create_user(name, job):
    url = f"{BASE_URL}/api/users"

    payload = {
        "name": name,
        "job": job
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == name
    assert data["job"] == job
    assert "id" in data
    assert "createdAt" in data
    assert data["createdAt"][:4] == str(datetime.now().year)
