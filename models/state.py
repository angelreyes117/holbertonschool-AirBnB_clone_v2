#!/usr/bin/python3
"""
State model
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os


class State(BaseModel, Base):
    """State: name + relation to City"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """FileStorage: return list of City instances with state_id == me.id"""
            from models import storage
            from models.city import City
            return [c for c in storage.all(City).values()
                    if c.state_id == self.id]
