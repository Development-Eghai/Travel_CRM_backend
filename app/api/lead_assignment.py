# app/api/lead_assignment.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.lead_assignment import LeadAssignmentCreate, LeadAssignmentOut
from models.lead_assignment import LeadAssignment
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=LeadAssignmentOut)
def create_assignment(assignment_in: LeadAssignmentCreate, db: Session = Depends(get_db)):
    assignment = LeadAssignment(**assignment_in.model_dump())
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment

@router.get("/", response_model=List[LeadAssignmentOut])
def get_all_assignments(db: Session = Depends(get_db)):
    return db.query(LeadAssignment).all()

@router.get("/lead/{lead_id}", response_model=List[LeadAssignmentOut])
def get_assignments_by_lead(lead_id: int, db: Session = Depends(get_db)):
    return db.query(LeadAssignment).filter(LeadAssignment.lead_id == lead_id).all()

@router.get("/{assignment_id}", response_model=LeadAssignmentOut)
def get_assignment_by_id(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(LeadAssignment).filter(LeadAssignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment

@router.put("/{assignment_id}", response_model=LeadAssignmentOut)
def update_assignment(assignment_id: int, assignment_in: LeadAssignmentCreate, db: Session = Depends(get_db)):
    assignment = db.query(LeadAssignment).filter(LeadAssignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    for key, value in assignment_in.model_dump().items():
        setattr(assignment, key, value)
    db.commit()
    db.refresh(assignment)
    return assignment

@router.delete("/{assignment_id}")
def delete_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(LeadAssignment).filter(LeadAssignment.id == assignment_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    db.delete(assignment)
    db.commit()
    return {"detail": "Assignment deleted successfully"}