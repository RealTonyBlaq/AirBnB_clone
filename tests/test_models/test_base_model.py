#!/usr/bin/python3
""" Unittest for BaseModel in base_model.py """

import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class """

    def test_args(self):
        """ Tests when only *args is passed """
        bm = BaseModel("name")
        self.assertNotIn("name", bm.__dict__)

    def test_args_dict(self):
        """ Tests when a list is passed as *args """
        my_list = ["age", "name"]
        bm = BaseModel(*my_list)
        self.assertNotIn("age", bm.__dict__)

    def test_args_attr(self):
        """ Tests when *args exists and **kwargs exists too """
        bm = BaseModel()
        bm.first_name = "Ifeanyi"
        bm.number = 20
        a_dict = bm.to_dict()
        new = BaseModel("last_name", "age", **a_dict)
        self.assertNotIn("age", new.__dict__)

    def test_kwargs_empty(self):
        """
        Tests the **kwargs when an empty dictionary is passed
        to see if id, created_at, updated_at instances were created
        """
        a_dict = {}
        bm = BaseModel(**a_dict)
        self.assertIsInstance(bm.id, str)

    def test_kwargs_not_empty(self):
        """ Tests the **kwargs when it is not empty """
        bm = BaseModel()
        bm.name = "Ifeanyi"
        bm.age = 15
        a_dict = bm.to_dict()
        new = BaseModel(**a_dict)
        self.assertEqual(new.age, 15)

    def test_id_type(self):
        """ Tests if the id type is a string """
        bm = BaseModel()
        self.assertEqual(type(bm.id), str)

    def test_id_randomness(self):
        """ Tests if id generates random numbers """
        bm = BaseModel()
        self.assertNotEqual(bm.id, uuid.uuid4())

    def test_created_at_instance(self):
        """ Confirms if created_at is an instance of datetime """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime.datetime)

    def test_updated_at_instance(self):
        """ Confirms if updated_at is an instance of datetime """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_updated_at_save(self):
        """ Tests if updated_at updates when save() is called """
        bm = BaseModel()
        before_save = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, before_save)

    def test_updated_at_is_not_created_at(self):
        """ Checks if attributes updated_at and created_at are not equal """
        bm = BaseModel()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_updated_at_ne_created_at(self):
        """
        Tests if created_at and updated_at are not equal after the
        public method save() is called.
        """
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)

    def test_str_type(self):
        """ Tests the string representation of BaseModel """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_save(self):
        """ Checks if updated_at updates at save() call """
        bm = BaseModel()
        before_save = bm.updated_at
        bm.save()
        self.assertNotEqual(before_save, bm.updated_at)

    def test_to_dict_type(self):
        """ Checks type of the return value of to_dict() """
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)
