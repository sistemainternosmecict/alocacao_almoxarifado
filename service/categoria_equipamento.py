from repository.categoria_equipamento import Categoria_repository
from domain.schemas.criar_categoria import Criar_categoria
from domain.schemas.categoria_equipamento_response import Categoria_equipamento_response
from domain.schemas.list_categorias import List_categoria_equipamento_response


class Categoria_equipamento_service:
    def __init__(self):
        self.repository = Categoria_repository()

    def criar_categoria(self, dados: Criar_categoria) -> Categoria_equipamento_response:
        response = self.repository.criar_categoria(dados)
        return response

    def obter_categorias(self) -> List_categoria_equipamento_response:
        response: list = self.repository.obter_categorias()
        list_response = {"lista": response, "contagem": len(response)}
        return List_categoria_equipamento_response(**list_response)

    def obter_categoria(self, categoria_id: int) -> Categoria_equipamento_response:
        response = self.repository.obter_categoria(categoria_id)
        return response
