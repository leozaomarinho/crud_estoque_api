from fastapi import FastAPI
from app.routers import produto
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Produtos",
    description="Uma API simples para gerenciar produtos",
)

app.include_router(produto.router, tags=["produtos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
