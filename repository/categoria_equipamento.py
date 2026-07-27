from repository.database import Database
from domain.schemas.criar_categoria import Criar_categoria
from domain.schemas.categoria_equipamento_response import Categoria_equipamento_response
from domain.schemas.list_categorias import List_categoria_equipamento_response


class Categoria_repository:
    def __init__(self):
        self._table_name = "tb_categoria_equipamento"
        self.database = Database()
        self.supabase = self.database.obter_conexao()

    def criar_categoria(self, dados: Criar_categoria) -> Categoria_equipamento_response:
        resposta = (
            self.supabase.table(self._table_name).insert(dados.model_dump()).execute()
        )
        return Categoria_equipamento_response(**resposta.data[0])

    def obter_categorias(self) -> list:
        resposta = self.supabase.table(self._table_name).select("").execute()
        return [Categoria_equipamento_response(**reg) for reg in resposta.data]

    def obter_categoria(self, categoria_id: int) -> Categoria_equipamento_response:
        resposta = (
            self.supabase.table(self._table_name)
            .select("*")
            .eq("categoria_id", categoria_id)
            .execute()
        )
        return Categoria_equipamento_response(**resposta.data[0])

    # Implementar a remoção de categoria
    def remover_categoria(self, categoria_id: int):
        resposta = (
            self.supabase.table(self._table_name)
            .delete()
            .eq("categoria_id", categoria_id)
            .execute()
        )
        return resposta.data
