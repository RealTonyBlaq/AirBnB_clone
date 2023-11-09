#!/usr/bin/python3
""" Module for class BaseModel """

from models import storage
import datetime
import uuid


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """
        Initializes the attributes:

        Parameters:
        -----------
        args: Non-keyworded arguments won't be used
        kwargs: Each key of this dictionary is an attribute name
                The key's value is the attribute's value

        if kwargs is empty, the attributes below are created:
        id (str): Unique id assigned with uuid
        created_at: assigned with time when an instance is created
        updated_at: Assigned with time when an instance is created
                    and updates when public instance method save()
                    is called.
        """
        args = None
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        value = datetime.datetime.fromisoformat(value)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self.to_dict())

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values including
        the __class__ key with the class name of the object """
        a_dict = {}
        a_dict["__class__"] = __class__.__name__
        for key in self.__dict__:
            value = getattr(self, key)
            if key == "updated_at" or key == "created_at":
                value = value.isoformat()
            a_dict[key] = value
        return a_dict
