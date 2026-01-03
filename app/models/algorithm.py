from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Algorithm(Base):
    __tablename__ = "algorithms"
    algorithm_id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    version = Column(String(100))
    source_url = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
