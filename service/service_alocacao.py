from domain.schemas.schemas import (
    Criar_alocacao,
    Alocacao_response,
    List_alocacao_response,
    Atualizar_alocacao,
    Atualizar_alocacao_response,
)
from repository.repository_alocacao import Alocacao_repository
from service.service_equipamento import Equipamento_service


class Alocacao_equipamento_service:
    def __init__(self):
        self.alocacao_id: int = 0
        self.quantidade: int = 0
        self.observacoes: str = ""
        self.status_alocacao: int = 0
        self.equipamento_service: Equipamento_service
        self.repository = Alocacao_repository()
        self._instanciar_equipamento()

    def _instanciar_equipamento(self) -> None:
        self.equipamento_service = Equipamento_service()

    def _popular_equipamentos(self, alocacao_dict: dict) -> dict:
        equipamentos_ids = alocacao_dict.get("equipamentos", [])
        equipamentos_detalhados = []
        for eq_id in equipamentos_ids:
            try:
                eq_detalhe = self.equipamento_service.obter_equipamento(eq_id).model_dump()
                equipamentos_detalhados.append(eq_detalhe)
            except Exception:
                equipamentos_detalhados.append({"equipamento_id": eq_id, "erro": "Equipamento não encontrado"})
        alocacao_dict["equipamentos"] = equipamentos_detalhados
        return alocacao_dict

    def criar_alocacao(self, dados: Criar_alocacao) -> Alocacao_response:
        response = self.repository.criar_alocacao(dados)
        response = self._popular_equipamentos(response)
        return Alocacao_response(**response)

    def obter_alocacao(self, alocacao_id: int) -> Alocacao_response:
        alocacao_dict = self.repository.obter_alocacao(alocacao_id)
        alocacao_dict = self._popular_equipamentos(alocacao_dict)
        return Alocacao_response(**alocacao_dict)

    def obter_alocacoes(self) -> List_alocacao_response:
        alocacao_list = self.repository.obter_alocacoes()
        alocacoes_populadas = []
        for alocacao in alocacao_list:
            alocacoes_populadas.append(self._popular_equipamentos(alocacao))
        contagem = len(alocacoes_populadas)
        return List_alocacao_response(lista=alocacoes_populadas, contagem=contagem)

    def atualizar_status_alocacao(
        self, dados: Atualizar_alocacao
    ) -> Atualizar_alocacao_response:
        alocacao_id = dados.alocacao_id
        novo_status = dados.novo_status
        resposta = self.repository.atualizar_status_alocacao(
            alocacao_id, novo_status
        )
        return Atualizar_alocacao_response(
            novo_status=resposta.get("status_alocacao", novo_status),
            msg="Alocação atualizada com sucesso"
        )
