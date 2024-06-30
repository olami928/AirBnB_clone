#!/usr/bin/python3
"""This is the test class for place."""


import unittest
from datetime import datetime
from models.place import Place
import uuid


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up test methods"""
        self.place = Place()
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "My Place"
        self.place.description = "A nice place to stay"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["1", "2", "3"]

    def tearDown(self):
        """Tear down test methods"""
        del self.place

    def test_place_instance(self):
        """Test if place is an instance of Place"""
        self.assertIsInstance(self.place, Place)

    def test_place_attributes(self):
        """Test if place attributes are correctly assigned"""
        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "My Place")
        self.assertEqual(self.place.description, "A nice place to stay")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["1", "2", "3"])

    def test_place_id(self):
        """Test if id is a valid UUID"""
        place_id = self.place.id
        self.assertIsInstance(place_id, str)
        try:
            uuid_obj = uuid.UUID(place_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_place_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_place_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_str(self):
        """Test the __str__ method of Place"""
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.to_dict())
        self.assertEqual(str(self.place), expected_str)

    def test_place_save(self):
        """Test the save method of Place"""
        old_updated_at = self.place.updated_at
        self.place.save()
        new_updated_at = self.place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_place_to_dict(self):
        """Test the to_dict method of Place"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], '1234')
        self.assertEqual(place_dict['user_id'], '5678')
        self.assertEqual(place_dict['name'], 'My Place')
        self.assertEqual(place_dict['description'], 'A nice place to stay')
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertEqual(place_dict['number_bathrooms'], 2)
        self.assertEqual(place_dict['max_guest'], 5)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 37.7749)
        self.assertEqual(place_dict['longitude'], -122.4194)
        self.assertEqual(place_dict['amenity_ids'], ["1", "2", "3"])


if __name__ == '__main__':
    unittest.main()
