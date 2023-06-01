#!/usr/bin/python
"""holds calss comment"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime

class Comment(BaseModel, Base):
    """Representation of comment"""
    __tablename__ = "comments"
    content = Column(String(512), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    post_id = Column(String(60), ForeignKey("posts.id"), nullable=False)