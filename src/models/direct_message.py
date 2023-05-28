#!/usr/bin/python
"""hold class """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, DateTime, Integer
from sqlalchemy.orm import relationship

class Direct_Message(BaseModel, Base):
    """Representation of Direct Message"""
    __tablename__ = "direct_message"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    content = Column(String(128), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id'))
    sender = relationship('User', back_populates='messages_sent', foreign_keys=[sender_id])
    receiver_id = Column(Integer, ForeignKey('users.id'))
    receiver = relationship('User', back_populates='messages_received', foreign_keys=[receiver_id])
