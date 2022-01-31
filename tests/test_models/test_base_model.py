#!/usr/bin/python3
"""Contains test cases for the BaseModel class used
for all other classes in this project"""
import unittest
from models.base_model import BaseModel

class TestBaseModelClass(unittest.TestCase):
    """Tests the Instance attributes and methods
    used in this class"""

    def setUp(self):
        """sets up the resources required to run the tests"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """deletes the resources used after tests are run"""

        del self.model1
        del self.model2

    def test_id_attribute(self):
        """Tests that objects of this class are properly instantiated
        with a universally unique identifier"""

        #test that the objects are assigned an id attribute during instantiation
        self.assertTrue(hasattr(self.model1, "id"))

        #tests that the id attribute is a string
        self.assertIs(type(self.model1.id), str)

        #tests that the id attribute is a universally unique identifier
        self.assertNotEqual(self.model1.id, self.model2.id)

if __name__ == "__main__":
    unittest.main()
