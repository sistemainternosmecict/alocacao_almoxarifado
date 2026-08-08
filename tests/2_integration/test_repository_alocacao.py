import pytest
from domain.schemas.schemas import Criar_alocacao
from domain.enums import StatusAlocacao
from repository.repository_alocacao import Alocacao_repository


@pytest.fixture
def repo():
    return Alocacao_repository()


@pytest.fixture
def alocacao_criada_fixture(repo):
    dados_entrada = Criar_alocacao(
        quantidade=10,
        observacoes="Alocação fixture",
        status_alocacao=StatusAlocacao.EM_VIGOR,
        equipamentos=[1, 2]
    )
    alocacao = repo.criar_alocacao(dados_entrada)

    yield alocacao


def test_criar_alocacao_integracao(repo):
    dados_entrada = Criar_alocacao(
        quantidade=5,
        observacoes="Alocação teste integração",
        status_alocacao=StatusAlocacao.EM_VIGOR,
        equipamentos=[3, 4]
    )
    resultado = repo.criar_alocacao(dados_entrada)
    assert isinstance(resultado, dict)
    assert resultado["alocacao_id"] is not None
    assert resultado["quantidade"] == 5
    assert resultado["observacoes"] == "Alocação teste integração"


def test_obter_alocacoes_integracao(repo, alocacao_criada_fixture):
    resultado = repo.obter_alocacoes()
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    ids_alocacoes = [a["alocacao_id"] for a in resultado]
    assert alocacao_criada_fixture["alocacao_id"] in ids_alocacoes


def test_obter_alocacao_por_id_integracao(repo, alocacao_criada_fixture):
    resultado = repo.obter_alocacao(alocacao_criada_fixture["alocacao_id"])
    assert isinstance(resultado, dict)
    assert resultado["alocacao_id"] == alocacao_criada_fixture["alocacao_id"]
    assert resultado["observacoes"] == alocacao_criada_fixture["observacoes"]


def test_atualizar_status_alocacao(repo, alocacao_criada_fixture):
    novo_status_int = StatusAlocacao.ENCERRADA.value
    resultado = repo.atualizar_status_alocacao(
        alocacao_criada_fixture["alocacao_id"], novo_status_int
    )
    assert resultado["status_alocacao"] == novo_status_int
