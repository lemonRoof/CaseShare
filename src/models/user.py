#!/usr/bin/python3
"""holds class User"""

from .base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """Representation of a user"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    images = relationship("Image", backref="user")
    videos = relationship("Video", backref="user")
    documents = relationship("document", backref="user")
    posts = relationship("Post", backref="user")
    likes = relationship("Like", backref="user")
    comments = relationship("Comment", backref="user")
    documents = relationship("Document", backref="user")

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
