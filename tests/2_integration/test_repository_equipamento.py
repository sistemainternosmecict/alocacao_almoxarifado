import pytest
from domain.schemas.schemas import Equipamento_response, Criar_equipamento, Atualizar_equipamento_numeros
from domain.enums import StatusEquipamento
from repository.repository_equipamento import Equipamento_repository


@pytest.fixture
def repo():
    return Equipamento_repository()


@pytest.fixture
def equipamento_criado_fixture(repo):
    dados_entrada = Criar_equipamento(
        categoria_id=1,
        nome="Exemplo de equipamento",
        descricao="Equipamento usado na bateria de testes automatizados.",
        serial="",
        patrimonio="",
    )
    equipamento = repo.criar_equipamento(dados_entrada)

    yield equipamento


def test_criar_equipamento_integracao(repo):
    dados_entrada = Criar_equipamento(
        categoria_id=2,
        nome="Exemplo de equipamento 2",
        descricao="Equipamento 2 usado na bateria de testes automatizados.",
        serial="",
        patrimonio="",
    )
    resultado = repo.criar_equipamento(dados_entrada)
    assert isinstance(resultado, dict)
    assert resultado["equipamento_id"] is not None
    assert resultado["nome"] == "Exemplo de equipamento 2"
    assert (
        resultado["descricao"]
        == "Equipamento 2 usado na bateria de testes automatizados."
    )


def test_obter_equipamentos_integracao(repo, equipamento_criado_fixture):
    resultado = repo.obter_equipamentos()
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    ids_equipamentos = [e["equipamento_id"] for e in resultado]
    assert equipamento_criado_fixture["equipamento_id"] in ids_equipamentos


def test_obter_equipamento_por_id_integracao(repo, equipamento_criado_fixture):
    resultado = repo.obter_equipamento(equipamento_criado_fixture["equipamento_id"])
    assert isinstance(resultado, dict)
    assert resultado["equipamento_id"] == equipamento_criado_fixture["equipamento_id"]
    assert resultado["nome"] == equipamento_criado_fixture["nome"]


def test_atualizar_status_equipamento(repo, equipamento_criado_fixture):
    novo_status_int = 1
    resultado = repo.atualizar_status_equipamento(
        equipamento_criado_fixture["equipamento_id"], novo_status_int
    )
    assert resultado["status_equipamento"] == novo_status_int


def test_atualizar_registros_unicos_integracao(repo, equipamento_criado_fixture):
    novo_serial = "SN-NEW-123"
    novo_patrimonio = "PAT-NEW-123"
    dados = Atualizar_equipamento_numeros(
        serial=novo_serial,
        patrimonio=novo_patrimonio
    )
    resultado = repo.atualizar_registros_unicos(
        equipamento_criado_fixture["equipamento_id"], dados
    )
    assert resultado["serial"] == novo_serial
    assert resultado["patrimonio"] == novo_patrimonio
    assert resultado["equipamento_id"] == equipamento_criado_fixture["equipamento_id"]
