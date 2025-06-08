#!/usr/bin/python3
"""
DBStorage engine: uses SQLAlchemy to interface with MySQL
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base

# import all models so that Base.metadata.create_all() will see them
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Interacts with the MySQL database via SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine using env vars"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
            pool_pre_ping=True
        )

    def all(self, cls=None):
        """Query on the current database session all objects of type cls,
        or all types if cls is None"""
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        else:
            for cl in (User, State, City, Amenity, Place, Review):
                query = self.__session.query(cl).all()
                for obj in query:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Remove or close the current session"""
        self.__session.remove()
