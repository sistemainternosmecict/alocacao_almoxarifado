from unittest.mock import MagicMock, patch
from domain.schemas.criar_categoria import Criar_categoria
from repository.categoria_equipamento import Categoria_repository
from domain.schemas.categoria_equipamento_response import Categoria_equipamento_response
from repository.database import Database
import pytest


def test_criar_categoria():
    repo = Categoria_repository()
    mock_supabase = MagicMock()
    repo.supabase = mock_supabase
    dados_retorno = [
        {
            "categoria_id": 1,
            "categoria": "Eletrônicos",
            "descricao_categoria": "Descricao",
        }
    ]
    mock_supabase.table.return_value.insert.return_value.execute.return_value.data = (
        dados_retorno
    )
    dados_entrada = Criar_categoria(
        categoria="Eletrônicos", descricao_categoria="Descricao"
    )
    resultado = repo.criar_categoria(dados_entrada)
    mock_supabase.table.assert_called_once_with("tb_categoria_equipamento")
    mock_supabase.table.return_value.insert.assert_called_once_with(
        dados_entrada.model_dump()
    )

    assert resultado.categoria_id == 1
    assert resultado.categoria == "Eletrônicos"


@patch("repository.categoria_equipamento.Database")
def test_obter_categorias_sucesso(mock_database_class):
    dados_falsos = [
        {
            "categoria_id": 1,
            "categoria": "Monitores",
            "descricao_categoria": "Descricao 1",
        },
        {
            "categoria_id": 2,
            "categoria": "Periféricos",
            "descricao_categoria": "Descricao 2",
        },
    ]
    mock_resposta_execute = MagicMock()
    mock_resposta_execute.data = dados_falsos
    mock_supabase = MagicMock()
    mock_supabase.table.return_value.select.return_value.execute.return_value = (
        mock_resposta_execute
    )
    mock_database_instance = MagicMock()
    mock_database_instance.obter_conexao.return_value = mock_supabase
    mock_database_class.return_value = mock_database_instance
    repo = Categoria_repository()
    resultado = repo.obter_categorias()
    mock_supabase.table.assert_called_once_with("tb_categoria_equipamento")
    mock_supabase.table().select.assert_called_once_with("")
    mock_supabase.table().select().execute.assert_called_once()
    assert len(resultado) == 2
    assert isinstance(resultado, list)
    assert resultado[0].categoria_id == 1
    assert resultado[0].categoria == "Monitores"


@patch("repository.categoria_equipamento.Database")
def test_obter_categoria_por_id_sucesso(mock_database_class):
    categoria_id_busca = 1
    dados_falsos = [
        {
            "categoria_id": categoria_id_busca,
            "categoria": "Monitores",
            "descricao_categoria": "Monitores de vídeo",
        }
    ]

    mock_resposta_execute = MagicMock()
    mock_resposta_execute.data = dados_falsos
    mock_supabase = MagicMock()
    mock_supabase.table.return_value.select.return_value.eq.return_value.execute.return_value = mock_resposta_execute
    mock_database_instance = MagicMock()
    mock_database_instance.obter_conexao.return_value = mock_supabase
    mock_database_class.return_value = mock_database_instance
    repo = Categoria_repository()
    resultado = repo.obter_categoria(categoria_id_busca)
    mock_supabase.table.assert_called_once_with("tb_categoria_equipamento")
    mock_supabase.table().select.assert_called_once_with("*")
    mock_supabase.table().select().eq.assert_called_once_with(
        "categoria_id", categoria_id_busca
    )
    mock_supabase.table().select().eq().execute.assert_called_once()
    assert isinstance(resultado, Categoria_equipamento_response)
    assert resultado.categoria_id == categoria_id_busca
    assert resultado.categoria == "Monitores"


@patch("repository.categoria_equipamento.Database")
def test_remover_categoria_sucesso(mock_database_class):
    categoria_id_busca = 1
    dados_falsos: list[dict[str, int | str]] = [
        {
            "categoria_id": categoria_id_busca,
            "categoria": "Monitores",
            "descricao_categoria": "Monitores de vídeo",
        }
    ]

    # Mock do retorno da execução do Supabase
    mock_resposta_execute = MagicMock()
    mock_resposta_execute.data = dados_falsos

    # Mock do encadeamento do Supabase: table().delete().eq().execute()
    mock_supabase = MagicMock()
    mock_supabase.table.return_value.delete.return_value.eq.return_value.execute.return_value = mock_resposta_execute

    # Configuração da classe Database mockada
    mock_database_instance = MagicMock()
    mock_database_instance.obter_conexao.return_value = mock_supabase
    mock_database_class.return_value = mock_database_instance

    # Execução do método
    repo = Categoria_repository()
    resultado = repo.remover_categoria(categoria_id_busca)

    # Asserções dos chamamentos do Supabase
    mock_supabase.table.assert_called_once_with("tb_categoria_equipamento")
    mock_supabase.table().delete.assert_called_once()
    mock_supabase.table().delete().eq.assert_called_once_with(
        "categoria_id", categoria_id_busca
    )
    mock_supabase.table().delete().eq().execute.assert_called_once()

    # Asserção do resultado retornado pelo método
    assert resultado == dados_falsos


def test_database_init_sem_variaveis_ambiente_lanca_excecao(monkeypatch):
    # 1. Simula a ausência das variáveis de ambiente temporariamente
    monkeypatch.delenv("EQUIP_SUPABASE_URL", raising=False)
    monkeypatch.delenv("EQUIP_SUPABASE_KEY", raising=False)

    # 2. Verifica se a classe dispara o ValueError esperado ao ser instanciada
    with pytest.raises(ValueError) as exc_info:
        Database()

    # 3. Asserção opcional da mensagem de erro
    assert "precisam estar configuradas no .env" in str(exc_info.value)
