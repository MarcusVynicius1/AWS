from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from . import models, schemas, controllers

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/livros/", response_model=schemas.LivroResponse)
def criar_livro_endpoint(livro: schemas.LivroCreate, db: Session = Depends(get_db)):
    return controllers.criar_livro(db, livro)

@app.get("/livros/", response_model=list[schemas.LivroResponse])
def listar_livros_endpoint(db: Session = Depends(get_db)):
    return controllers.listar_livros(db)

@app.get("/livros/{livro_id}", response_model=schemas.LivroResponse)
def buscar_livro_endpoint(livro_id: int, db: Session = Depends(get_db)):
    livro = controllers.buscar_livro(db, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@app.delete("/livros/{livro_id}")
def deletar_livro_endpoint(livro_id: int, db: Session = Depends(get_db)):
    livro = controllers.deletar_livro(db, livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {"message": "Livro deletado com sucesso"}