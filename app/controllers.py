from sqlalchemy.orm import Session
from . import models, schemas

def criar_livro(db: Session, livro: schemas.LivroCreate):
    novo_livro = models.Livro(**livro.model_dump())
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    return novo_livro

def listar_livros(db: Session):
    return db.query(models.Livro).all()

def buscar_livro(db: Session, livro_id: int):
    return db.query(models.Livro).filter(models.Livro.id == livro_id).first()

def deletar_livro(db: Session, livro_id: int):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if livro:
        db.delete(livro)
        db.commit()
    return livro