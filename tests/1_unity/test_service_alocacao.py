from unittest.mock import MagicMock, patch
import pytest

from domain.schemas.schemas import (
    Criar_alocacao,
    Alocacao_response,
    List_alocacao_response,
    Atualizar_alocacao
)
from domain.enums import StatusAlocacao
from service.service_alocacao import Alocacao_equipamento_service


@pytest.fixture
def service_mocked():
    with (
        patch("service.service_alocacao.Alocacao_repository") as repository_cls,
        patch(
            "service.service_alocacao.Equipamento_service"
        ) as equipamento_service_cls,
    ):
        service = Alocacao_equipamento_service()
        service.repository = repository_cls.return_value
        service.equipamento_service = equipamento_service_cls.return_value

        yield service


def test_criar_alocacao_sucesso(service_mocked):
    mock_alocacao = {
        "quantidade": 10,
        "observacoes": "Alocação teste",
        "status_alocacao": StatusAlocacao.EM_VIGOR,
        "equipamentos": [1, 2]
    }
    criar = Criar_alocacao(**mock_alocacao)
    dados_retorno_repo = {
        "alocacao_id": 1,
        "quantidade": 10,
        "observacoes": "Alocação teste",
        "status_alocacao": 1,
        "equipamentos": [1, 2]
    }
    service_mocked.repository.criar_alocacao.return_value = dados_retorno_repo
    
    mock_equipamento = MagicMock()
    mock_equipamento.model_dump.return_value = {"equipamento_id": 1, "nome": "Eq 1"}
    service_mocked.equipamento_service.obter_equipamento.return_value = mock_equipamento
    
    resultado = service_mocked.criar_alocacao(criar)
    
    service_mocked.repository.criar_alocacao.assert_called_once_with(criar)
    assert isinstance(resultado, Alocacao_response)
    assert len(resultado.equipamentos) == 2


def test_obter_alocacao_sucesso(service_mocked):
    dados_retorno_repo = {
        "alocacao_id": 1,
        "quantidade": 5,
        "observacoes": "Alocação teste obter",
        "status_alocacao": 1,
        "equipamentos": [3]
    }
    service_mocked.repository.obter_alocacao.return_value = dados_retorno_repo
    
    mock_equipamento = MagicMock()
    mock_equipamento.model_dump.return_value = {"equipamento_id": 3, "nome": "Eq 3"}
    service_mocked.equipamento_service.obter_equipamento.return_value = mock_equipamento
    
    resultado = service_mocked.obter_alocacao(1)
    
    service_mocked.repository.obter_alocacao.assert_called_once_with(1)
    assert isinstance(resultado, Alocacao_response)


def test_obter_alocacoes_sucesso(service_mocked):
    dados_retorno_repo = [{
        "alocacao_id": 1,
        "quantidade": 5,
        "observacoes": "Alocação listada",
        "status_alocacao": 1,
        "equipamentos": [4]
    }]
    service_mocked.repository.obter_alocacoes.return_value = dados_retorno_repo
    
    mock_equipamento = MagicMock()
    mock_equipamento.model_dump.return_value = {"equipamento_id": 4, "nome": "Eq 4"}
    service_mocked.equipamento_service.obter_equipamento.return_value = mock_equipamento
    
    resultado = service_mocked.obter_alocacoes()
    
    assert isinstance(resultado, List_alocacao_response)
    assert resultado.contagem == 1
    assert len(resultado.lista) == 1


def test_popular_equipamentos_erro(service_mocked):
    dados_retorno_repo = [{
        "alocacao_id": 1,
        "quantidade": 5,
        "observacoes": "Alocação com erro",
        "status_alocacao": 1,
        "equipamentos": [999]
    }]
    service_mocked.repository.obter_alocacoes.return_value = dados_retorno_repo
    
    service_mocked.equipamento_service.obter_equipamento.side_effect = Exception("Not found")
    
    resultado = service_mocked.obter_alocacoes()
    
    assert len(resultado.lista) == 1
    aloc = resultado.lista[0]
    assert len(aloc.equipamentos) == 1
    assert "erro" in aloc.equipamentos[0]
