#!/usr/bin/python3
""" Module for class BaseModel """

import datetime
import uuid


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self):
        """
        Initializes the attributes:

        id (str): Unique id assigned with uuid
        created_at: assigned with time when an instance is created
        updated_at: Assigned with time when an instance is created
                    and updates when public instance method save()
                    is called.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Returns a string representation of BaseModel """
        return "[{}] ({}) {}"\
            .format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attr @updated_at with the
        current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dict containing all keys/values """
        a_dict = {}
        a_dict["__class__"] = __class__.__name__
        for key in self.__dict__:
            value = getattr(self, key)
            if key == "updated_at" or key == "created_at":
                value = value.isoformat()
            a_dict[key] = value
        return a_dict