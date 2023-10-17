#!/usr/bin/python3
"""Unittest for amenity.py"""

import unittest
import uuid
import models
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
    """class for testing amenity class"""

    def setUp(self):
        """called before every test"""
        self.new_inst = Amenity()

    def tearDown(self):
        """called after every test"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test__init__id(self):
        """tests id method"""
        this_dict = self.new_amenity.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        this_dict = self.new_amenity.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "")

        self.assertFalse(hasattr(self.new_amenity, "updated_at"))
        self.assertFalse(hasattr(self.new_amenity, "my_number"))
        self.assertFalse(hasattr(self.new_amenity, "random_attr"))
        self.new_amenity.name = "TeamTeam!"
        self.new_amenity.age = 100
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_amenity, "age"))
        delattr(self.new_amenity, "name")
        self.assertFalse(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.__class__.__name__, "BaseModel")

    def test_save_init(self):
        """tests save method"""
        this_dict = self.new_amenity.__dict__
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        """tests save update method"""
        this_dict = self.new_amenity.__dict__
        before = this_dict.get("updated_at")
        self.new_amenity.save()
        this_dict = self.new_amenity.__dict__
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test___str__(self):
        correct_format = ("[{}] ({}) {}".format
                          (self.new_amenity.__class__.__name__,
                           self.new_amenity.id,
                           self.new_amenity.__dict__))
        self.assertEqual(print(correct_format), print(self.new_amenity))

    def test_repr(self):
        str_return = self.new_amenity.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        """tests json"""
        json_return = BaseModel.to_json(self.new_amenity)
        self.assertEqual(type(json_return), dict)


if __name__ == '__main__':
    unittest.main()
