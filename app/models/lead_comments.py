from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from ..core.database import Base
from datetime import datetime

class LeadComment(Base):
    __tablename__ = "lead_comments"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False)
    comment = Column(Text, nullable=False)
    commented_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now())