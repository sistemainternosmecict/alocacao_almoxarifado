from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_criar_historico():
    payload = {
        "equipamento_id": 40,
        "unidade": "Unidade teste",
        "setor": "setor x",
        "sala": "Sala x",
    }
    response = client.post("/api/v1/historico", json=payload)
    data = response.json()
    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert "historico_id" in data
    assert "Location" in response.headers


def test_obter_historico():
    equipamento_id = 1
    response = client.get(f"/api/v1/historico/{equipamento_id}")
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert "lista" in data
    assert "contagem" in data
    assert len(data["lista"]) > 1
