#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        If cls is specified, returns only objects of that class."""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary."""
        self.all().update({obj.__class__.__name__ + "." + obj.id: obj})

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, obj_data in obj_dict.items():
                cls_name = obj_data['__class__']
                cls = eval(cls_name)  # Carga la clase a partir del nombre
                self.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method to deserialize JSON file to objects."""
        self.reload()
