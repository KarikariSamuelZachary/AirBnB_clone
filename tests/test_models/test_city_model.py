#!/usr/bin/python3
"""
City Test module

This module contains test cases for the city model
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):
    """City model test class"""

    def setUp(self):
        """Set up tests dependencies"""
        self.c = City()
        self.c.name = ''
        self.c.state_id = ''

    def test_create_city(self):
        """Test creating a new city"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")
        self.assertIsInstance(self.c, City)
        self.assertTrue(issubclass(type(self.c), BaseModel))

    def test_new_instance_stored_in_objects(self):
        """Test new instance is stored in storage"""
        self.assertIn(self.c, storage.all().values())

    def test_attributes(self):
        """Test that the appropriate attributes are set"""

        self.assertTrue(hasattr(self.c, "id"))
        self.assertTrue(hasattr(self.c, "created_at"))
        self.assertTrue(hasattr(self.c, "updated_at"))
        self.assertTrue(hasattr(self.c, "state_id"))
        self.assertEqual(self.c.state_id, "")
        self.assertTrue(hasattr(self.c, "name"))
        self.assertEqual(self.c.name, "")
