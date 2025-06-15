#!/usr/bin/python3
"""
First User
"""
from models.base_model import BaseModel
class User(BaseModel):
    """Class user that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialise User; BaseModel logic"""
        super().__init__(self, *args, **kwargs)
