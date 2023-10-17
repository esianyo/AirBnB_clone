#!/usr/bin/python3
"""Unittest module"""


import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class Test__init__(unittest.TestCase):
    'Class for testing __init__ in models'

    def tearDown(self):
        """method called after each test"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass

    def test___init__(self):
        """loads test until all tests are completed"""
        before_dict = storage.all()
        self.assertEqual(before_dict, {})
        self.new_inst = BaseModel()
        after_dict = storage.all()
        self.assertIsNotNone(after_dict)
        self.assertTrue(isinstance(after_dict, dict))