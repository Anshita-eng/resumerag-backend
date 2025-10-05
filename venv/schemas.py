from pydantic import BaseModel
from typing import Optional

class ResumeCreate(BaseModel):
    filename: str
    content: str
    email: Optional[str] = None

class ResumeOut(BaseModel):
    id: int
    filename: str
    email: Optional[str] = None
    content: str
    created_at: Optional[str] = None

    # pydantic v2-compatible config for ORM (from attributes)
    model_config = {"from_attributes": True}
