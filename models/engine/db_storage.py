#!/usr/bin/python3
"""
DBStorage engine: uses SQLAlchemy ORM to interface with MySQL.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base, BaseModel

# import models so that they get registered on Base.metadata
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Manages persistence in a MySQL database via SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Create the engine using HBNB_MYSQL_* environment variables."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        uri = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(uri, pool_pre_ping=True)

    def all(self, cls=None):
        """
        Query on the current database session all objects of type cls,
        or all types if cls is None.
        """
        objs = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objs[key] = obj
        else:
            for model in (User, State, City, Amenity, Place, Review):
                for obj in self.__session.query(model).all():
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize a scoped session."""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """
        Called on Flask teardown: remove() will close the session
        and ensure new sessions are fresh.
        """
        self.__session.remove()
