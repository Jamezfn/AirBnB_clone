#!/usr/bin/python3
"""
Store first object
"""
import json
import os
import models
from models.base_model import BaseModel
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
                        self.__objects[key] = instance
                    else:
                        continue
        except Exception:
            pass
