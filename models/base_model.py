#!/usr/bin/python3
"""BaseModel"""
import uuid
import models
from datetime import datetime
class BaseModel:
    """Defines commom attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize class instance with unique ID and timestamp"""
        if kwargs:
            for  key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
            self.id = getattr(self, 'id', str(uuid.uuid4()))
            self.created_at = getattr(self, 'created_at', datetime.now())
            self.updated_at = getattr(self, 'updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates a public instance attribute with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/value"""
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result
