#!/usr/bin/python
"""hold class """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship

if models.storage_t == "db":
    post = Table("post", Base.metadata, Column("post_id", String(60), ForeignKey("posts.id", onupdate="CASCADE"), ondelete="CASCADE"), primary_key=True)


class Post(BaseModel, Base):
    """Reperesentation of Plaece"""
    if models.storage_t == "db":
        __tablename__ = "posts"
        user_id = Column(String(60), ForeignKey("user_id"), nullable=False)
        content = Column(String(128), nullable=False)
        timestamps = Column(DateTime, nullable=False)
        comments = relationship("Comment", backref="post", cascade="all, delete, delete-orphan")
        likes = relationship("Like", backref="like", cascade="all, delete, delete, delete-orphan")

    else:
        user_id = ""
        content = ""
        timestamp = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def comments(self):
            """getter attribute returns the list of comment instances"""
            from models.comment import Comment
            comment_list = []
            all_comments = models.storage.all(Comment)
            for comment in all_comments.values():
                if comment.post_id == self.id:
                    comment_list.append(comment)
            return comment_list
            
        @property
        def likes(self):
            """getter attribute returns the list of comment instances"""
            from models.like import Like
            like_list = []
            all_likes = models.storage.all(Like)
            for like in all_likes.values():
                if like.post_id == self.id:
                    like_list.append(like)
            return like_list
