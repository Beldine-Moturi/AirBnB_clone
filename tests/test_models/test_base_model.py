#!/usr/bin/python3
"""Unittest of 'base_model'"""

import unittest
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """Test Base Class"""

    @classmethod
    def setUpClass(cls) -> None:
        """ Setup class method """
        cls.model1 = BaseModel()
        cls.model2 = BaseModel()

        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        """Clear objects after tests"""
        del cls.model1
        del cls.model2

        return super().tearDownClass()

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
        self.assertIsNotNone(self.id)
        # self.assertIsNotNone(model1.created_at)
        # self.assertIsNotNone(self.updated_at)


if __name__ == '__main__':
    unittest.main()
