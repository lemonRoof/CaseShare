#!/usr/bin/python
""" holds class direct_message"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Direct_message(BaseModel, Base):
     """Representation of direct message"""
     __tablename__ = "direct_messages"
     content = Column(String(512), nullable=False)
     sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
     receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
     images = relationship("Image", backref="user", cascade="all, delete, delete-orphan")
     videos = relationship("Video", backref="user", cascade="all, delete, delete-orphan")
     likes = relationship("Like", backref="user", cascade="all, delete, delete-orphan")