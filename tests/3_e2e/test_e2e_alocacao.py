import pytest
from fastapi.testclient import TestClient
from fastapi import status
from main import app
from domain.enums import StatusAlocacao

client = TestClient(app)

@pytest.fixture
def categoria_criada():
    payload = {"categoria": "Categoria E2E Alocacao", "descricao_categoria": "Categoria E2E"}
    response = client.post("/api/v1/categoria", json=payload)
    data = response.json()
    categoria_id = data["categoria_id"]
    yield data
    client.delete(f"/api/v1/categoria/{categoria_id}")

@pytest.fixture
def equipamento_criado(categoria_criada):
    payload = {
        "categoria_id": categoria_criada["categoria_id"],
        "nome": "Eq E2E Alocacao",
        "descricao": "Eq para teste alocacao",
        "serial": "SN-ALOC",
        "patrimonio": "PAT-ALOC"
    }
    response = client.post("/api/v1/equipamento", json=payload)
    data = response.json()
    yield data


@pytest.fixture
def alocacao_criada(equipamento_criado):
    payload = {
        "quantidade": 1,
        "observacoes": "Alocação fixture E2E",
        "status_alocacao": StatusAlocacao.EM_VIGOR.value,
        "equipamentos": [equipamento_criado["equipamento_id"]]
    }
    response = client.post("/api/v1/alocacao", json=payload)
    data = response.json()
    yield data


def test_criar_alocacao(equipamento_criado):
    payload = {
        "quantidade": 2,
        "observacoes": "Alocação teste E2E",
        "status_alocacao": StatusAlocacao.EM_VIGOR.value,
        "equipamentos": [equipamento_criado["equipamento_id"]]
    }
    response = client.post("/api/v1/alocacao", json=payload)
    data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert "alocacao_id" in data
    assert "Location" in response.headers
    assert data["observacoes"] == payload["observacoes"]


def test_obter_todas_alocacoes(alocacao_criada):
    response = client.get("/api/v1/alocacao")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert "lista" in data
    assert "contagem" in data
    assert data["contagem"] > 0
    assert len(data["lista"]) > 0


def test_obter_alocacao_por_id(alocacao_criada):
    aloc_id = alocacao_criada["alocacao_id"]
    response = client.get(f"/api/v1/alocacao/{aloc_id}")
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["alocacao_id"] == aloc_id
    assert data["observacoes"] == alocacao_criada["observacoes"]


def test_atualizar_alocacao(alocacao_criada):
    aloc_id = alocacao_criada["alocacao_id"]
    payload = {
        "alocacao_id": aloc_id,
        "novo_status": StatusAlocacao.ENCERRADA.value
    }
    
    response = client.put(f"/api/v1/alocacao/{aloc_id}", json=payload)
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "novo_status" in data
    assert data["novo_status"] == StatusAlocacao.ENCERRADA.value
