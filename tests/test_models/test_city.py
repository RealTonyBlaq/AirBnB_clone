#!/use/bin/python3
"""to test the city module"""
import unittest
from models.city import City
from models.base_model import BaseModel
import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        """set up a city instance for testing"""
        self.city = City()

    def test_instance(self):
        """Test if the city is an instance of state"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """test if the city has the required attributes"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attribute_types(self):
        """test if the type of attributes are correct"""
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_to_dict_method(self):
        """test is to_dict method produces the correct output"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertTrue('__class__' in city_dict)
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)
        self.assertTrue('state_id' in city_dict)
        self.assertTrue('name' in city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_str_method(self):
        """test if the str method produces the corrected output"""
        expected_str = "[City] ({}) {}".format(
                self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == "__main__":
    unittest.main()
