#!/usr/bin/python
""" holds class image"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Image(BaseModel, Base):
    """Representation of image"""
    __tablename__ = "images"
    filename = Column(String(100), nullable=False)
    post_id = Column(String(60), ForeignKey("posts.id"), nullable=False)