from sqlalchemy.orm import Session
from app import schemas, models
from app.schemas import ProdutoCreate, ProdutoUpdate

class ProdutoService:

    @staticmethod
    def criar_produto(db: Session, produto: schemas.ProdutoCreate):
        db_produto = models.Produto(
            nome=produto.nome,
            preco=produto.preco,
            quantidade=produto.quantidade
        )
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    
    @staticmethod
    def listar_produtos(db: Session):
        return db.query(models.Produto).all()
    
    @staticmethod
    def obter_produto(db: Session, produto_id: int):
        return db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    
    @staticmethod

    def atualizar_produto(db: Session, produto_id: int, produto: schemas.ProdutoCreate):
        db_produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
        if not db_produto:
            return None
        for key, value in produto.dict(exclude_unset=True).items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    
    def excluir_produto(db: Session, produto_id: int):
        db_produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
        if not db_produto:
            return None
        db.delete(db_produto)
        db.commit()
        return db_produto
    
