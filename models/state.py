#!/usr/bin/python3
"""Script of a class State"""

from models.base_model import BaseModel


class State(BaseModel):
    """a class State that inherit from BaseModel.

    Attributes:
        name (str): The name of the state
    """

    name = ""
