from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, func
from database import Base

class Tarefa (Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    concluida = Column(Boolean, default=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
