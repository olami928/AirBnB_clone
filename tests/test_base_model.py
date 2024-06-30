#!/usr/bin/python3
"""This is the test class for basemodel."""


import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        del self.model

    def test_id(self):
        """Test id is assigned and is unique"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertIsInstance(self.model.id, str)
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """Test created_at is assigned and is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at is assigned and is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str(self):
        """Test __str__ method"""
        expected_output = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        """Test save method updates updated_at"""
        old_updated_at = self.model.updated_at
        sleep(0.1)  # Sleep to ensure time has passed
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method creates accurate dictionary"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_contains_added_attributes(self):
        """Test to_dict method contains attributes added after instantiation"""
        self.model.name = "Test Model"
        self.model.my_number = 89
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['my_number'], 89)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(new_model.to_dict(), model_dict)

    def test_kwargs_instantiation_missing_updated_at(self):
        """Test instantiation with kwargs missing updated_at"""
        model_dict = self.model.to_dict()
        del model_dict['updated_at']
        new_model = BaseModel(**model_dict)
        self.assertNotEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.id, new_model.id)

    def test_kwargs_instantiation_missing_created_at(self):
        """Test instantiation with kwargs missing created_at"""
        model_dict = self.model.to_dict()
        del model_dict['created_at']
        with self.assertRaises(KeyError):
            BaseModel(**model_dict)

    def test_save_with_kwargs(self):
        """Test save method with kwargs updates updated_at"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        old_updated_at = new_model.updated_at
        sleep(0.1)
        new_model.save()
        self.assertNotEqual(new_model.updated_at, old_updated_at)
        self.assertGreater(new_model.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
