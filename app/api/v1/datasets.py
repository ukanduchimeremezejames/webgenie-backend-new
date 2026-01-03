from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from app.core.database import AsyncSessionLocal
from app.models.dataset import Dataset
from app.schemas.dataset import DatasetCreate, DatasetOut
import uuid

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/", response_model=list[DatasetOut])
async def list_datasets(db=Depends(get_db)):
    result = await db.execute(select(Dataset))
    return result.scalars().all()

@router.post("/", response_model=DatasetOut)
async def create_dataset(payload: DatasetCreate, db=Depends(get_db)):
    ds = Dataset(dataset_id=str(uuid.uuid4()), name=payload.name, organism=payload.organism, type=payload.type)
    async with db as session:
        session.add(ds)
        await session.commit()
        await session.refresh(ds)
    return ds
