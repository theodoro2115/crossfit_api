from pydantic import BaseModel
from typing import List

# ---------- PONTUAÇÃO ----------

class PontuacaoBase(BaseModel):
    evento: str
    pontos: float

class PontuacaoCreate(PontuacaoBase):
    pass

class PontuacaoOut(PontuacaoBase):
    id: int
    class Config:
        orm_mode = True


# ---------- ATLETA ----------

class AtletaBase(BaseModel):
    nome: str
    idade: int
    categoria: str

class AtletaCreate(AtletaBase):
    pass

class AtletaOut(AtletaBase):
    id: int
    pontuacoes: List[PontuacaoOut] = []
    class Config:
        orm_mode = True
