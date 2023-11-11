#!/usr/bin/python3
""" Test suite for Class FileStorage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Testing FileStorage """

    def test_all_return_value(self):
        """ Tests the return value of the all() in FileStorage """
        fs = FileStorage()
        self.assertEqual(fs.all(), {})

    def test_all_return_type(self):
        """ Tests the return type of all() """
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_new_dict_length(self):
        """
        Tests if new() adds keys to __objects of FileStorage
        by testing the length of all()
        """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        self.assertEqual(len(fs.all()), 1)

    def test_new_dict_values(self):
        """ Tests the dict detail created by new() """
        fs = FileStorage()
        bm = BaseModel()
        bm_dict = bm.to_dict()
        fs.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm_dict["id"])
        new = {key: bm_dict}
        self.assertNotEqual(fs.all(), new)
