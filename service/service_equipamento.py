from domain.schemas.schemas import (
    Criar_equipamento,
    Equipamento_response,
    List_equipamento_response,
    Atualizar_equipamento,
    Atualizar_equipamento_response,
    Atualizar_equipamento_numeros,
)
from domain.enums import StatusEquipamento
from repository.repository_equipamento import Equipamento_repository
from service.service_categoria_equipamento import Categoria_equipamento_service
from service.service_historico_equipamento import Historico_equipamento_service


class Equipamento_service:
    def __init__(self):
        self.equipamento_id: int = 0
        self.categoria_id: int = 0
        self.nome: str = ""
        self.descricao: str = ""
        self.serial: str = ""
        self.patrimonio: str = ""
        self.status_equipamento: StatusEquipamento = StatusEquipamento.EQUIPAMENTO_NOVO
        self.historico: Historico_equipamento_service
        self.categoria: Categoria_equipamento_service
        self.repository = Equipamento_repository()
        self._instanciar_historico()
        self._instanciar_categoria()

    def _instanciar_historico(self) -> None:
        self.historico = Historico_equipamento_service()

    def _instanciar_categoria(self) -> None:
        self.categoria = Categoria_equipamento_service()

    def criar_novo_equipamento(self, dados: Criar_equipamento) -> Equipamento_response:
        response = self.repository.criar_equipamento(dados)
        response["categoria"] = self.categoria.obter_categoria(
            response["categoria_id"]
        ).model_dump()
        historico_res = self.historico.obter_historico(response["equipamento_id"])
        response["historico"] = historico_res.model_dump()["lista"]
        return Equipamento_response(**response)

    def obter_equipamento(self, equipamento_id) -> Equipamento_response:
        equipamento_dict = self.repository.obter_equipamento(equipamento_id)
        equipamento_dict["categoria"] = self.categoria.obter_categoria(
            equipamento_dict["categoria_id"]
        ).model_dump()
        historico_res = self.historico.obter_historico(
            equipamento_dict["equipamento_id"]
        )
        equipamento_dict["historico"] = historico_res.model_dump()["lista"]
        return Equipamento_response(**equipamento_dict)

    def obter_equipamentos(self) -> List_equipamento_response:
        equipamento_list = self.repository.obter_equipamentos()
        for equipamento in equipamento_list:
            try:
                equipamento["categoria"] = self.categoria.obter_categoria(
                    equipamento["categoria_id"]
                ).model_dump()
            except Exception:
                equipamento["categoria"] = {
                    "categoria_id": equipamento["categoria_id"],
                    "categoria": "Desconhecida",
                    "descricao_categoria": "Categoria deletada ou não encontrada",
                }
                
            try:
                historico_res = self.historico.obter_historico(
                    equipamento["equipamento_id"]
                )
                equipamento["historico"] = historico_res.model_dump()["lista"]
            except Exception:
                equipamento["historico"] = []
                
        contagem = len(equipamento_list)
        return List_equipamento_response(lista=equipamento_list, contagem=contagem)

    def atualizar_status_equipamento(
        self, dados: Atualizar_equipamento
    ) -> Atualizar_equipamento_response:
        equipamento_id = dados.equipamento_id
        novo_status = dados.novo_status
        resposta = self.repository.atualizar_status_equipamento(
            equipamento_id, novo_status
        )
        return Atualizar_equipamento_response(
            novo_status=resposta.get("status_equipamento", novo_status),
            msg="Equipamento atualizado com sucesso"
        )

    def atualizar_registros_unicos(
        self, equipamento_id: int, dados: Atualizar_equipamento_numeros
    ) -> Equipamento_response:
        equipamento_dict = self.repository.atualizar_registros_unicos(
            equipamento_id, dados
        )
        equipamento_dict["categoria"] = self.categoria.obter_categoria(
            equipamento_dict["categoria_id"]
        ).model_dump()
        historico_res = self.historico.obter_historico(
            equipamento_dict["equipamento_id"]
        )
        equipamento_dict["historico"] = historico_res.model_dump()["lista"]
        return Equipamento_response(**equipamento_dict)
