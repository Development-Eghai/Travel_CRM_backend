from sqlalchemy import Column, Integer, String, Boolean, Enum, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    Admin = "Admin"
    Editor = "Editor"
    Agent = "Agent"

class UserStatus(str, enum.Enum):
    Active = "Active"
    Inactive = "Inactive"
    Suspended = "Suspended"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    mobile_number = Column(String(20))
    password_hash = Column(Text, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.Active)
    # address = Column(Text)
    send_user_email = Column(Boolean, default=False)
    tenant_id = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())