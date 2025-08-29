from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.user import UserCreate, UserWithKey, UserOut
from app.crud.user import create_user, get_users

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserWithKey)
def create(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user, api_key = create_user(db, user)
        return {"user": db_user, "api_key": api_key}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserOut])
def read_all(db: Session = Depends(get_db)):
    return get_users(db)


user_router = router