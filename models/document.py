#!/usr/bin/python
""" holds class document"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Document(BaseModel, Base):
    """Representation of videos"""
    if models.storage_t == "db":
        __tablename__ = "Documents"
        filename = Column(String(100), nullable=False)
        post_id = Column(Integer, ForeignKey("post_id"), nullable=False)

    else:
        filename = ""
        post_id = ""

    def __init__(self, *args, **kwargs):
        """initalizes videos"""
        super().__init__(*args, **kwargs)
