#!/usr/bin/python3
""" Module for class FileStorage """

from models.base_model import BaseModel
import json
import os


class FileStorage(BaseModel):
    """
    Defines a class FileStorage that:
        serializes instances to a JSON file
        deserializes JSON file to instances

    Private Class Attributes:
    -------------------------
    file_path (str): path to the JSON file
    objects (dict): stores all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Adds a key to __objects """
        key = __class__.__name__ + "." + self.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to a json file specified in __file_path """
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """ Deserializes instances from a json file if path exists """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                data = f.read()
            FileStorage.__objects = json.loads(data)