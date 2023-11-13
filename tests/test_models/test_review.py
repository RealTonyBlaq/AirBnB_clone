#!/use/bin/python3
"""to test the review module"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import datetime


class TestReview(unittest.TestCase):
    def setUp(self):
        """set up a review instance for testing"""
        self.review = Review()

    def test_instance(self):
        """Test if the review is an instance of state"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """test if the review has the required attributes"""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """test if the type of attributes are correct"""
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_to_dict_method(self):
        """test is to_dict method produces the correct output"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertTrue('__class__' in review_dict)
        self.assertTrue('id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)
        self.assertTrue('place_id' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('text' in review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_str_method(self):
        """test if the str method produces the corrected output"""
        expected_str = "[Review] ({}) {}".format(
                self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)


if __name__ == "__main__":
    unittest.main()
