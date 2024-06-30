#!/usr/bin/python3
"""This is the test class for amenity."""


import unittest
from datetime import datetime
from models.amenity import Amenity
import uuid


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up test methods"""
        self.amenity = Amenity()
        self.amenity.name = "Wi-Fi"

    def tearDown(self):
        """Tear down test methods"""
        del self.amenity

    def test_amenity_instance(self):
        """Test if amenity is an instance of Amenity"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_attributes(self):
        """Test if amenity attributes are correctly assigned"""
        self.assertEqual(self.amenity.name, "Wi-Fi")

    def test_amenity_id(self):
        """Test if id is a valid UUID"""
        amenity_id = self.amenity.id
        self.assertIsInstance(amenity_id, str)
        try:
            uuid_obj = uuid.UUID(amenity_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_amenity_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_amenity_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_str(self):
        """Test the __str__ method of Amenity"""
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.to_dict())
        self.assertEqual(str(self.amenity), expected_str)

    def test_amenity_save(self):
        """Test the save method of Amenity"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        new_updated_at = self.amenity.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_amenity_to_dict(self):
        """Test the to_dict method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Wi-Fi')

if __name__ == '__main__':
    unittest.main()
