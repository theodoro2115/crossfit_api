from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)
    categoria = Column(String)

    pontuacoes = relationship("Pontuacao", back_populates="atleta", cascade="all, delete-orphan")


class Pontuacao(Base):
    __tablename__ = "pontuacoes"

    id = Column(Integer, primary_key=True, index=True)
    atleta_id = Column(Integer, ForeignKey("atletas.id"))
    evento = Column(String)
    pontos = Column(Float)

    atleta = relationship("Atleta", back_populates="pontuacoes")
