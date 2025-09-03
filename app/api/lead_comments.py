from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.lead_comments import LeadComment
from schemas.lead_comments import LeadCommentCreate, LeadCommentOut

router = APIRouter()

@router.post("/", response_model=LeadCommentOut)
def create_comment(comment_in: LeadCommentCreate, db: Session = Depends(get_db)):
    comment = LeadComment(**comment_in.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


@router.get("/{lead_id}", response_model=list[LeadCommentOut])
def get_comments_for_lead(lead_id: int, db: Session = Depends(get_db)):
    return db.query(LeadComment).filter(LeadComment.lead_id == lead_id).order_by(LeadComment.created_at.desc()).all()

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(LeadComment).filter(LeadComment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(comment)
    db.commit()
    return {"detail": "Comment deleted successfully"}