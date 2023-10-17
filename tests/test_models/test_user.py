#!/usr/bin/python3
"""Unittest for user.py"""


import unittest
import uuid
from models.user import User
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """class for testing user class"""

    def setUp(self):
        """called before every test"""
        self.new_user = User()

    def tearDown(self):
        """called after every test"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test__init__id(self):
        """tests id method"""
        this_dict = self.new_user.__dict__
        self.assertIsNotNone(this_dict.get("id"))

    def test__init__created_at(self):
        this_dict = self.new_user.__dict__
        self.assertIsNotNone(this_dict.get("created_at"))

    def test_attributes(self):
        self.assertTrue(hasattr(self.new_user, "email"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "password"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "first_name"))
        self.assertEqual(self.new_user.email, "")
        self.assertTrue(hasattr(self.new_user, "last_name"))
        self.assertEqual(self.new_user.email, "")

        self.assertFalse(hasattr(self.new_user, "updated_at"))
        self.assertFalse(hasattr(self.new_user, "my_number"))
        self.assertFalse(hasattr(self.new_user, "random_attr"))
        self.new_user.name = "TeamTeam!"
        self.new_user.age = 100
        self.assertTrue(hasattr(self.new_user, "name"))
        self.assertEqual(self.new_user.name, "TeamTeam!")
        self.assertTrue(hasattr(self.new_user, "age"))
        delattr(self.new_user, "name")
        self.assertFalse(hasattr(self.new_user, "name"))
        self.assertEqual(self.new_user.__class__.__name__, "BaseModel")

    def test_save_init(self):
        this_dict = self.new_user.__dict__
        self.assertIsNone(this_dict.get("updated_at"))

    def test_save_update(self):
        this_dict = self.new_user.__dict__
        before = this_dict.get("updated_at")
        self.new_user.save()
        this_dict = self.new_user.__dict__
        after = this_dict.get("updated_at")
        self.assertNotEqual(before, after)

    def test___str__(self):
        """tests for string representation"""
        correct_format = ("[{}] ({}) {}".format
                          (self.new_user.__class__.__name__,
                           self.new_user.id,
                           self.new_user.__dict__))
        self.assertEqual(print(correct_format), print(self.new_user))

    def test_repr(self):
        str_return = self.new_user.__str__
        self.assertIsNotNone(str_return)

    def test_to_json(self):
        """tests for json"""
        json_return = BaseModel.to_json(self.new_user)
        self.assertEqual(type(json_return), dict)


if __name__ == '__main__':
    unittest.main()
