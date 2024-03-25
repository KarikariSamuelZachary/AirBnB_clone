#!/usr/bin/python3
"""Review Module

This module conatins a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Initialisation of the Reciew Class
    """
    place_id = ""
    user_id = ""
    text = ""
