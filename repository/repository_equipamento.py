from repository.database import Database
from domain.schemas.schemas import Criar_equipamento, Equipamento_response


class Equipamento_repository:
    def __init__(self):
        self._table_name = "tb_equipamentos"
        self._database = Database()
        self.supabase = self._database.obter_conexao()

    def criar_equipamento(self, dados: Criar_equipamento) -> dict:
        resposta = (
            self.supabase.table(self._table_name).insert(dados.model_dump()).execute()
        )
        return resposta.data[0]

    def obter_equipamentos(self) -> list:
        resposta = self.supabase.table(self._table_name).select("*").execute()
        return resposta.data

    def obter_equipamento(self, equipamento_id: int) -> dict:
        resposta = (
            self.supabase.table(self._table_name)
            .select("*")
            .eq("equipamento_id", equipamento_id)
            .execute()
        )
        return resposta.data[0]

    def atualizar_status_equipamento(self, equipamento_id: int, novo_status) -> dict:
        resposta = (
            self.supabase.table(self._table_name)
            .update({"status_equipamento": novo_status})
            .eq("equipamento_id", equipamento_id)
            .execute()
        )
        print(resposta)
        return resposta.data[0]
