import pytest
from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)

@pytest.fixture
def categoria_criada():
    payload = {"categoria": "Categoria E2E Equipamento", "descricao_categoria": "Categoria para testes de equipamento"}
    response = client.post("/api/v1/categoria", json=payload)
    data = response.json()
    categoria_id = data["categoria_id"]
    yield data
    # Limpeza da categoria (se a tabela de equipamentos tiver constraint restrita, 
    # o delete pode falhar pois não temos rota de DELETE de equipamento).
    client.delete(f"/api/v1/categoria/{categoria_id}")

@pytest.fixture
def equipamento_criado(categoria_criada):
    payload = {
        "categoria_id": categoria_criada["categoria_id"],
        "nome": "Equipamento E2E Fixture",
        "descricao": "Equipamento criado via fixture para testes E2E",
        "serial": "E2E-123",
        "patrimonio": "PAT-E2E"
    }
    response = client.post("/api/v1/equipamento", json=payload)
    data = response.json()
    yield data
    # Não existe endpoint de deleção de equipamento implementado no controller_equipamento.py ainda

def test_criar_equipamento(categoria_criada):
    payload = {
        "categoria_id": categoria_criada["categoria_id"],
        "nome": "Equipamento Teste Criacao",
        "descricao": "Equipamento E2E teste criação",
        "serial": "SN-9999",
        "patrimonio": "PAT-9999"
    }
    response = client.post("/api/v1/equipamento", json=payload)
    data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert "equipamento_id" in data
    assert "Location" in response.headers
    assert data["nome"] == payload["nome"]
    assert data["descricao"] == payload["descricao"]


def test_obter_todos_equipamentos(equipamento_criado):
    response = client.get("/api/v1/equipamento")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert "lista" in data
    assert "contagem" in data
    assert data["contagem"] > 0
    assert len(data["lista"]) > 0


def test_obter_equipamento_por_id(equipamento_criado):
    eq_id = equipamento_criado["equipamento_id"]
    response = client.get(f"/api/v1/equipamento/{eq_id}")
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["equipamento_id"] == eq_id
    assert data["nome"] == equipamento_criado["nome"]


def test_atualizar_equipamento(equipamento_criado):
    eq_id = equipamento_criado["equipamento_id"]
    # Payload baseando-se no schema Atualizar_equipamento
    payload = {
        "equipamento_id": eq_id,
        "novo_status": 1
    }
    
    response = client.put(f"/api/v1/equipamento/{eq_id}", json=payload)
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "novo_status" in data
    assert data["novo_status"] == 1
