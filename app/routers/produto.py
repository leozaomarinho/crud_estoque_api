from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.produto import get_produtos, get_produto, create_produto, update_produto, delete_produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate
from fastapi import HTTPException



router = APIRouter(
    prefix="/produtos",
    tags=["produtos"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/home")
def read_root():
    return {"message": "Bem-vindo à API de Produtos"}

@router.get("/", response_model=list)
def listar_produtos(db: Session = Depends(get_db)):
    return get_produtos(db)

@router.get("/{id}", response_model=ProdutoUpdate)
def obter_produto(id: str, db: Session = Depends(get_db)):
    db_produto = get_produto(db, id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto not found")
    return db_produto

@router.post("/", response_model=ProdutoUpdate)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return create_produto(db, produto)

@router.put("/{id}", response_model=ProdutoUpdate)
def update_existing_produto(id: str, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    db_produto = update_produto(db, id, produto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto not found")
    return db_produto

@router.delete("/{id}", response_model=ProdutoUpdate)
def delete_existing_produto(id: str, db: Session = Depends(get_db)):
    db_produto = delete_produto(db, id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto not found")
    return db_produto