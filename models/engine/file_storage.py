#!/usr/bin/python3
"""
Store first object
"""
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.<id>"""
        cls_name = f"{obj.__class__.__name__}.{obj.id}"
        key = self.__objects[cls_name] = obj

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, data in obj_dict.items():
                    cls_name = data.get('__class__')
                    if cls_name == 'BaseModel':
                        instance = BaseModel(**data)
                    elif cls_name == 'User':
                        instance = User(**data)
                    elif cls_name == 'State':
                        instance = State(**data)
                    elif cls_name == 'Amenity':
                        instance = Amenity
                    elif cls_name == 'Place':
                        instance = Place(**data)
                    elif cls_name == 'Review':
                        instance = Review(**data)
                    else:
                        continue
                    self.__objects[key] = instance
        except Exception:
            pass
