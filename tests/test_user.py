#!/usr/bin/python3
"""This is the test class for user."""


import unittest
from datetime import datetime
from models.user import User
import uuid


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up test methods"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "johndoe@example.com"
        self.user.password = "password"

    def tearDown(self):
        """Tear down test methods"""
        del self.user

    def test_user_instance(self):
        """Test if user is an instance of User"""
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        """Test if user attributes are correctly assigned"""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "johndoe@example.com")
        self.assertEqual(self.user.password, "password")

    def test_user_id(self):
        """Test if id is a valid UUID"""
        user_id = self.user.id
        self.assertIsInstance(user_id, str)
        try:
            uuid_obj = uuid.UUID(user_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_user_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_user_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_str(self):
        """Test the __str__ method of User"""
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.to_dict())
        self.assertEqual(str(self.user), expected_str)

    def test_user_save(self):
        """Test the save method of User"""
        old_updated_at = self.user.updated_at
        self.user.save()
        new_updated_at = self.user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_user_to_dict(self):
        """Test the to_dict method of User"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')
        self.assertEqual(user_dict['email'], 'johndoe@example.com')
        self.assertEqual(user_dict['password'], 'password')

if __name__ == '__main__':
    unittest.main()
