from ..user import User
from ..post import Post
from ..like import Like
from ..document import Document
from ..comment import Comment
from ..image import Image
from ..video import Video
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Post": Post, "Like": Like, "Comment": Comment, "Image": Image, "Video": Video, "Document": Document}

class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CS_MYSQL_USER = getenv("CS_MYSQL_USER")
        CS_MYSQL_PWD = getenv("CS_MYSQL_PWD")
        CS_MYSQL_HOST = getenv("CS_MYSQL_HOST")
        CS_MYSQL_DB = getenv("CS_MYSQL_DB")
        CS_ENV = getenv("CS_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(CS_MYSQL_USER, CS_MYSQL_PWD, CS_MYSQL_HOST, CS_MYSQL_DB))

        if CS_ENV == "test":
            from ..base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls):
        """query on the current database session"""

        objs = []
        if cls in classes.keys():
            objs = self.__session.query(classes[cls]).all()
        elif cls in classes.values():
            objs = self.__session.query(cls).all()
        return objs
        
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload data from the database"""
        from ..base_model import Base
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Return the oject based on th call name and its ID, or None if not found"""
        if cls not in classes.values():
            return None
        return self.__session.get(cls, id)
    
    def get_user_by_email(self, email):
        """Get a user by their email address"""
        return self.__session.query(User).filter_by(email=email)

    def count(self, cls):
        """
        count the number of object in storage
        """
        return self.__session.query(cls).count()