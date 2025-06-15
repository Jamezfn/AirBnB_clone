#!/usr/bin/python3
"""
State class
"""
from models.base_model import BaseModel
class State(BaseModel):
    """Describes a state class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialise state; BaseModel logic"""
        super().__init__(*args, **kwargs)
