#!/usr/bin/python3
"""
Amenity Test module

This module contains test cases for the amenity model
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity model test class"""

    def test_attributes(self):
        """Test that the appropriate attributes are set"""
        a = Amenity()
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, 'name'))
        self.assertEqual(a.name, "")
