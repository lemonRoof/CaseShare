#!/usr/bin/python
""" holds class direct_message"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Message(BaseModel, Base):
     """Representation of direct message"""
     __tablename__ = "messages"
     content = Column(String(512), nullable=False)
     sender_id = Column(String(60), ForeignKey('users.id'), nullable=False)
     receiver_id = Column(String(60), ForeignKey('users.id'), nullable=False)

     sender = relationship("User", foreign_keys=[sender_id])
     receiver = relationship("User", foreign_keys=[receiver_id])
