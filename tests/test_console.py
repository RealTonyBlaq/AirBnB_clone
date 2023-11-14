#!/usr/bin/python3
"""script to test the console."""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage

class TestHBNBCommand(unittest.TestCase):
    """test HBNBCommand"""
    def setUp(self):
        """set up before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """clean up after ach test"""
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test count command"""
        with patch.object(storage, 'all', return_value={'User.1': 1, 'User.2': 2}):
            self.console.onecmd("count User")
            self.assertEqual(mock_stdout.getvalue().strip(), "2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """test quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        with patch.object(storage, 'all', return_value={'User.1': 1, 'User.2': 2}):
            self.console.onecmd("show User 1")
            self.assertEqual(mock_stdout.getvalue().strip(), "1")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """test destroy command"""
        with patch.object(storage, 'all', return_value={'User.1': 1, 'User.2': 2}):
            self.console.onecmd("destroy User 1")
            self.assertNotIn('User.1', storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command,"""
        with patch.object(storage, 'all', return_value={'User.1': 1, 'User.2': 2}):
            self.console.onecmd("all User")
            self.assertIn("1", mock_stdout.getvalue().strip())
            self.assertIn("2", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        with patch.object(storage, 'save'):
            self.console.onecmd("create User")
            self.assertIsNotNone(mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test update command."""
        with patch.object(storage, 'all', return_value={'User.1': 1}):
            self.console.onecmd("update User 1 name 'John'")
            self.assertIn("ok", mock_stdout.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
