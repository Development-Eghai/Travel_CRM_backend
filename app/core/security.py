from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from app.models.api_key import APIKey

def verify_api_key(x_api_key: str = Header(...), db: Session = Depends(get_db)):
    key = db.query(APIKey).filter(APIKey.key_value == x_api_key, APIKey.is_active == True).first()
    if not key:
        raise HTTPException(status_code=403, detail="Invalid or inactive API key")
    return key
