from pydantic import BaseModel


class Criar_categoria(BaseModel):
    categoria: str
    descricao_categoria: str
