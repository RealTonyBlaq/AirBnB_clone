#!/usr/bin/python3
"""Script that defines te class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class Review that inherit from BaseModel.

    Attribute:
        place_id (str): The place id
        user_id (str): User id
        text (str): Review texts
    """

    place_id = " "
    user_id = " "
    text = " "
