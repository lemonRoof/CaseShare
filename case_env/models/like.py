import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy  import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Like(BaseModel, Base):
    """Representation of city"""
    if models.storage_t == "db":
        __tablename__ = "likes"
        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    else:
        user_id = ""
        post = ""

    def __init__(self, *agrs, **kwargs):
        """initializes like"""
        super().__init__(*agrs, **kwargs)
