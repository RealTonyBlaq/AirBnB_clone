#!/usr/bin/python3
""" Unittest for BaseModel in base_model.py """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime
import json
import os
import unittest
import uuid


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

    def test_attr_created_exists(self):
        """ Checks if a created attribute exists """
        bm = BaseModel()
        bm.time = "2:30pm"
        self.assertEqual("2:30pm", bm.time)

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

    def test_kwargs_list(self):
        """ Tests BaseModel with kwargs as a list """
        my_list = ["age", "number", "time"]
        with self.assertRaises(TypeError):
            BaseModel(**my_list)

    def test_args_list(self):
        """ Tests when a list is passed as *args """
        my_list = ["age", "name"]
        bm = BaseModel(*my_list)
        self.assertNotIn("age", bm.__dict__.values())
        self.assertNotIn("name", bm.__dict__.values())

    def test_args_and_kwargs(self):
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
        self.assertIn(bm.id, bm.__dict__.values())

    def test_kwargs_not_empty(self):
        """
        Tests BaseModel when **kwargs is the dict rep of another
        BaseModel class
        """
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

    def test_created_at_type(self):
        """ Confirms if created_at is a type() of datetime """
        bm = BaseModel()
        self.assertEqual(type(bm.created_at), datetime.datetime)

    def test_updated_at_type(self):
        """ Confirms if updated_at is a type() of datetime """
        bm = BaseModel()
        self.assertEqual(type(bm.updated_at), datetime.datetime)

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

    def test_save_before_call(self):
        """ Tests if the file was created with instantiation """
        if os.path.exists("file.json"):
            os.remove("file.json")
        bm = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_save_file(self):
        """ checks if the file is created at save() call """
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_with_arg(self):
        """ Tests save with a positional argument """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(["list", "test", 20])

    def test_save_with_another_instance(self):
        """ Tests save() with another instance """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            BaseModel().save(bm)

    def test_save_file_content_type(self):
        """ Tests if file contents is a dict after deserialization """
        BaseModel().save()
        with open("file.json", encoding='utf-8') as file:
            data = json.loads(file.read())
        self.assertEqual(type(data), dict)

    def test_save_updates_file(self):
        """ Tests if a string exists in the file """
        bm = BaseModel()
        bm.save()
        bmid = "{}.{}".format(bm.__class__.__name__, bm.id)
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_string_representation(unittest.TestCase):
    """ Tests the __str__() method of BaseModel """

    def test_str_type(self):
        """ Tests the string representation of BaseModel """
        bm = BaseModel()
        self.assertEqual(type(bm.__str__()), str)

    def test_str_result(self):
        """ Tests the __str__() result """
        bm = BaseModel()
        self.assertEqual(bm.__str__(), "[{}] ({}) {}"
                         .format(bm.__class__.__name__, bm.id, bm.__dict__))


class TestBaseModel_to_dict(unittest.TestCase):
    """ Tests the to_dict() method of BaseModel """

    def test_to_dict_type(self):
        """ Checks type of the return value of to_dict() """
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_to_dict_return_values(self):
        """ Checks if attrs created are returned by to_dict() """
        bm = BaseModel()
        self.assertIn("id", bm.to_dict().keys())
        self.assertIn("created_at", bm.to_dict().keys())
        self.assertIn("__class__", bm.to_dict().keys())
        self.assertIn("updated_at", bm.to_dict().keys())

    def test_to_dict_return_value(self):
        """ Checks if new attrs created are returned by to_dict() """
        bm = BaseModel()
        bm.test = "Passed"
        self.assertIn("test", bm.to_dict().keys())

    def test_to_dict_arg(self):
        """ Tests to_dict() with an argument """
        a_dict = {"id": "12345", "name": "Ifeanyi"}
        with self.assertRaises(TypeError):
            BaseModel().to_dict(a_dict)

    def test_to_dict_attr_types(self):
        """ Tests the attribute types """
        bm_dict = BaseModel().to_dict()
        self.assertEqual(type(bm_dict["id"]), str)
        self.assertEqual(type(bm_dict["__class__"]), str)
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)

    def test_to_dict_and_dict(self):
        """ Confirms that self.__dict__ and to_dict() are not equal """
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)


if __name__ == "__main__":
    unittest.main()
