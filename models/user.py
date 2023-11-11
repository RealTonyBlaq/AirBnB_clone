#!/usr/bin/python3
"""script of class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inherit from BaseModel"""

    email = " "
    password = " "
    first_name = " "
    last_name = " "
