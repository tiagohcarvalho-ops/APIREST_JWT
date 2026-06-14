# main.py
from fastapi import FastAPI
from database import engine, Base
from routers import router
 
Base.metadata.create_all(bind=engine)
 
app = FastAPI(
    title="Meu Backend",
    description="API com autenticação JWT e SQLite",
    version="1.0.0",
)
 
app.include_router(router)
 
 
@app.get("/")
def root():
    return {"message": "API rodando com sucesso!"}
# main.py
from fastapi import FastAPI
from database import engine, Base
from routers import router
 
Base.metadata.create_all(bind=engine)
 
app = FastAPI(
    title="Meu Backend",
    description="API com autenticação JWT e SQLite",
    version="1.0.0",
)
 
app.include_router(router)
 
 
@app.get("/")
def root():
    return {"message": "API rodando com sucesso!"}
