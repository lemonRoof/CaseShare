import models
from models.user import User
from models.post import Post
from models.like import Likes
from models.comment import Comment
from models.image import Image
from models.video import Video
from models.document import Document
from os import getenv
import sqlalchemy
import sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Post": Post, "Likes": Likes, "Comment": Comment, "Image": Image, "Video": Video, "Document": Document}

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
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
            return (new_dict)
        
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
        Base.matedate.create_all(self.__engine)
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
        
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
            
        return None
    
    def count(self, cls=None):
        """
        count the number of object in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

