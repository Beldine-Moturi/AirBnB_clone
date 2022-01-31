#!/usr/bin/python3
"""Contains test cases for the BaseModel class used
for all other classes in this project"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


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

        self.assertTrue(hasattr(self.model1, "id"))
        self.assertIs(type(self.model1.id), str)
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_created_at_attribute(self):
        """Tests that the current datetime is assigned when
        objects of this class are instantiated"""

        t = datetime.now()
        created = self.model1.created_at.isoformat(timespec='seconds')
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertIs(type(self.model1.created_at), datetime)
        self.assertGreaterEqual(t.isoformat(timespec='seconds'), created)

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.model1.updated_at
        self.model1.save()
        new = self.model1.updated_at
        self.assertNotEqual(old, new)

    def test_updated_at_attribute(self):
        """Tests that the current datetime is assigned when
        objects of this class are updated"""

        self.assertTrue(hasattr(self.model1, "updated_at"))
        self.assertIs(type(self.model1.updated_at), datetime)
        self.model1.save()
        t = datetime.now()
        update = self.model1.updated_at.isoformat(timespec='seconds')
        self.assertEqual(t.isoformat(timespec='seconds'), update)


if __name__ == "__main__":
    unittest.main()
