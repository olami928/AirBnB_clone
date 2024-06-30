#!/usr/bin/python3
"""This is the test class for review."""


import unittest
from datetime import datetime
from models.review import Review
import uuid


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up test methods"""
        self.review = Review()
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "This is a great place!"

    def tearDown(self):
        """Tear down test methods"""
        del self.review

    def test_review_instance(self):
        """Test if review is an instance of Review"""
        self.assertIsInstance(self.review, Review)

    def test_review_attributes(self):
        """Test if review attributes are correctly assigned"""
        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "This is a great place!")

    def test_review_id(self):
        """Test if id is a valid UUID"""
        review_id = self.review.id
        self.assertIsInstance(review_id, str)
        try:
            uuid_obj = uuid.UUID(review_id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_review_created_at(self):
        """Test if created_at is a datetime object"""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_review_updated_at(self):
        """Test if updated_at is a datetime object"""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_str(self):
        """Test the __str__ method of Review"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.to_dict())
        self.assertEqual(str(self.review), expected_str)

    def test_review_save(self):
        """Test the save method of Review"""
        old_updated_at = self.review.updated_at
        self.review.save()
        new_updated_at = self.review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertLess(old_updated_at, new_updated_at)

    def test_review_to_dict(self):
        """Test the to_dict method of Review"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], '1234')
        self.assertEqual(review_dict['user_id'], '5678')
        self.assertEqual(review_dict['text'], 'This is a great place!')


if __name__ == '__main__':
    unittest.main()
