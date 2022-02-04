#!/usr/bin/python3
"""Unittest of 'base_model'"""

import unittest
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """Test Base Class"""

    def setUp(self):
        """Sets up sample objects for test running"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.model3 = BaseModel()

    def tearDown(self):
        """Destroys the objects setup for test running after\
            they have been used"""

        del self.model1
        del self.model2
        del self.model3

    def test_base_model_cls_doc(self):
        """Check if docstring for class is present"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_base_model_methods(self):
        """Check if method exists in BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_base_model_methods_doc(self):
        """Check that docstring exist for all methods"""
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)

    def test_base_model_attributes(self):
        """Test that these attributes exists in the BaseModel class
        """

        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "updated_at"))


if __name__ == '__main__':
    unittest.main()
