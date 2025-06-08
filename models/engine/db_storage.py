#!/usr/bin/python3
"""This module defines the DBStorage class."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from os import getenv

from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """Interacts with the MySQL database using SQLAlchemy ORM."""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session all objects of the given class.
        If cls is None, queries all types of objects."""
        obj_dict = {}
        classes = [State, City]

        if cls:
            classes = [cls]

        for class_ in classes:
            results = self.__session.query(class_).all()
            for obj in results:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.remove()
