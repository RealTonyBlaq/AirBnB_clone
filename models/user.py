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
    def __init__(self, *args, **kwargs):
        '''initialize user Instance'''
        super().__init__(*args, **kwargs)
        self.email = " "
        self.password = " "
        self.first_name = " "
        self.last_name = " "

    """email = " "
    password = " "
    first_name = " "
    last_name = " "
    """

    def to_dict(self):
        '''Return dictionary representation of user'''
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            '__class__': 'User',
        })
        return user_dict
