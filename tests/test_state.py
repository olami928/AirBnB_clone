#!/usr/bin/python3
"""This is the test class for state."""


import unittest
from datetime import datetime
from models.state import State
import uuid


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up test methods"""
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        """Tear down test methods"""
        del self.state

    def test_state_instance(self):
        """Test if state is an instance of State"""
        self.assertIsInstance(self.state, State)

    def test_state_attributes(self):
        """Test if state attributes are correctly assigned"""
        self.assertEqual(self.state.name, "California")

    def test_state_id(self):
        """Test if id is a valid UUID"""
        state_id = self.state.id
        self.assertIsInstance(state_id, str)
        try:
            uuid_obj = uuid.UUID(state_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_state_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_state_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_str(self):
        """Test the __str__ method of State"""
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.to_dict())
        self.assertEqual(str(self.state), expected_str)

    def test_state_save(self):
        """Test the save method of State"""
        old_updated_at = self.state.updated_at
        self.state.save()
        new_updated_at = self.state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_state_to_dict(self):
        """Test the to_dict method of State"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'California')

if __name__ == '__main__':
    unittest.main()
