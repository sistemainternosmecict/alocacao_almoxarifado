from fastapi import FastAPI
from routers import categoria_controller

app = FastAPI(title="Almoxarifado", version="0.1")

app.include_router(
    categoria_controller.router, prefix="/api/v1", tags=["Categoria_controller"]
)


@app.get("/api/v1/health")
def status():
    return {"status": "ok"}
