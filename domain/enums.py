from enum import Enum


class StatusEquipamento(Enum):
    EQUIPAMENTO_NOVO = 0
    FUNCIONANDO = 1
    DEFEITUOSO = 2
    MANUTENCAO = 3
    DESCARTE = 4

    @property
    def descricao(self) -> str:
        descricoes = {
            0: "Equipamento novo",
            1: "Funcionando",
            2: "Defeituoso",
            3: "Manutenção",
            4: "Descarte",
        }
        return descricoes[self.value]


# --- Exemplos de uso ---

# 1. Acessando um membro pelo nome
# status = StatusEquipamento.FUNCIONANDO
# print(f"Nome do Enum: {status.name}")
# print(f"Valor do Enum: {status.value}")
# print(f"Descrição: {status.descricao}")
# Saída:
# Nome do Enum: FUNCIONANDO
# Valor do Enum: 1
# Descrição: Funcionando


class StatusAlocacao(Enum):
    ENCERRADA = 0
    EM_VIGOR = 1

    @property
    def descricao(self) -> str:
        descricoes = {0: "Em vigor", 1: "Encerrada"}
        return descricoes[self.value]
