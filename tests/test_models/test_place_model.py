#!/usr/bin/python3
"""Place Test module

This module contains test cases for the place model
"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """Place model test class"""

    def setUp(self):
        """Set up tests dependencies"""
        self.p = Place()

    def test_create_place(self):
        """Test creating a new place"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")
        self.assertIsInstance(self.p, Place)
        self.assertTrue(issubclass(type(self.p), BaseModel))

    def test_new_instance_stored_in_objects(self):
        """Test new instance is stored in storage"""
        self.assertIn(self.p, storage.all().values())

    def test_attributes(self):
        """Test that the appropriate attributes are set"""
        p = self.p
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))
        self.assertTrue(hasattr(p, 'city_id'))
        self.assertEqual(p.city_id, "")
        self.assertTrue(hasattr(p, "user_id"))
        self.assertEqual(p.user_id, "")
        self.assertTrue(hasattr(p, 'name'))
        self.assertEqual(p.name, "")
        self.assertTrue(hasattr(p, 'description'))
        self.assertEqual(p.description, "")
        self.assertTrue(hasattr(p, 'number_rooms'))
        self.assertEqual(p.number_rooms, 0)
        self.assertTrue(hasattr(p, 'number_bathrooms'))
        self.assertEqual(p.number_bathrooms, 0)
        self.assertTrue(hasattr(p, 'max_guest'))
        self.assertEqual(p.max_guest, 0)
        self.assertTrue(hasattr(p, 'price_by_night'))
        self.assertEqual(p.price_by_night, 0)
        self.assertTrue(hasattr(p, 'latitude'))
        self.assertEqual(p.latitude, 0.0)
        self.assertTrue(hasattr(p, 'longitude'))
        self.assertEqual(p.longitude, 0.0)
        self.assertTrue(hasattr(p, 'amenity_ids'))
        self.assertEqual(p.amenity_ids, [])
