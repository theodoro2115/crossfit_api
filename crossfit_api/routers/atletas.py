from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Atleta
from schemas import AtletaCreate, AtletaOut
from database import get_db

router = APIRouter(prefix="/atletas", tags=["Atletas"])

@router.post("/", response_model=AtletaOut)
async def criar_atleta(atleta: AtletaCreate, db: AsyncSession = Depends(get_db)):
    novo = Atleta(**atleta.dict())
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return novo


@router.get("/", response_model=list[AtletaOut])
async def listar_atletas(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta))
    return result.scalars().all()


@router.get("/{atleta_id}", response_model=AtletaOut)
async def buscar_atleta(atleta_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta).filter_by(id=atleta_id))
    atleta = result.scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta


@router.delete("/{atleta_id}")
async def deletar_atleta(atleta_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta).filter_by(id=atleta_id))
    atleta = result.scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    await db.delete(atleta)
    await db.commit()
    return {"message": "Atleta removido com sucesso"}
