from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#createEngine estabelece a conexão com o banco de dados
#SessionLocal cria uma sessão para interagir com o banco de dados
#Base é a classe base para os modelos do SQLAlchemy

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()