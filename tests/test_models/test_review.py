#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.review import Review
import unittest


class TestReviewClassAttributes(unittest.TestCase):
    """Tests instantiation of Review objects and all the attributes
    defined in the class"""

    def test_review_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class Review"""

        review1 = Review()
        review1.text = "good"

        self.assertTrue(hasattr(review1, "text"))
        self.assertEqual(review1.text, "good")


class TestReviewClassStorage(unittest.TestCase):
    """Tests that objects of class Review are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with User objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_review1 = Review()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Review)

        new_review1.save()
        new_review2 = Review()
        new_review2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Review)


if __name__ == "__main__":
    unittest.main()
