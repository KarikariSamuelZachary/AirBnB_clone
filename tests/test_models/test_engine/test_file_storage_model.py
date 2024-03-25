#!/usr/bin/python3
"""
This module contains the test cases for the storage system model
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Create a FileStorage instance"""
        self.storage = FileStorage()

    def tearDown(self):
        """Remove the test file if it exists after each test"""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all_empty(self):
        """Test if all() returns an empty dictionary initially"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test adding a new object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"{type(obj).__name__}.{obj.id}", self.storage.all())

    def test_save_reload(self):
        """Test saving and reloading objects from file"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"{type(obj1).__name__}.{obj1.id}", self.storage.all())
        self.assertIn(f"{type(obj2).__name__}.{obj2.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
