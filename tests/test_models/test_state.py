#!/use/bin/python3
"""to test the state module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        """set up a state instance for testing"""
        self.state = State()

    def test_instance(self):
        """Test if the state is an instance of state"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """test if the state has the required attributes"""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_types(self):
        """test if the type of attributes are correct"""
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        self.assertIsInstance(self.state.name, str)

    def test_to_dict_method(self):
        """test is to_dict method produces the correct output"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertTrue('__class__' in state_dict)
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('name' in state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

    def test_str_method(self):
        """test if the str method produces the corrected output"""
        expected_str = "[State] ({}) {}".format(
                self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)


if __name__ == "__main__":
    unittest.main()
