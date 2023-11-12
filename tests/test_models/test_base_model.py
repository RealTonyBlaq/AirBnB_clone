#!/usr/bin/python3
""" Unittest for BaseModel in base_model.py """

import datetime
from models.base_model import BaseModel
import unittest
import uuid
from models.engine.file_storage import FileStorage


class TestBaseModel_instance_creation(unittest.TestCase):
    """ Testing the BaseModel instance creation """

    def test_type(self):
        """ Tests instance type """
        bm = BaseModel()
        self.assertEqual(BaseModel, type(bm))

    def test_two_instances(self):
        """ Tests two instances' ids, verifying inequality """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_instance_attr_exists(self):
        """ Verifies existence of all attributes """
        bm = BaseModel()
        self.assertIn(bm.id, bm.__dict__.values())
        self.assertIn(bm.created_at, bm.__dict__.values())
        self.assertIn(bm.updated_at, bm.__dict__.values())

    def test_instance_storage(self):
        """ Tests that instance was stored """
        bm = BaseModel()
        self.assertIn(bm, FileStorage.all(bm).values())

    def test_args(self):
        """ Tests when only *args is passed """
        bm = BaseModel("name")
        self.assertNotIn("name", bm.__dict__.values())

    def test_None(self):
        """ Tests when None is passed """
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_kwargs_(self):
        """
        Tests a dict as **kwargs with:
        id = (str)
        created_at = <class datetime>
        updated_at = <class datetime>
        """
        date = str(datetime.datetime.now())
        a_dict = {'id': "12345", 'created_at': date, 'updated_at': date}
        self.assertEqual("12345", BaseModel(**a_dict).id)

    def test_kwargs_None(self):
        """
        Tests a dict as **kwargs with:
        id = None
        created_at = None
        updated_at = None
        """
        a_dict = {'id': None, 'created_at': None, 'updated_at': None}
        with self.assertRaises(TypeError):
            BaseModel(**a_dict)

    def test_kwargs_dict(self):
        """ Tests BaseModel with kwargs as a list """
        my_list = ["age", "number", "time"]
        with self.assertRaises(TypeError):
            BaseModel(**my_list)

    def test_args_dict(self):
        """ Tests when a list is passed as *args """
        my_list = ["age", "name"]
        bm = BaseModel(*my_list)
        self.assertNotIn("age", bm.__dict__)
        self.assertNotIn("name", bm.__dict__)

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

    def test_updated_at_is_not_created_at(self):
        """ Checks if attributes updated_at and created_at are not equal """
        bm = BaseModel()
        self.assertNotEqual(bm.created_at, bm.updated_at)


class TestBaseModel_Save(unittest.TestCase):
    """ Testing the public method save() of BaseModel """

    def test_save(self):
        """ Checks if updated_at updates at save() call """
        bm = BaseModel()
        before_save = bm.updated_at
        bm.save()
        self.assertNotEqual(before_save, bm.updated_at)

    def test_updated_at_save(self):
        """ Tests if updated_at updates when save() is called """
        bm = BaseModel()
        before_save = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, before_save)

    def test_updated_at_ne_created_at(self):
        """
        Tests if created_at and updated_at are not equal after the
        public method save() is called.
        """
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)


class TestBaseModel_string_representation(unittest.TestCase):
    """ Tests the __str__() method of BaseModel """

    def test_str_type(self):
        """ Tests the string representation of BaseModel """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)


class TestBaseModel_to_dict(unittest.TestCase):
    """ Tests the to_dict() method of BaseModel """
    def test_to_dict_type(self):
        """ Checks type of the return value of to_dict() """
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
