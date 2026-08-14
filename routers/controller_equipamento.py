from fastapi import APIRouter, status, Response, Request
from domain.schemas.schemas import (
    Criar_equipamento,
    Equipamento_response,
    List_equipamento_response,
    Atualizar_equipamento,
    Atualizar_equipamento_response,
    Atualizar_equipamento_numeros,
)
from service.service_equipamento import Equipamento_service

router = APIRouter()


@router.post(
    "/equipamento",
    response_model=Equipamento_response,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo equipamento",
)
def criar_equipamento(
    equipamento: Criar_equipamento, request: Request, response: Response
) -> Equipamento_response:
    equipamento_service = Equipamento_service()
    service_response = equipamento_service.criar_novo_equipamento(equipamento)
    location = str(
        request.url_for(
            "obter_equipamento", equipamento_id=service_response.equipamento_id
        )
    )
    response.headers["Location"] = location
    return service_response


@router.get(
    "/equipamento",
    response_model=List_equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Obter todos os equipamentos",
)
def obter_equipamentos() -> List_equipamento_response:
    equipamento_service = Equipamento_service()
    service_response = equipamento_service.obter_equipamentos()
    return service_response.model_dump()


@router.get(
    "/equipamento/{equipamento_id}",
    response_model=Equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Obter um equipamento pelo id",
)
def obter_equipamento(equipamento_id: int) -> Equipamento_response:
    equipamento_service = Equipamento_service()
    service_response = equipamento_service.obter_equipamento(equipamento_id)
    return service_response.model_dump()


@router.put(
    "/equipamento/{equipamento_id}",
    response_model=Atualizar_equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Atualizar um equipamento pelo id",
)
def atualizar_equipamento(
    dados: Atualizar_equipamento,
) -> Atualizar_equipamento_response:
    equipamento_service = Equipamento_service()
    service_response = equipamento_service.atualizar_status_equipamento(dados)
    return service_response.model_dump()


@router.put(
    "/equipamento/registro/{equipamento_id}",
    response_model=Equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Atualizar patrimônio e serial de um equipamento pelo id",
)
def atualizar_registros_equipamento(
    equipamento_id: int, dados: Atualizar_equipamento_numeros
) -> Equipamento_response:
    equipamento_service = Equipamento_service()
    service_response = equipamento_service.atualizar_registros_unicos(
        equipamento_id, dados
    )
    return service_response.model_dump()
