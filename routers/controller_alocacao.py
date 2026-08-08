from fastapi import APIRouter, status, Response, Request
from domain.schemas.schemas import (
    Criar_alocacao,
    Alocacao_response,
    List_alocacao_response,
    Atualizar_alocacao,
    Atualizar_alocacao_response,
)
from service.service_alocacao import Alocacao_equipamento_service

router = APIRouter()


@router.post(
    "/alocacao",
    response_model=Alocacao_response,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova alocação",
)
def criar_alocacao(
    alocacao: Criar_alocacao, request: Request, response: Response
) -> Alocacao_response:
    alocacao_service = Alocacao_equipamento_service()
    service_response = alocacao_service.criar_alocacao(alocacao)
    location = str(
        request.url_for(
            "obter_alocacao", alocacao_id=service_response.alocacao_id
        )
    )
    response.headers["Location"] = location
    return service_response


@router.get(
    "/alocacao",
    response_model=List_alocacao_response,
    status_code=status.HTTP_200_OK,
    summary="Obter todas as alocações",
)
def obter_alocacoes() -> List_alocacao_response:
    alocacao_service = Alocacao_equipamento_service()
    service_response = alocacao_service.obter_alocacoes()
    return service_response.model_dump()


@router.get(
    "/alocacao/{alocacao_id}",
    response_model=Alocacao_response,
    status_code=status.HTTP_200_OK,
    summary="Obter uma alocação pelo id",
)
def obter_alocacao(alocacao_id: int) -> Alocacao_response:
    alocacao_service = Alocacao_equipamento_service()
    service_response = alocacao_service.obter_alocacao(alocacao_id)
    return service_response.model_dump()


@router.put(
    "/alocacao/{alocacao_id}",
    response_model=Atualizar_alocacao_response,
    status_code=status.HTTP_200_OK,
    summary="Atualizar o status de uma alocação pelo id",
)
def atualizar_alocacao(
    alocacao_id: int,
    dados: Atualizar_alocacao,
) -> Atualizar_alocacao_response:
    # Ensure ID matches payload
    dados.alocacao_id = alocacao_id
    alocacao_service = Alocacao_equipamento_service()
    service_response = alocacao_service.atualizar_status_alocacao(dados)
    return service_response.model_dump()
