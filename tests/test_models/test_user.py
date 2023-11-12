#!/usr/bin/python3
"""script to test user class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """class TestUser"""
    def test_inheritance(self):
        """method to test inheritance"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """method to test attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attributes_type(self):
        """method to test attributes type"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_default_attribute_values(self):
        """method to test default attribute values"""
        user = User()
        self.assertEqual(user.email, " ")
        self.assertEqual(user.password, " ")
        self.assertEqual(user.first_name, " ")
        self.assertEqual(user.last_name, " ")

    def test_setting_attribute_values(self):
        """method to check the setting of attribute values"""
        user = User()
        user.email = "test@mail.com"
        user.password = "save_password"
        user.first_name = "Steve"
        user.last_name = "Adah"

        self.assertEqual(user.email, "test@mail.com")
        self.assertEqual(user.password, "save_password")
        self.assertEqual(user.first_name, "Steve")
        self.assertEqual(user.last_name, "Adah")

    def test_to_dict_method(self):
        """test method to_dict"""
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertTrue(isinstance(user_dict['email'], str))
        self.assertTrue(isinstance(user_dict['password'], str))
        self.assertTrue(isinstance(user_dict['first_name'], str))
        self.assertTrue(isinstance(user_dict['last_name'], str))
        self.assertFalse(isinstance(user_dict['__class__'], type(User)))
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_str_method(self):
        """test string method"""
        user = User()
        user_str = str(user)
        self.assertIsInstance(user_str, str)


if __name__ == "__main__":
    unittest.main()
