from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List
from datetime import datetime

from app.database.database import get_db
from app.models.link import Link
from app.models.schemas import LinkCreate, LinkResponse, LinkCreateResponse, LinkUpdate
from app.core.config import BASE_URL

router = APIRouter(tags=["links"])
redirect_router = APIRouter(tags=["redirect"])

def create_short_url(link_id: str) -> str:
    """生成完整的短链接URL"""
    return f"{BASE_URL}/{link_id}"

@router.post("/links", response_model=LinkCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_link(link_data: LinkCreate, db: Session = Depends(get_db)):
    """创建短链接"""
    # 检查ID是否已存在，如果存在则重新生成
    while True:
        new_link = Link(
            url=str(link_data.url),
            expire_at=link_data.expire_at
        )
        existing = db.query(Link).filter(Link.id == new_link.id).first()
        if not existing:
            break
    
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    
    response = LinkCreateResponse(
        id=new_link.id,
        url=new_link.url,
        short_url=create_short_url(new_link.id),
        created_at=new_link.created_at,
        expire_at=new_link.expire_at
    )
    
    return response

@router.get("/links", response_model=List[LinkResponse])
async def get_links(
    offset: int = 0, 
    limit: int = 20, 
    db: Session = Depends(get_db)
):
    """获取短链接列表"""
    links = db.query(Link).order_by(desc(Link.created_at)).offset(offset).limit(limit).all()
    
    response = []
    for link in links:
        response.append(LinkResponse(
            id=link.id,
            url=link.url,
            short_url=create_short_url(link.id),
            clicks=link.clicks,
            created_at=link.created_at,
            expire_at=link.expire_at
        ))
    
    return response

@router.get("/links/{link_id}", response_model=LinkResponse)
async def get_link(link_id: str, db: Session = Depends(get_db)):
    """获取单个短链接信息"""
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    # 检查是否过期
    if link.expire_at and datetime.utcnow() > link.expire_at:
        raise HTTPException(status_code=410, detail="Link has expired")
    
    response = LinkResponse(
        id=link.id,
        url=link.url,
        short_url=create_short_url(link.id),
        clicks=link.clicks,
        created_at=link.created_at,
        expire_at=link.expire_at
    )
    
    return response

@router.patch("/links/{link_id}")
async def update_link(
    link_id: str, 
    link_update: LinkUpdate, 
    db: Session = Depends(get_db)
):
    """更新短链接"""
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    update_data = link_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        if field == "url" and value is not None:
            setattr(link, field, str(value))
        else:
            setattr(link, field, value)
    
    db.commit()
    return {"message": "Link updated successfully"}

@router.delete("/links/{link_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(link_id: str, db: Session = Depends(get_db)):
    """删除短链接"""
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    db.delete(link)
    db.commit()

@redirect_router.get("/{link_id}")
async def redirect_link(link_id: str, db: Session = Depends(get_db)):
    """短链跳转"""
    link = db.query(Link).filter(Link.id == link_id).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    
    # 检查是否过期
    if link.expire_at and datetime.utcnow() > link.expire_at:
        raise HTTPException(status_code=410, detail="Link has expired")
    
    # 增加点击次数
    link.clicks += 1
    db.commit()
    
    return RedirectResponse(url=link.url, status_code=302)