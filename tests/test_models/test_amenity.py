#!/use/bin/python3
"""to test the amenity module"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """set up a amenity instance for testing"""
        self.amenity = Amenity()

    def test_instance(self):
        """Test if the amenity is an instance of state"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """test if the amenity has the required attributes"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_types(self):
        """test if the type of attributes are correct"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict_method(self):
        """test is to_dict method produces the correct output"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertTrue('__class__' in amenity_dict)
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)
        self.assertTrue('name' in amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_str_method(self):
        """test if the str method produces the corrected output"""
        expected_str = "[Amenity] ({}) {}".format(
                self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == "__main__":
    unittest.main()
