from unittest.mock import MagicMock, patch
import pytest

from domain.schemas.schemas import (
    Categoria_equipamento_response,
    Criar_equipamento,
    Equipamento_response,
    List_historico_equipamento_response,
)
from service.service_equipamento import Equipamento_service


@pytest.fixture
def service_mocked():
    with (
        patch("service.service_equipamento.Equipamento_repository") as repository_cls,
        patch(
            "service.service_equipamento.Categoria_equipamento_service"
        ) as categoria_service_cls,
        patch(
            "service.service_equipamento.Historico_equipamento_service"
        ) as historico_service_cls,
    ):
        service = Equipamento_service()
        service.repository = repository_cls.return_value
        service.categoria = categoria_service_cls.return_value
        service.historico = historico_service_cls.return_value

        yield service


def test_criar_equipamento_sucesso(service_mocked):
    mock_equipamento = {
        "categoria_id": 2,
        "nome": "Pc da categoria 2",
        "descricao": "Descricao 2",
        "serial": "",
        "patrimonio": "",
    }
    criar = Criar_equipamento(**mock_equipamento)
    dados_retorno_repo = {
        "equipamento_id": 1,
        "categoria_id": 2,
        "nome": "Pc da categoria 2",
        "descricao": "Descricao 2",
        "serial": "",
        "patrimonio": "",
        "status_equipamento": 1,
    }
    service_mocked.repository.criar_equipamento.return_value = dados_retorno_repo
    mock_categoria = MagicMock()
    mock_categoria.model_dump.return_value = {"categoria_id": 2, "nome": "Categoria 2"}
    service_mocked.categoria.obter_categoria.return_value = mock_categoria
    mock_historico = MagicMock()
    mock_historico.model_dump.return_value = {"lista": [], "contagem": 0}
    service_mocked.historico.obter_historico.return_value = mock_historico
    resultado = service_mocked.criar_novo_equipamento(criar)
    service_mocked.repository.criar_equipamento.assert_called_once_with(criar)
    assert isinstance(resultado, Equipamento_response)


def test_obter_equipamento_sucesso(service_mocked):
    dados_retorno_repo = {
        "equipamento_id": 1,
        "categoria_id": 2,
        "nome": "Pc da categoria 2",
        "descricao": "Descricao 2",
        "serial": "",
        "patrimonio": "",
        "status_equipamento": 1,
    }
    service_mocked.repository.obter_equipamento.return_value = dados_retorno_repo
    mock_categoria = MagicMock()
    mock_categoria.model_dump.return_value = {"categoria_id": 2, "nome": "Categoria 2"}
    service_mocked.categoria.obter_categoria.return_value = mock_categoria
    mock_historico = MagicMock()
    mock_historico.model_dump.return_value = {"lista": [], "contagem": 0}
    service_mocked.historico.obter_historico.return_value = mock_historico
    resultado = service_mocked.obter_equipamento(dados_retorno_repo["equipamento_id"])
    service_mocked.repository.obter_equipamento.assert_called_once_with(
        dados_retorno_repo["equipamento_id"]
    )
    assert isinstance(resultado, Equipamento_response)

def test_obter_equipamentos_exceptions(service_mocked):
    dados_retorno_repo = [{
        "equipamento_id": 1,
        "categoria_id": 2,
        "nome": "Pc",
        "descricao": "Desc",
        "serial": "",
        "patrimonio": "",
        "status_equipamento": 1,
    }]
    service_mocked.repository.obter_equipamentos.return_value = dados_retorno_repo
    
    # Forcing exceptions in obter_categoria and obter_historico
    service_mocked.categoria.obter_categoria.side_effect = Exception("Not found")
    service_mocked.historico.obter_historico.side_effect = Exception("Not found")
    
    resultado = service_mocked.obter_equipamentos()
    
    assert len(resultado.lista) == 1
    equip = resultado.lista[0]
    assert equip.categoria["categoria"] == "Desconhecida"
    assert equip.historico == []
