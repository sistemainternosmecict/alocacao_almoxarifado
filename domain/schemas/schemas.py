from pydantic import BaseModel


class Categoria_equipamento_response(BaseModel):
    categoria_id: int
    categoria: str
    descricao_categoria: str


class List_categoria_equipamento_response(BaseModel):
    lista: list[Categoria_equipamento_response]
    contagem: int


class Criar_categoria(BaseModel):
    categoria: str
    descricao_categoria: str
