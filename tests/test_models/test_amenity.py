#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.amenity import Amenity
import unittest


class TestAmenityClassAttributes(unittest.TestCase):
    """Tests instantiation of Amenity objects and all the attributes
    defined in the class"""

    def test_amenity_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class Amenity"""

        amenity1 = Amenity()
        amenity1.name = "WiFi"

        self.assertTrue(hasattr(amenity1, "name"))


class TestAmenityClassStorage(unittest.TestCase):
    """Tests that objects of class Amenity are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with City objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_amenity1 = Amenity()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Amenity)

        new_amenity1.save()
        new_amenity2 = Amenity()
        new_amenity2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Amenity)


if __name__ == "__main__":
    unittest.main()
