import pytest
from domain.schemas.schemas import Criar_historico, Historico_equipamento_response
from repository.repository_historico import Historico_repository

# --- FIXTURES ---


@pytest.fixture
def repo():
    return Historico_repository()


@pytest.fixture
def historico_criado_fixture(repo):
    dados_entrada = Criar_historico(
        equipamento_id=999,
        unidade="Registro Temporário para Teste",
        setor="setor x",
        sala="",
    )
    registro_criado = repo.criar_historico(dados_entrada)
    yield registro_criado
    repo.supabase.table(repo._table_name).delete().eq(
        "historico_id", registro_criado.historico_id
    ).execute()


# --- TESTES DE INTEGRAÇÃO ---


def test_criar_historico_integracao(repo):
    dados_entrada = Criar_historico(
        equipamento_id=1,
        unidade="Manutenção preventiva realizada",
        setor="setor x",
        sala="",
    )
    resultado = repo.criar_historico(dados_entrada)
    assert resultado is not None
    assert isinstance(resultado, Historico_equipamento_response)
    assert resultado.equipamento_id == dados_entrada.equipamento_id
    repo.supabase.table(repo._table_name).delete().eq(
        "historico_id", resultado.historico_id
    ).execute()


def test_obter_historico_por_equipamento_id_integracao(repo, historico_criado_fixture):
    equipamento_id = historico_criado_fixture.equipamento_id
    resultado = repo.obter_historico(equipamento_id=equipamento_id)
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    assert all(isinstance(h, Historico_equipamento_response) for h in resultado)
    assert all(h.equipamento_id == equipamento_id for h in resultado)


def test_obter_historico_equipamento_inexistente(repo):
    """Testa a busca por um equipamento_id que não possui registros."""
    id_inexistente = 99999999

    # Execução
    resultado = repo.obter_historico(equipamento_id=id_inexistente)

    # Asserções
    assert isinstance(resultado, list)
    assert len(resultado) == 0
