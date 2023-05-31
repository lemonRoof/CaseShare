from .base_model import BaseModel, Base
from sqlalchemy  import Column, String, ForeignKey

class Like(BaseModel, Base):
    """Representation of city"""

    __tablename__ = "likes"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    post_id = Column(String(60), ForeignKey("posts.id"), nullable=False)
