from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class ApplicationCreate(BaseModel):
    user_name: str
    description: str

class Application(ApplicationCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ApplicationsResponse(BaseModel):
    items: List[Application]
    total: int
    page: int
    size: int