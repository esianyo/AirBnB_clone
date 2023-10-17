#!/usr/bin/python3
"""Unittest for base_model.py"""

import unittest
import uuid
import models
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """class for testing base model"""

    def setUp(self):
        """called before each test is run"""
        self.new_inst = BaseModel()

    def tearDown(self):
        """called after running each test"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test__init__id(self):
        """method for testing id method"""
        this_dict = self.new_inst.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        this_dict = self.new_inst.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        self.assertFalse(hasattr(self.new_inst, "updated_at"))
        self.assertFalse(hasattr(self.new_inst, "my_number"))
        self.assertFalse(hasattr(self.new_inst, "random_attr"))
        self.new_inst.name = "TeamTeam!"
        self.new_inst.age = 100
        self.assertTrue(hasattr(self.new_inst, "name"))
        self.assertEqual(self.new_inst.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_inst, "age"))
        delattr(self.new_inst, "name")
        self.assertFalse(hasattr(self.new_inst, "name"))
        self.assertEqual(self.new_inst.__class__.__name__, "BaseModel")

    def test_save_init(self):
        this_dict = self.new_inst.__dict__
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        this_dict = self.new_inst.__dict__
        before = this_dict.get("updated_at")
        self.new_inst.save()
        this_dict = self.new_inst.__dict__
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test___str__(self):
        correct_format = ("[{}] ({}) {}".format
                          (self.new_inst.__class__.__name__,
                           self.new_inst.id,
                           self.new_inst.__dict__))
        self.assertEqual(print(correct_format), print(self.new_inst))

    def test_repr(self):
        str_return = self.new_inst.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        json_return = BaseModel.to_json(self.new_inst)
        self.assertEqual(type(json_return), dict)


if __name__ == '__main__':
    unittest.main()
