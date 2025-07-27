from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate

def get_produtos(db:Session):
    return db.query(Produto).all()
    # retorna todos os produtos


def get_produto(db: Session,id:str):
    return db.query(Produto).filter(Produto.id == id).first()
    # retorna um produto específico pelo ID

def create_produto(db: Session, produto: ProdutoCreate):
    db_produto = Produto(
        id=produto.id,
        nome=produto.nome,
        preco=produto.preco,
        quantidade=produto.quantidade
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto
    # cria um novo produto no banco de dados