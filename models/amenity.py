#!/usr/bin/python3
"""
Amenity module
"""
from models.base_model import BaseModel
class Amenity(BaseModel):
    """Describes the Amenity class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialise Amenity; BaseModel logic"""
        super().__init__(self, *args, **kwargs)
