#!/usr/bin/python3
"""
Review
"""
from models.base_model import BaseModel
class Review(BaseModel):
    """Describes Review class"""
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """Initialise review; BaseModel logic"""
        super().__init__(*args, **kwargs)
