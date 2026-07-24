from pydantic import BaseModel


class Categoria_equipamento_response(BaseModel):
    categoria_id: int
    categoria: str
    descricao_categoria: str
