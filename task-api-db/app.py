from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Tarefa
from database import Base, engine, SessionLocal
from datetime import datetime
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Tarefas", version="1.0.0")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TarefaSchema(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False

class TarefaResposta(TarefaSchema):
    id: int
    data_criacao: datetime

    class Config:
        orm_mode = True

@app.post("/tarefas", response_model=TarefaResposta)
def criar_tarefa(tarefa: TarefaSchema, db: Session = Depends(get_db)):
    nova_tarefa = Tarefa(
        titulo = tarefa.titulo,
        descricao = tarefa.descricao,
        concluida = tarefa.concluida
    )
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas", response_model=List[TarefaResposta])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(Tarefa).all()

@app.put("/tarefas/{tarefa_id}", response_model=TarefaResposta)
def atualizar_tarefa(tarefa_id: int, tarefa: TarefaSchema, db: Session = Depends(get_db)):
    tarefa_existente = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa_existente:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_existente.titulo = tarefa.titulo
    tarefa_existente.descricao = tarefa.descricao
    tarefa_existente.concluida = tarefa.concluida
    db.commit()
    db.refresh(tarefa_existente)
    return tarefa_existente

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    return {"message":"Tarefa deletada com sucesso"}
