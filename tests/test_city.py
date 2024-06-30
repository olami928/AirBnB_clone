#!/usr/bin/python3
"""This is the test class for city."""


import unittest
from datetime import datetime
from models.city import City
import uuid


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up test methods"""
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "state_1234"

    def tearDown(self):
        """Tear down test methods"""
        del self.city

    def test_city_instance(self):
        """Test if city is an instance of City"""
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """Test if city attributes are correctly assigned"""
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "state_1234")

    def test_city_id(self):
        """Test if id is a valid UUID"""
        city_id = self.city.id
        self.assertIsInstance(city_id, str)
        try:
            uuid_obj = uuid.UUID(city_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_city_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_str(self):
        """Test the __str__ method of City"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.to_dict())
        self.assertEqual(str(self.city), expected_str)

    def test_city_save(self):
        """Test the save method of City"""
        old_updated_at = self.city.updated_at
        self.city.save()
        new_updated_at = self.city.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_city_to_dict(self):
        """Test the to_dict method of City"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertEqual(city_dict['state_id'], 'state_1234')

if __name__ == '__main__':
    unittest.main()
