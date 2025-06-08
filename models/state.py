#!/usr/bin/python3
"""State module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    class State(BaseModel, Base):
        """State model for DB storage"""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
else:
    class State(BaseModel):
        """State model for file storage"""
        name = ""
        
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to self.id"""
            from models import storage
            from models.city import City
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
