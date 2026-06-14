# models.py
from sqlalchemy import Column, Integer, String, Boolean
from database import Base
 
 
class User(Base):
    __tablename__ = "Usuarios"
 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
