#!/usr/bin/python3
"""Contains tests for the Class User"""
import json
from models import storage
import os
from models.user import User
import unittest


class TestUserClassAttributes(unittest.TestCase):
    """Tests instantiation of User objects and all the attributes
    defined in the class"""

    def test_user_attributes(self):
        """tests the instantiations and dynamic allocation of attributes
        to objects of the class User"""

        user1 = User()
        user1.first_name = "Bella"
        user1.last_name = "Moturi"
        user1.email = "beldinemoturi@gmail.com"
        user1.password = "password1"

        for att in ['first_name', 'last_name', 'email', 'password']:
            self.assertTrue(hasattr(user1, att))
        self.assertEqual(user1.first_name, "Bella")
        self.assertEqual(user1.last_name, "Moturi")
        self.assertEqual(user1.email, "beldinemoturi@gmail.com")
        self.assertEqual(user1.password, "password1")


class TestUserClassStorage(unittest.TestCase):
    """Tests that objects of class User are properly stored in the file
    storage"""

    @classmethod
    def tearDownClass(cls):
        """Tears down resources created when running the tests"""

        os.remove("filestorage.json")

    def test_file_storage(self):
        """Tests the file storage with User objects"""

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        new_user1 = User()
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 2)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == User)

        new_user1.save()
        new_user2 = User()
        new_user2.save()
        self.assertTrue(os.path.isfile("filestorage.json"))
        storage.reload()
        all_objs = storage.all()
        self.assertTrue(len(all_objs) == 3)
        for key, value in all_objs.items():
            self.assertTrue(type(value) == User)


if __name__ == "__main__":
    unittest.main()
