from pydantic import BaseModel

class ProdutoBase(BaseModel):
    id: int
    nome: str
    preco: float

class ProdutoCreate(ProdutoBase):
    id: str

class ProdutoUpdate(ProdutoBase):
    pass 

class ProdutoResponse(ProdutoBase):
    id: str

    class Config:
        orm_mode = True