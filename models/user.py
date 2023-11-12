#!/usr/bin/python3
"""script of class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class inherit from BaseModel.

    Attributes:
        email (str): User's email
        password (str): Password of the user
        first_name (str): User's first name
        last_name (str): User's last name
    """

    email = " "
    password = " "
    first_name = " "
    last_name = " "
