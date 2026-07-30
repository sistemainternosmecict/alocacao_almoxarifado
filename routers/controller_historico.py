from fastapi import APIRouter, status, Response, Request
from domain.schemas.schemas import (
    Criar_historico,
    Historico_equipamento_response,
    List_historico_equipamento_response,
)
from service.service_historico_equipamento import Historico_equipamento_service

router = APIRouter()


@router.post(
    path="/historico",
    response_model=Historico_equipamento_response,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo histórico de equipamento",
)
def criar_historico(
    historico: Criar_historico, request: Request, response: Response
) -> Historico_equipamento_response:
    historico_service = Historico_equipamento_service()
    service_response: Historico_equipamento_response = (
        historico_service.criar_historico(dados=historico)
    )
    location = str(
        object=request.url_for(
            "obter_historico", equipamento_id=service_response.equipamento_id
        )
    )
    response.headers["Location"] = location
    return service_response


@router.get(
    path="/historico/{equipamento_id}",
    response_model=List_historico_equipamento_response,
    status_code=status.HTTP_200_OK,
    summary="Obter histórico por id do equipamento",
)
def obter_historico(
    equipamento_id: int,
) -> List_historico_equipamento_response:
    historico_service = Historico_equipamento_service()
    service_response = historico_service.obter_historico(equipamento_id=equipamento_id)
    return service_response
