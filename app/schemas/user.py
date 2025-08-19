from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    Admin = "Admin"
    Editor = "Editor"
    Agent = "Agent"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None
    mobile_number: str | None = None
    role: UserRole
    send_user_email: bool = False
    tenant_id: int

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True