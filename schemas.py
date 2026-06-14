# schemas.py
from pydantic import BaseModel, EmailStr
 
 
class UserCreate(BaseModel):
    """Dados para criar um novo usuário."""
    username: str
    email: str
    password: str
 
 
class UserResponse(BaseModel):
    """Dados retornados ao cliente (sem a senha)."""
    id: int
    username: str
    email: str
    is_active: bool
 
    class Config:
        from_attributes = True
 
 
class Token(BaseModel):
    """Token JWT retornado após login."""
    access_token: str
    token_type: str
 
 
class TokenData(BaseModel):
    """Dados extraídos do payload do JWT."""
    username: str | None = None
