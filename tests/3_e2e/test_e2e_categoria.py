import pytest
from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


@pytest.fixture
def categoria_criada():
    payload = {"categoria": "Ferramentas Elétricas", "descricao_categoria": "desc"}
    response = client.post("/api/v1/categoria", json=payload)
    data = response.json()
    categoria_id = data["categoria_id"]
    yield data  # Retorna os dados para o teste usar
    client.delete(f"/api/v1/categoria/{categoria_id}")


def test_criar_categoria():
    payload = {"categoria": "Ferramentas Elétricas", "descricao_categoria": "desc"}
    response = client.post("/api/v1/categoria", json=payload)
    data = response.json()
    categoria_id = data["categoria_id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert "categoria_id" in response.json()
    assert "Location" in response.headers
    client.delete(f"/api/v1/categoria/{categoria_id}")


def test_obter_todas_categorias():
    response = client.get("/api/v1/categoria")
    assert "lista" in response.json()
    assert "contagem" in response.json()
    assert response.status_code == status.HTTP_200_OK


def test_obter_categoria_por_id(categoria_criada):
    cat_id = categoria_criada["categoria_id"]
    response = client.get(f"/api/v1/categoria/{cat_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["categoria_id"] == cat_id


def test_remover_categoria():
    create_resp = client.post(
        "/api/v1/categoria",
        json={"categoria": "Ferramentas Elétricas 2", "descricao_categoria": "desc 2"},
    )
    cat_id = create_resp.json()["categoria_id"]

    delete_resp = client.delete(f"/api/v1/categoria/{cat_id}")
    assert delete_resp.status_code == status.HTTP_204_NO_CONTENT
