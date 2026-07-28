from unittest.mock import MagicMock, patch
import pytest

from domain.schemas.schemas import (
    Criar_historico,
    Historico_equipamento_response,
    List_historico_equipamento_response,
)
from service.service_historico_equipamento import Historico_equipamento_service


@pytest.fixture
def service_mocked():
    """Fixture que descarrega a dependência do repositório criando um mock."""
    with patch(
        target="service.service_historico_equipamento.Historico_repository"
    ) as repository_cls:
        # Instancia a classe de serviço (o __init__ usará o mock do repositório)
        service = Historico_equipamento_service()
        # Disponibiliza a instância mockada do repositório para os testes
        service.repository = repository_cls.return_value
        yield service


def test_criar_historico_sucesso(service_mocked):
    # Arrange
    dados_input = MagicMock(spec=Criar_historico)
    historico_esperado = MagicMock(spec=Historico_equipamento_response)
    service_mocked.repository.criar_historico.return_value = historico_esperado

    # Act
    resultado = service_mocked.criar_historico(dados_input)

    # Assert
    service_mocked.repository.criar_historico.assert_called_once_with(dados_input)
    assert resultado == historico_esperado


def test_obter_historico_sucesso(service_mocked):
    # Arrange
    equipamento_id = 1
    lista_esperada = [
        MagicMock(spec=Historico_equipamento_response),
        MagicMock(spec=Historico_equipamento_response),
    ]
    service_mocked.repository.obter_historico.return_value = lista_esperada
    retorno_esperado = List_historico_equipamento_response(
        lista=lista_esperada, contagem=2
    )

    # Act
    resultado = service_mocked.obter_historico(equipamento_id)

    # Assert
    service_mocked.repository.obter_historico.assert_called_once_with(equipamento_id)
    assert resultado == retorno_esperado


def test_contar_historico_sucesso(service_mocked):
    # Arrange
    lista_temp = ["item1", "item2", "item3"]

    # Act
    resultado = service_mocked._contar_historico(lista_temp)

    # Assert
    assert resultado == 3
