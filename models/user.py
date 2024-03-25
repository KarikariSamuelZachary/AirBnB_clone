#!/usr/bin/python3
"""User Module

This model contains a class that inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Model

    Inherits from the BaseModel parent class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
