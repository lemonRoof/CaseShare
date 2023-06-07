#!/usr/bin/python
""" holds class direct_message"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Direct_message(BaseModel, Base):
     """Representation of direct message"""
     __tablename__ = "direct_messages"
     sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
     receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)