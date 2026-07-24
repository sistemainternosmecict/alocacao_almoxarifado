from fastapi import APIRouter, status, Response, Request
from domain.schemas.criar_categoria import Criar_categoria
from domain.schemas.categoria_equipamento_response import Categoria_equipamento_response
from domain.schemas.list_categorias import List_categoria_equipamento_response
from service.categoria_equipamento import Categoria_equipamento_service

router = APIRouter()


@router.post(
    "/categoria",
    response_model=Categoria_equipamento_response,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova categoria de equipamento",
)
def criar_categoria(
    categoria: Criar_categoria, request: Request, response: Response
) -> Categoria_equipamento_response:
    categoria_service = Categoria_equipamento_service()
    service_response = categoria_service.criar_categoria(categoria)
    location = str(
        request.url_for("obter_categoria", categoria_id=service_response.categoria_id)
    )
    response.headers["Location"] = location
    return service_response


@router.get(
    "/categoria",
    response_model=List_categoria_equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Obter todas as categorias de equipamento",
)
def obter_categorias() -> List_categoria_equipamento_response:
    categoria_service = Categoria_equipamento_service()
    service_response = categoria_service.obter_categorias()
    return service_response


@router.get(
    "/categoria/{categoria_id}",
    response_model=Categoria_equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Obter uma categoria de equipamento pelo id",
)
def obter_categoria(categoria_id: int) -> Categoria_equipamento_response:
    categoria_service = Categoria_equipamento_service()
    service_response = categoria_service.obter_categoria(categoria_id)
    return service_response
