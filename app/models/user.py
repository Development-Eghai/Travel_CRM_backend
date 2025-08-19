from sqlalchemy import Column, Integer, String, Boolean, Enum, Text, DateTime
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    Admin = "Admin"
    Editor = "Editor"
    Agent = "Agent"

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
    send_user_email = Column(Boolean, default=False)
    tenant_id = Column(Integer, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)