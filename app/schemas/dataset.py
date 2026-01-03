from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DatasetCreate(BaseModel):
    name: str
    organism: Optional[str]
    type: Optional[str]

class DatasetOut(BaseModel):
    dataset_id: str
    name: str
    organism: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
