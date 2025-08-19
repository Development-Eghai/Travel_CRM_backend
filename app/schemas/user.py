from pydantic import BaseModel, ConfigDict, EmailStr

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

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    first_name: str | None = None
    last_name: str | None = None
    mobile_number: str | None = None
    role: str
    send_user_email: bool
    tenant_id: int

    model_config = ConfigDict(from_attributes=True)
