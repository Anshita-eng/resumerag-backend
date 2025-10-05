from sqlalchemy.orm import Session
import models, schemas

def create_resume(db: Session, resume: schemas.ResumeCreate):
    db_resume = models.Resume(
        filename=resume.filename,
        email=resume.email,
        content=resume.content
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def get_resume(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()

def list_resumes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Resume).offset(skip).limit(limit).all()
