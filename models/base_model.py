#!/bin/usr/python3

"""The Base_Model

This module contains a class that defines all common attributes
for other classes
"""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common methods for classes"""

    def __init__(self, *args, **kwargs):
        """
        This  method initializes the model
        Args:
            *args : Takes any data type as input
            **kwargs : Takes a dictionary with key value pairs
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns the string repr of the base model class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """updates updated_at with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns __dict__ instance of the class"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
