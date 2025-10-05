from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI(title="ResumeRAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

resumes = []

# Pydantic model
class ResumeOut(BaseModel):
    id: int
    filename: str
    email: str = "example@example.com"
    content: str = "dummy content"
    created_at: str  # <-- Change to string

@app.get("/resumes/", response_model=List[ResumeOut])
async def get_resumes():
    # Convert datetime to ISO string
    return [
        {**r, "created_at": r["created_at"].isoformat()} for r in resumes
    ]

@app.post("/upload-resume/", response_model=ResumeOut)
async def upload_resume(file: UploadFile = File(...)):
    resume = {
        "id": len(resumes) + 1,
        "filename": file.filename,
        "email": "example@example.com",
        "content": "dummy content",
        "created_at": datetime.now()
    }
    resumes.append(resume)
    return {**resume, "created_at": resume["created_at"].isoformat()}

@app.post("/analyze-resume/{resume_id}")
async def analyze_resume(resume_id: int):
    resume = next((r for r in resumes if r["id"] == resume_id), None)
    if not resume:
        return {"error": "Resume not found"}
    analysis = {
        "summary": f"Analysis of {resume['filename']}",
        "skills": ["Python", "FastAPI", "React"]
    }
    return {"analysis": analysis}

