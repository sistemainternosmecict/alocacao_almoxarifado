import pytest
from domain.schemas.schemas import Categoria_equipamento_response, Criar_categoria
from repository.categoria_equipamento import Categoria_repository


@pytest.fixture
def repo():
    """Fixture para instanciar o repositório conectado ao banco real."""
    return Categoria_repository()


@pytest.fixture
def categoria_criada_fixture(repo):
    """
    Fixture de apoio: cria uma categoria no banco antes do teste
    e garante sua remoção após a execução (Teardown).
    """
    dados_entrada = Criar_categoria(
        categoria="Teste Integração Temp",
        descricao_categoria="Categoria temporária para testes",
    )
    categoria = repo.criar_categoria(dados_entrada)

    yield categoria  # Fornece a categoria criada para o teste

    # Teardown: Limpa os dados do banco real após o teste rodar
    repo.remover_categoria(categoria.categoria_id)


def test_criar_categoria_integracao(repo):
    # 1. Dados de entrada
    dados_entrada = Criar_categoria(
        categoria="Periféricos Teste",
        descricao_categoria="Teclados e mouses de teste",
    )

    # 2. Execução no banco real
    resultado = repo.criar_categoria(dados_entrada)

    # 3. Asserções
    assert isinstance(resultado, Categoria_equipamento_response)
    assert resultado.categoria_id is not None
    assert resultado.categoria == "Periféricos Teste"
    assert resultado.descricao_categoria == "Teclados e mouses de teste"

    # Teardown manual para este teste específico
    repo.remover_categoria(resultado.categoria_id)


def test_obter_categorias_integracao(repo, categoria_criada_fixture):
    # Execução
    resultado = repo.obter_categorias()

    # Asserções
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    # Verifica se a categoria criada pela fixture está na lista retornada
    ids_categorias = [c.categoria_id for c in resultado]
    assert categoria_criada_fixture.categoria_id in ids_categorias


def test_obter_categoria_por_id_integracao(repo, categoria_criada_fixture):
    # Execução buscando pelo ID real inserido na fixture
    resultado = repo.obter_categoria(categoria_criada_fixture.categoria_id)

    # Asserções
    assert isinstance(resultado, Categoria_equipamento_response)
    assert resultado.categoria_id == categoria_criada_fixture.categoria_id
    assert resultado.categoria == categoria_criada_fixture.categoria


def test_remover_categoria_integracao(repo):
    dados_entrada = Criar_categoria(
        categoria="Para Deletar", descricao_categoria="Será excluída imediatamente"
    )
    categoria_para_deletar = repo.criar_categoria(dados_entrada)
    resultado = repo.remover_categoria(categoria_para_deletar.categoria_id)
    assert isinstance(resultado, list)
    assert len(resultado) == 1
