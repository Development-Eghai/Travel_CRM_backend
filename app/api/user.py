from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from schemas.user import UserCreate, UserWithKey, UserOut
from crud.user import create_user, get_users
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user, api_key = create_user(db, user)
        user_data = UserOut.model_validate(db_user).model_dump()
        return api_json_response_format(True, "User created successfully.", 201, {"user": user_data, "api_key": api_key})
    except ValueError as e:
        return api_json_response_format(False, str(e), 400, {})
    except Exception as e:
        return api_json_response_format(False, f"Unexpected error creating user: {e}", 500, {})

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    try:
        users = get_users(db)
        data = [UserOut.model_validate(u).model_dump() for u in users]
        return api_json_response_format(True, "Users retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving users: {e}", 500, {})

user_router = router