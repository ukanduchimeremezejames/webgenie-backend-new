from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from app.core.database import AsyncSessionLocal
from app.models.algorithm import Algorithm
from app.schemas.algorithm import AlgorithmOut, AlgorithmCreate
import uuid

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/", response_model=list[AlgorithmOut])
async def list_algorithms(db=Depends(get_db)):
    result = await db.execute(select(Algorithm))
    return result.scalars().all()

@router.post("/", response_model=AlgorithmOut)
async def create_algorithm(payload: AlgorithmCreate, db=Depends(get_db)):
    alg = Algorithm(algorithm_id=str(uuid.uuid4()), name=payload.name, description=payload.description)
    async with db as session:
        session.add(alg)
        await session.commit()
        await session.refresh(alg)
    return alg
