#!/usr/bin/python3
"""
Base module

This module contains the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Contains all common model attributes and methods from which
    all other models would inherit
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new model
        Args:
            *args (any type): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue

                if key in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, val)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """ Return the print/str representation of the BaseModel instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Saves the model instance by updating the updated_at attr"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """Returns a dictionary of all key/values of a model instance"""
        model_data = self.__dict__.copy()
        model_data['__class__'] = type(self).__name__
        model_data['created_at'] = self.created_at.isoformat()
        model_data['updated_at'] = self.updated_at.isoformat()

        return model_data
