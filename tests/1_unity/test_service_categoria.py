from unittest.mock import MagicMock, patch
import pytest

from domain.schemas.schemas import (
    Categoria_equipamento_response,
    Criar_categoria,
    List_categoria_equipamento_response,
)
from service.service_categoria_equipamento import Categoria_equipamento_service


@pytest.fixture
def service_mocked():
    """Fixture que descarrega a dependência do repositório criando um mock."""
    with patch(
        "service.service_categoria_equipamento.Categoria_repository"
    ) as repository_cls:
        # Instancia a classe de serviço (o __init__ usará o mock do repositório)
        service = Categoria_equipamento_service()
        # Disponibiliza a instância mockada do repositório para os testes
        service.repository = repository_cls.return_value
        yield service


def test_criar_categoria_sucesso(service_mocked):
    # Arrange
    dados_input = MagicMock(spec=Criar_categoria)
    categoria_esperada = MagicMock(spec=Categoria_equipamento_response)
    service_mocked.repository.criar_categoria.return_value = categoria_esperada

    # Act
    resultado = service_mocked.criar_categoria(dados_input)

    # Assert
    service_mocked.repository.criar_categoria.assert_called_once_with(dados_input)
    assert resultado == categoria_esperada


def test_obter_categorias_sucesso(service_mocked):
    # Arrange
    lista_mock = [
        MagicMock(spec=Categoria_equipamento_response),
        MagicMock(spec=Categoria_equipamento_response),
    ]
    service_mocked.repository.obter_categorias.return_value = lista_mock

    # Act
    with patch(
        "service.service_categoria_equipamento.List_categoria_equipamento_response"
    ) as mock_schema_list:
        mock_schema_list.return_value = "resposta_schema_formatada"
        resultado = service_mocked.obter_categorias()

        # Assert
        service_mocked.repository.obter_categorias.assert_called_once()
        mock_schema_list.assert_called_once_with(lista=lista_mock, contagem=2)
        assert resultado == "resposta_schema_formatada"


def test_obter_categoria_por_id_sucesso(service_mocked):
    # Arrange
    categoria_id = 1
    categoria_esperada = MagicMock(spec=Categoria_equipamento_response)
    service_mocked.repository.obter_categoria.return_value = categoria_esperada

    # Act
    resultado = service_mocked.obter_categoria(categoria_id)

    # Assert
    service_mocked.repository.obter_categoria.assert_called_once_with(categoria_id)
    assert resultado == categoria_esperada


def test_remover_categoria_sucesso(service_mocked):
    # Arrange
    categoria_id = 1
    retorno_esperado = [True]  # Ou o retorno esperado do método remover_categoria
    service_mocked.repository.remover_categoria.return_value = retorno_esperado

    # Act
    resultado = service_mocked.remover_categoria(categoria_id)

    # Assert
    service_mocked.repository.remover_categoria.assert_called_once_with(categoria_id)
    assert resultado == retorno_esperado
