# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
DATABASE_URL = "sqlite:///./app.db"
 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()
 
 
def get_db():
    """Dependency que fornece uma sessão do banco por requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
