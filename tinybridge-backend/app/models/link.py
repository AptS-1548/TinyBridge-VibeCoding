from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from app.database.database import Base
import secrets
import string

class Link(Base):
    __tablename__ = "links"
    
    id = Column(String, primary_key=True, index=True)
    url = Column(String, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expire_at = Column(DateTime(timezone=True), nullable=True)
    
    def __init__(self, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = self.generate_short_id()
        super().__init__(**kwargs)
    
    @staticmethod
    def generate_short_id(length=6):
        """生成短链接ID"""
        chars = string.ascii_letters + string.digits
        return ''.join(secrets.choice(chars) for _ in range(length))