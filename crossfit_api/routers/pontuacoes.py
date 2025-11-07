from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Pontuacao, Atleta
from schemas import PontuacaoCreate, PontuacaoOut
from database import get_db

router = APIRouter(prefix="/pontuacoes", tags=["Pontuações"])

@router.post("/{atleta_id}", response_model=PontuacaoOut)
async def adicionar_pontuacao(atleta_id: int, pontuacao: PontuacaoCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Atleta).filter_by(id=atleta_id))
    atleta = result.scalars().first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")

    nova_pontuacao = Pontuacao(atleta_id=atleta_id, **pontuacao.dict())
    db.add(nova_pontuacao)
    await db.commit()
    await db.refresh(nova_pontuacao)
    return nova_pontuacao


@router.get("/", response_model=list[PontuacaoOut])
async def listar_pontuacoes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Pontuacao))
    return result.scalars().all()
