#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.city import City
import unittest


class TestCityClassAttributes(unittest.TestCase):
    """Tests instantiation of City objects and all the attributes
    defined in the class"""

    def test_city_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class City"""

        city1 = City()
        city1.name = "Nakuru"

        self.assertTrue(hasattr(city1, "name"))


class TestCityClassStorage(unittest.TestCase):
    """Tests that objects of class City are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with City objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_city1 = City()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == City)

        new_city1.save()
        new_city2 = City()
        new_city2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == City)
