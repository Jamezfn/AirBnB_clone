#!/usr/bin/python3
"""
City model
"""
from models.base_model import BaseModel
class City(BaseModel):
    """Describes city class"""
    state = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialises a City; BaseModel logic"""
        super().__init__(self, *args, **kwargs)
