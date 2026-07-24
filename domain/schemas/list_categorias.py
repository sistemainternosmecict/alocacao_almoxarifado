from pydantic import BaseModel
from .categoria_equipamento_response import Categoria_equipamento_response


class List_categoria_equipamento_response(BaseModel):
    lista: list[Categoria_equipamento_response]
    contagem: int
