from fastapi import FastAPI
from app.routers import produto
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Produtos",
    description="Uma API simples para gerenciar produtos",
)

app.include_router(produto.router)
