#!/usr/bin/python3
"""test_base_model module
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """class testing base_model module
    """
     def test_init(self):
        """
        unittest for init method
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        Unittest for save method
        """
        my_model = BaseModel()

        prev_updated_at = my_model.updated_at

        curr_updated_at = my_model.save()

        self.assertNotEqual(prev_updated_at, curr_updated_at)

    def test_to_dict(self):
        """
        Unittest for to_dict method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())

     def test_str(self):
        """
        Unittest for string method
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
