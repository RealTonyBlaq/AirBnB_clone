#!/usr/bin/python3
"""Script that defines te class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class Review that inherit from BaseModel"""

    place_id = " "
    user_id = " "
    text = " "
