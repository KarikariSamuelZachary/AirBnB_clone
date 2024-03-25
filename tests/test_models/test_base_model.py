#!/usr/bin/python3
"""
Test BaseModel module

Contains test cases for the base model
"""
import unittest
import uuid
import time
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """Tests for base model attrs and methods"""

    def setUp(self):
        """Set up dependencies for the tests"""
        self.bm = BaseModel()

    def test_attributes(self):
        """Test all attributes have been set"""
        self.assertTrue(hasattr(self.bm, 'id'))
        self.assertTrue(hasattr(self.bm, 'created_at'))
        self.assertTrue(hasattr(self.bm, 'updated_at'))
        self.assertEqual(type(self.bm.id), str)
        self.assertEqual(type(self.bm.created_at), datetime)
        self.assertEqual(type(self.bm.updated_at), datetime)

    def test_id(self):
        """Test two models won't have same id"""
        bm2 = BaseModel()
        self.assertNotEqual(self.bm.id, bm2.id)

    def test_create_obj_from_kwargs(self):
        """Test that the obj is created with kwargs if kwargs are passed in"""
        bm_dict = {
            'id': '1234',
            'created_at': '2022-05-17T18:28:42.152949',
            'updated_at': '2022-05-17T18:28:42.152949',
        }
        self.bm = BaseModel(**bm_dict)
        self.assertIsInstance(self.bm, BaseModel)
        self.assertEqual(self.bm.id, '1234')
        self.assertEqual(str(self.bm.created_at), '2022-05-17 18:28:42.152949')
        self.assertEqual(str(self.bm.updated_at), '2022-05-17 18:28:42.152949')

    def test_save(self):
        """
        Test that the save method updates the updated_at field and
        does not update the created_at field
        """
        # They're initially equal
        cr_a = self.bm.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        up_a = self.bm.updated_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        self.assertEqual(cr_a[:-6], up_a[:-6])  # Ignore microseconds

        old_created_at, old_updated_at = self.bm.created_at, self.bm.updated_at

        self.bm.save()
        new_up_a = self.bm.updated_at.strftime('%Y-%m-%d %H:%M:%S.%f')
        self.assertEqual(old_created_at, self.bm.created_at)
        self.assertNotEqual(up_a, new_up_a)

    def test_to_dict(self):
        """Test to_dict method"""
        bm_dict = self.bm.to_dict()
        self.assertTrue(isinstance(bm_dict, dict))
        self.assertTrue('__class__' in bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in bm_dict)
        self.assertTrue('created_at' in bm_dict)
        self.assertTrue('updated_at' in bm_dict)

    def test_str(self):
        """Test string representation of base model"""
        str_ = str(self.bm)
        self.assertTrue('[BaseModel]' in str_)
        self.assertTrue('id' in str_)
        self.assertTrue('created_at' in str_)
        self.assertTrue('updated_at' in str_)
