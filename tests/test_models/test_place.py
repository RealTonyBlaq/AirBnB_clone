#!/use/bin/python3
"""to test the place module"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import datetime


class TestPlace(unittest.TestCase):
    def setUp(self):
        """set up a place instance for testing"""
        self.place = Place()

    def test_instance(self):
        """Test if the place is an instance of state"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """test if the place has the required attributes"""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_attribute_types(self):
        """test if the type of attributes are correct"""
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime.datetime)
        self.assertIsInstance(self.place.updated_at, datetime.datetime)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_to_dict_method(self):
        """test is to_dict method produces the correct output"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertTrue('__class__' in place_dict)
        self.assertTrue('id' in place_dict)
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)
        self.assertTrue('city_id' in place_dict)
        self.assertTrue('user_id' in place_dict)
        self.assertTrue('name' in place_dict)
        self.assertTrue('description' in place_dict)
        self.assertTrue('number_rooms' in place_dict)
        self.assertTrue('number_bathrooms' in place_dict)
        self.assertTrue('max_guest' in place_dict)
        self.assertTrue('price_by_night' in place_dict)
        self.assertTrue('latitude' in place_dict)
        self.assertTrue('longitude' in place_dict)
        self.assertTrue('amenity_ids' in place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_str_method(self):
        """test if the str method produces the corrected output"""
        expected_str = "[Place] ({}) {}".format(
                self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)


if __name__ == "__main__":
    unittest.main()
