#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.place import Place
import unittest


class TestPlaceClassAttributes(unittest.TestCase):
    """Tests instantiation of Place objects and all the attributes
    defined in the class"""

    def test_place_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class Place"""

        place1 = Place()
        place1.name = "Kasarani"
        place1.description = "far"
        place1.number_rooms = 5
        place1.max_guest = 5

        for att in ['name', 'description', 'number_rooms', 'max_guest']:
            self.assertTrue(hasattr(place1, att))
        self.assertEqual(place1.name, "Kasarani")
        self.assertEqual(place1.description, "far")
        self.assertEqual(place1.number_rooms, 5)
        self.assertEqual(place1.max_guest, 5)


class TestPlaceClassStorage(unittest.TestCase):
    """Tests that objects of class Place are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with User objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_place1 = Place()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Place)

        new_place1.save()
        new_place2 = Place()
        new_place2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == Place)
