#!/usr/bin/python3
"""
Database storage engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
import os


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for c in [State, City, User, Place, Review, Amenity]:
                objs.extend(self.__session.query(c).all())
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and the current session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()
