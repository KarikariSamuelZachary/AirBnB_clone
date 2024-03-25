#!/bin/usr/python3
"""File_Storage model

This module contains a class that stores instances of other classes
in a json file
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """This class stores instances of other classes
    by serializing and deserializing
    """
    __file_path = "data.json"
    __objects = dict()

    def all(self) -> dict:
        """Returns a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.id"
        FileStorage.__objects["key"] = obj

    def save(self):
        """serializes __objects to the JSON file (__file_path)"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized["key"] = value.to_dict()
            with open(FileStorage.__file_path, mode="w") as f:
                json.dump(serialized, f)

    def reload(self):
        """Deserializes json objs from json file"""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8')\
                    as f:
                loaded_objs = json.load(f)

            for key, obj in loaded_objs.items():
                class_name = obj['__class__']
                FileStorage.__objects[key] = eval(class_name)(**obj)
        except FileNotFoundError:
            pass
