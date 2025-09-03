# app/api/role.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.role import RoleCreate, RoleOut
from models.role import Role
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=RoleOut)
def create_role(role_in: RoleCreate, db: Session = Depends(get_db)):
    role = Role(**role_in.model_dump())
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

@router.get("/", response_model=List[RoleOut])
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.put("/{role_id}", response_model=RoleOut)
def update_role(role_id: int, role_in: RoleCreate, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    for key, value in role_in.model_dump().items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(role)
    db.commit()
    return {"detail": "Role deleted"}