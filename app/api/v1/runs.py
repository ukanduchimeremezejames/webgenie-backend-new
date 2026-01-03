from fastapi import APIRouter, Depends
from app.services.algorithm_runner import run_algorithm
from app.core.database import AsyncSessionLocal
from app.models.run import Run
from sqlalchemy.future import select

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.post("/run")
async def run(dataset_id: str, algorithm_id: str, params: dict | None = None):
    result = await run_algorithm(dataset_id, algorithm_id, params or {})
    return result

@router.get("/")
async def list_runs(db=Depends(get_db)):
    result = await db.execute(select(Run))
    return result.scalars().all()
