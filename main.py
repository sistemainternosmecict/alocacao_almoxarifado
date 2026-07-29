from fastapi import FastAPI
from routers import controller_categoria
from routers import controller_historico
from routers import controller_equipamento

app = FastAPI(title="Almoxarifado", version="0.1")

app.include_router(
    controller_categoria.router, prefix="/api/v1", tags=["Categoria_controller"]
)
app.include_router(
    controller_historico.router, prefix="/api/v1", tags=["Historico_controller"]
)
app.include_router(
    controller_equipamento.router, prefix="/api/v1", tags=["Equipamento_controller"]
)


@app.get("/api/v1/health")
def status():
    return {"status": "ok"}
