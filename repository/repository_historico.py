from repository.database import Database
from domain.schemas.schemas import Criar_historico, Historico_equipamento_response


class Historico_repository:
    def __init__(self):
        self._table_name = "tb_historico_equip"
        self.database = Database()
        self.supabase = self.database.obter_conexao()

    def criar_historico(self, dados: Criar_historico) -> Historico_equipamento_response:
        resposta = (
            self.supabase.table(self._table_name).insert(dados.model_dump()).execute()
        )
        return Historico_equipamento_response(**resposta.data[0])

    def obter_historicos(self) -> list:
        resposta = self.supabase.table(self._table_name).select("*").execute()
        return [Historico_equipamento_response(**reg) for reg in resposta.data]

    def obter_historico(
        self, equipamento_id: int
    ) -> list[Historico_equipamento_response]:
        resposta = (
            self.supabase.table(self._table_name)
            .select("*")
            .eq("equipamento_id", equipamento_id)
            .execute()
        )
        return [Historico_equipamento_response(**reg) for reg in resposta.data]
