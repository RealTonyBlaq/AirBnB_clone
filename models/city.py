#!/usr/bin/python3
"""Script of a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherit from BaseModel.
    Attributes:
        state_id (str): state id
        name (str): name of the city
    """

    state_id = ""
    name = ""
