from repository.database import Database
from domain.schemas.schemas import Criar_alocacao


class Alocacao_repository:
    def __init__(self):
        self._table_name = "tb_alocacao_equip"
        self._database = Database()
        self.supabase = self._database.obter_conexao()

    def criar_alocacao(self, dados: Criar_alocacao) -> dict:
        dados_dump = dados.model_dump()
        if hasattr(dados_dump.get("status_alocacao"), "value"):
            dados_dump["status_alocacao"] = dados_dump["status_alocacao"].value
            
        resposta = (
            self.supabase.table(self._table_name).insert(dados_dump).execute()
        )
        return resposta.data[0]

    def obter_alocacoes(self) -> list:
        resposta = self.supabase.table(self._table_name).select("*").execute()
        return resposta.data

    def obter_alocacao(self, alocacao_id: int) -> dict:
        resposta = (
            self.supabase.table(self._table_name)
            .select("*")
            .eq("alocacao_id", alocacao_id)
            .execute()
        )
        return resposta.data[0]

    def atualizar_status_alocacao(self, alocacao_id: int, novo_status: int) -> dict:
        if hasattr(novo_status, "value"):
            novo_status = novo_status.value
            
        resposta = (
            self.supabase.table(self._table_name)
            .update({"status_alocacao": novo_status})
            .eq("alocacao_id", alocacao_id)
            .execute()
        )
        return resposta.data[0]
