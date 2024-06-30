#!/usr/bin/python3
"""This is the test class for filestorage."""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test methods"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()
        self.storage.new(self.model)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)
        self.storage.save()

    def tearDown(self):
        """Tear down test methods"""
        del self.model
        del self.user
        del self.state
        del self.city
        del self.amenity
        del self.place
        del self.review
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the correct dictionary of objects"""
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.model.id), all_objs)
        self.assertIn("User.{}".format(self.user.id), all_objs)
        self.assertIn("State.{}".format(self.state.id), all_objs)
        self.assertIn("City.{}".format(self.city.id), all_objs)
        self.assertIn("Amenity.{}".format(self.amenity.id), all_objs)
        self.assertIn("Place.{}".format(self.place.id), all_objs)
        self.assertIn("Review.{}".format(self.review.id), all_objs)

    def test_new(self):
        """Test that new adds an object to __objects"""
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), all_objs)

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            json_data = json.load(f)
        key = "BaseModel.{}".format(self.model.id)
        self.assertIn(key, json_data)
        self.assertEqual(json_data[key]['__class__'], 'BaseModel')

    def test_reload(self):
        """Test that reload properly loads objects from file.json"""
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.model.id), all_objs)
        self.assertIn("User.{}".format(self.user.id), all_objs)
        self.assertIn("State.{}".format(self.state.id), all_objs)
        self.assertIn("City.{}".format(self.city.id), all_objs)
        self.assertIn("Amenity.{}".format(self.amenity.id), all_objs)
        self.assertIn("Place.{}".format(self.place.id), all_objs)
        self.assertIn("Review.{}".format(self.review.id), all_objs)

    def test_get(self):
        """Test that get retrieves the correct object by class name and id"""
        obj = self.storage.get('BaseModel', self.model.id)
        self.assertEqual(obj, self.model)

    def test_count(self):
        """Test that count returns the correct number of objects"""
        count = self.storage.count()
        self.assertEqual(count, 7)
        count = self.storage.count('BaseModel')
        self.assertEqual(count, 1)

if __name__ == '__main__':
    unittest.main()
