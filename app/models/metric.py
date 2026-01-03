from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Metric(Base):
    __tablename__ = "metrics"
    metric_id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(String(36), ForeignKey("runs.run_id"))
    auroc = Column(Float)
    auprc = Column(Float)
    f1_score = Column(Float)
    precision_at_k = Column(Float)
    recall_at_k = Column(Float)
    early_precision = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
