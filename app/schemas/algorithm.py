from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlgorithmCreate(BaseModel):
    name: str
    description: Optional[str]

class AlgorithmOut(BaseModel):
    algorithm_id: str
    name: str
    description: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
