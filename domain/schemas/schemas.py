from pydantic import BaseModel
from domain.enums import StatusEquipamento, StatusAlocacao


class Criar_categoria(BaseModel):
    categoria: str
    descricao_categoria: str


class Categoria_equipamento_response(BaseModel):
    categoria_id: int
    categoria: str
    descricao_categoria: str


class List_categoria_equipamento_response(BaseModel):
    lista: list[Categoria_equipamento_response]
    contagem: int


class Criar_historico(BaseModel):
    equipamento_id: int
    unidade: str
    setor: str
    sala: str


class Historico_equipamento_response(BaseModel):
    historico_id: int
    equipamento_id: int
    timestamp: str
    unidade: str
    setor: str
    sala: str


class List_historico_equipamento_response(BaseModel):
    lista: list[Historico_equipamento_response]
    contagem: int


class Criar_equipamento(BaseModel):
    categoria_id: int
    nome: str
    descricao: str
    serial: str
    patrimonio: str
    status_equipamento: StatusEquipamento


class Equipamento_response(BaseModel):
    equipamento_id: int
    categoria: Categoria_equipamento_response
    nome: str
    descricao: str
    serial: str
    patrimonio: str
    status_equpamento: StatusEquipamento
    historico: List_historico_equipamento_response


class List_equipamento_response(BaseModel):
    lista: list[Equipamento_response]
    contagem: int


class Atualizar_equipamento(BaseModel):
    novo_status: StatusEquipamento


class Atualizar_equipamento_response(BaseModel):
    novo_status: StatusEquipamento
    msg: str


class Criar_alocacao(BaseModel):
    quantidade: int
    observacoes: str
    status_alocacao: StatusAlocacao


class Alocacao_response(BaseModel):
    alocacao_id: int
    quantidade: int
    observacoes: str
    status_alocacao: StatusAlocacao
    equipamento_id: int


class List_alocacao_response(BaseModel):
    lista: list[Alocacao_response]
    contagem: int


class Atualizar_alocacao(BaseModel):
    novo_status: StatusAlocacao


class Atualizar_alocacao_response(BaseModel):
    novo_status: StatusAlocacao
    msg: str
