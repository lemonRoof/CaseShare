#!/usr/bin/python3
"""holds class User"""

from typing import Any
from .base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

class User(BaseModel, Base):
    """Representation of a user"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    country = Column(String(128))
    title = Column(String(256))
    phone = Column(String(26))
    age = Column(Integer, default=0)
    images = relationship("Image", backref="user", cascade="all, delete, delete-orphan")
    videos = relationship("Video", backref="user", cascade="all, delete, delete-orphan")
    documents = relationship("document", backref="user", cascade="all, delete, delete-orphan")
    posts = relationship("Post", backref="user", cascade="all, delete, delete-orphan")
    likes = relationship("Like", backref="user", cascade="all, delete, delete-orphan")
    comments = relationship("Comment", backref="user", cascade="all, delete, delete-orphan")
    documents = relationship("Document", backref="user", cascade="all, delete, delete-orphan")

    def __setattr__(self, __name: str, __value: Any):
        if __name == 'password':
            self.__dict__[__name] = generate_password_hash(__value)
        else:
            super.__setattr__(self, __name, __value)