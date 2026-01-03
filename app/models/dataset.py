from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    dataset_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    organism = Column(String(100))
    type = Column(String(100))
    genes = Column(Integer)
    cells = Column(Integer)
    edges = Column(Integer)
    source = Column(String(50))
    last_updated = Column(DateTime)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
