from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class LinkCreate(BaseModel):
    url: HttpUrl
    expire_at: Optional[datetime] = None

class LinkUpdate(BaseModel):
    url: Optional[HttpUrl] = None
    expire_at: Optional[datetime] = None

class LinkResponse(BaseModel):
    id: str
    url: str
    short_url: str
    clicks: int
    created_at: datetime
    expire_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class LinkCreateResponse(BaseModel):
    id: str
    url: str
    short_url: str
    created_at: datetime
    expire_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True