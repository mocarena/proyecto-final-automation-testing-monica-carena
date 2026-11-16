
import time
import pytest
import requests
from faker import Faker


BASE_URL = "https://jsonplaceholder.typicode.com"
fake = Faker()


@pytest.mark.e2e
def test_post_lifecycle():
    start_time = time.perf_counter()

    with requests.Session() as session:

        # 1. POST: crear un post con datos aleatorios
        payload = {
            "title": fake.sentence(),
            "body": fake.text(),
            "userId": 1
        }

        post_response = session.post(
            f"{BASE_URL}/posts",
            json=payload,
            timeout=10
        )

        assert post_response.status_code == 201

        post_data = post_response.json()

        # Validaciones de esquema y tipos
        assert isinstance(post_data, dict)
        assert "id" in post_data
        assert isinstance(post_data["id"], int)
        assert post_data["title"] == payload["title"]
        assert isinstance(post_data["body"], str)

        post_id = post_data["id"]

               # 2. PATCH: actualizar el título
        updated_title = "Título actualizado por QA"

        patch_response = session.patch(
            f"{BASE_URL}/posts/{post_id}",
            json={"title": updated_title},
            timeout=10
        )

        assert patch_response.status_code == 200

        patch_data = patch_response.json()

        assert isinstance(patch_data, dict)
        assert "title" in patch_data
        assert isinstance(patch_data["title"], str)
        assert patch_data["title"] == updated_title

        # 3. DELETE: eliminar el post
        delete_response = session.delete(
            f"{BASE_URL}/posts/{post_id}",
            timeout=10
        )

        assert delete_response.status_code == 200

    # 4. Validar tiempo total del ciclo
    elapsed_time = time.perf_counter() - start_time

    print(f"\nID del post creado: {post_id}")
    print(f"Tiempo total del ciclo: {elapsed_time:.3f} segundos")

    assert elapsed_time < 3, (
        f"El ciclo superó los 3 segundos: {elapsed_time:.3f}s"
    )
