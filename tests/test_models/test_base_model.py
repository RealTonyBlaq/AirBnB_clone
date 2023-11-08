#!/usr/bin/python3
""" Test cases for BaseModel in base_model.py """

import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """ Tests for the BaseModel class """

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
