#!/usr/bin/python3
""" Test suite for Class FileStorage """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os
import unittest


class TestFileStorage_attrs(unittest.TestCase):
    """ Testing the private class attributes """

    def test_objects(self):
        """ Tests __objects of FileStorage """
        fs = FileStorage()
        obj = getattr(fs, '_FileStorage__objects')
        self.assertEqual(type(obj), dict)
        self.assertNotEqual(obj, None)

    def test_file_path(self):
        """ Tests __file_path of FileStorage """
        fs = FileStorage()
        file = getattr(fs, '_FileStorage__file_path')
        self.assertNotEqual(file, None)
        self.assertEqual(type(file), str)
        fs.save()
        self.assertTrue(os.path.exists(file))


class TestFileStorage_all(unittest.TestCase):
    """ Testing FileStorage.all() """

    def test_all_return_type(self):
        """ Tests the return type of all() """
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_all_arg(self):
        """ Tests all() with an argument """
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_all_values(self):
        """ Tests if the dict repr of BaseModel() is stored in all() """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        self.assertNotIn(bm.to_dict(), fs.all().values())


class TestFileStorage_new(unittest.TestCase):
    """ Testing FileStorage.new """

    def test_new_None(self):
        """ Tests if new() works when None is passed as arg """
        with self.assertRaises(AttributeError):
            FileStorage().new(None)

    def test_new_string(self):
        """ Tests new() with a string as arg """
        with self.assertRaises(AttributeError):
            FileStorage().new("test")

    def test_new_list(self):
        """ Tests new() with a list as arg """
        with self.assertRaises(AttributeError):
            FileStorage().new(["test", "fail", "id"])

    def test_new_dict(self):
        """ Tests new() with a dict as arg """
        with self.assertRaises(AttributeError):
            FileStorage().new({"test": 20, "id": "12345"})

    def test_new_two_args(self):
        """ Tests with an two instances as arg """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            FileStorage().new(bm, None)

    def test_new_arg(self):
        """ Tests new() with one arg """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, fs.all().keys())

    def test_new_values(self):
        """ Tests if the instance passed to new() is stored in all() """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        self.assertIn(bm, fs.all().values())

    def test_new_dict_length(self):
        """
        Tests if new() adds keys to __objects of FileStorage
        by testing the length of all()
        """
        fs = FileStorage()
        bm = BaseModel()
        bm2 = BaseModel()
        fs.new(bm)
        self.assertGreater(len(fs.all()), 0)
        fs.new(bm2)
        self.assertGreater(len(fs.all()), 1)

    def test_new_dict_values(self):
        """ Tests the dict detail created by new() and BaseModel.to_dict() """
        fs = FileStorage()
        bm = BaseModel()
        bm_dict = bm.to_dict()
        fs.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm_dict["id"])
        new = {key: bm_dict}
        self.assertNotEqual(fs.all(), new)


class TestFileStorage_save(unittest.TestCase):
    """ Testing FileStorage.save() """

    def test_save_None(self):
        """ Tests save() with None as arg """
        with self.assertRaises(TypeError):
            FileStorage().save(None)

    def test_save_arg(self):
        """ Tests save() with a BaseModel instance as arg """
        with self.assertRaises(TypeError):
            FileStorage().save(BaseModel())

    def test_save_file_exists(self):
        """ Tests if save() created file.json """
        fs = FileStorage()
        fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_deserialization(self):
        """ Tests if the deserialized text is a dict """
        FileStorage().save()
        with open("file.json") as f:
            data = json.loads(f.read())
        self.assertEqual(type(data), dict)

    def test_save_deserialization_dict_value(self):
        """ Tests if the deserialized dict contains to_dict() value"""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        with open("file.json") as f:
            data = json.loads(f.read())
        self.assertIn(bm.to_dict(), data.values())

    def test_save_deserialization_dict_key(self):
        """ Tests if the deserialized dict contains a key """
        fs = FileStorage()
        bm = BaseModel()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        fs.new(bm)
        fs.save()
        with open("file.json") as f:
            data = json.loads(f.read())
        self.assertIn(key, data.keys())
        self.assertFalse(bm in data)


class TestFileStorage_reload(unittest.TestCase):
    """ Testing FileStorage().reload() """

    def test_reload_None(self):
        """ Tests reload() with None as arg """
        with self.assertRaises(TypeError):
            FileStorage().reload(None)

    def test_reload_arg(self):
        """ Tests reload() with BaseModel instance as arg """
        with self.assertRaises(TypeError):
            FileStorage().reload(BaseModel())

    def test_reload_file_doesnt_exist(self):
        """ Tests when file doesn't exist """
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage().reload()
        self.assertFalse(os.path.exists("file.json"))

    def test_reload(self):
        """ Tests if reload() recreates instances """
        if os.path.exists("file.json"):
            os.remove("file.json")
        fs = FileStorage()
        a_dict = fs.all().copy()
        fs.save()
        fs.reload()
        new_dict = fs.all().copy()
        self.assertEqual(type(new_dict), dict)
        self.assertCountEqual(a_dict, new_dict)

    def test_reload_override(self):
        """ Tests for method override """
        if os.path.exists("file.json"):
            os.remove("file.json")
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        fs.reload()
        self.assertFalse("__class__" in fs.all().values())

    def test_reload_instances(self):
        """ Tests for instance reload """
        if os.path.exists("file.json"):
            os.remove("file.json")
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        del bm
        del fs
        ff = FileStorage()
        ff.reload()
        self.assertNotEqual(ff.all(), {})

if __name__ == "__main__":
    unittest.main()
