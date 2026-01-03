from sqlalchemy import Column, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class Run(Base):
    __tablename__ = "runs"
    run_id = Column(String(36), primary_key=True)
    dataset_id = Column(String(36), ForeignKey("datasets.dataset_id"))
    algorithm_id = Column(String(36), ForeignKey("algorithms.algorithm_id"))
    run_date = Column(DateTime, server_default=func.now())
    parameters_json = Column(JSON)
    runtime_seconds = Column(Float)
    memory_mb = Column(Float)
    provenance_hash = Column(String(255))
