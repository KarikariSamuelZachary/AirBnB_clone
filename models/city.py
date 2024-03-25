#!/usr/bin/python3
"""City Module

This module conatins a class City that inherits from BaseMOdel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines Class city
    """
    state_id = ""
    name = ""
