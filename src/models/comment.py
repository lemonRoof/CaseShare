#!/usr/bin/python
"""holds calss comment"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship

class Comment(BaseModel, Base):
    """Representation of comment"""
    if models.storage_t == "db":
        __tablename__ = "comments"
        content = Column(String(60), nullable=False)
        timestamp = Column(DateTime, nullable=False)
        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        post_id = Column(Integer, ForeignKey("posts.id"), nullable=False) 

    else:
        content = ""
        timestamp = ""
        user_id = ""
        post_id = ""

    def __init__(self, *args, **kwargs):
        """initializes comment""" 
        super().__init__(*args, **kwargs)
