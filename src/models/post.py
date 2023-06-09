#!/usr/bin/python
"""hold class post """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship


class Post(BaseModel, Base):
    """Reperesentation of post"""
    __tablename__ = "posts"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    title = Column(String(128), nullable=False)
    content = Column(String(2048), nullable=False)
    comments = relationship("Comment", backref="post", cascade="all, delete, delete-orphan")
    likes = relationship("Like", backref="like", cascade="all, delete, delete, delete-orphan")