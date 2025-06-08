#!/usr/bin/python3
"""
FileStorage engine: serializes instances to JSON and deserializes back
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to JSON file & deserializes back"""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return dict of all objects, or those of class cls"""
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Add obj to storage dictionary with key <class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict()
                       for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for val in obj_dict.values():
                cls_name = val['__class__']
                obj = eval(f"{cls_name}(**val)")
                self.__objects[f"{cls_name}.{obj.id}"] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it exists"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)

    def close(self):
        """Call reload() for deserializing when used in Flask teardown"""
        self.reload()
