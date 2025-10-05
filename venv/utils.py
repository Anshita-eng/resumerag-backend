from fastapi import UploadFile
import re
from pypdf import PdfReader

def read_upload_file_text(upload_file: UploadFile) -> str:
    """
    Reads the uploaded file and returns text.
    Supports .txt and .pdf files.
    """
    filename = upload_file.filename.lower()
    if filename.endswith(".pdf"):
        reader = PdfReader(upload_file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    else:
        # treat as txt or fallback
        raw = upload_file.file.read()
        try:
            return raw.decode("utf-8")
        except Exception:
            return raw.decode("latin-1", errors="ignore")


def extract_skills(resume_text: str):
    skills_list = ["python", "sql", "aws", "react", "django", "javascript", "java", "c++", "tableau", "excel"]
    found = [s for s in skills_list if re.search(r'\b' + re.escape(s) + r'\b', resume_text, flags=re.I)]
    return found

def generate_summary(resume_text: str):
    skills = extract_skills(resume_text)
    return {
        "skills": skills,
        "skill_count": len(skills),
        "summary": f"Found skills: {', '.join(skills)}" if skills else "No recognized skills found."
    }
