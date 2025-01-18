from typing import Optional
from datetime import datetime

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from db.session import get_async_session
from models.applications import Application
from schemas.applications_schemas import (ApplicationCreate,
                                          Application,
                                          ApplicationsResponse)



router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=Application)
async def create_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_async_session)
):

    application = Application(
        user_name=application_data.user_name,
        description=application_data.description,
        created_at=datetime.utcnow()
    ) # pyright: ignore
    
    db.add(application)
    db.commit()
    db.refresh(application)
    
    return application

@router.get("/", response_model=ApplicationsResponse)
async def get_applications(
    user_name: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    size: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_async_session)
):
    query = select(Application)
    
    if user_name:
        query = query.filter(Application.user_name == user_name) # pyright: ignore

    total = db.scalar(select(func.count()).select_from(query.subquery()))
    query = query.offset((page - 1) * size).limit(size)
    applications = db.scalars(query).all()
    
    return ApplicationsResponse(
        items=applications, # pyright: ignore
        total=total, # pyright: ignore
        page=page,
        size=size
    ) 