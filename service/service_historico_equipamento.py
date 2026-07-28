from domain.schemas.schemas import (
    Criar_historico,
    Historico_equipamento_response,
    List_historico_equipamento_response,
)
from repository.repository_historico import Historico_repository


class Historico_equipamento_service:
    def __init__(self):
        self.repository = Historico_repository()

    def _contar_historico(self, lista_temp: list) -> int:
        return len(lista_temp)

    def criar_historico(self, dados: Criar_historico) -> Historico_equipamento_response:
        return self.repository.criar_historico(dados)

    def obter_historico(
        self, equipamento_id: int
    ) -> List_historico_equipamento_response:
        response = self.repository.obter_historico(equipamento_id)
        contagem = self._contar_historico(response)
        return List_historico_equipamento_response(lista=response, contagem=contagem)
