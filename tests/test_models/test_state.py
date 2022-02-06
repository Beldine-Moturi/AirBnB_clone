#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.state import State
import unittest


class TestStateClassAttributes(unittest.TestCase):
    """Tests instantiation of State objects and all the attributes
    defined in the class"""

    def test_state_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class State"""

        state1 = State()
        state1.name = "Nairobi"

        self.assertTrue(hasattr(state1, "name"))
        self.assertEqual(state1.name, "Nairobi")


class TestStateClassStorage(unittest.TestCase):
    """Tests that objects of class State are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with User objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_state1 = State()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == State)

        new_state1.save()
        new_state2 = State()
        new_state2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == State)


if __name__ == "__main__":
    unittest.main()
