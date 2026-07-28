from fastapi import FastAPI
from routers import controller_categoria

app = FastAPI(title="Almoxarifado", version="0.1")

app.include_router(
    controller_categoria.router, prefix="/api/v1", tags=["Categoria_controller"]
)


@app.get("/api/v1/health")
def status():
    return {"status": "ok"}
