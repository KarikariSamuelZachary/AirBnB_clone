#!/usr/bin/python3
"""
Storage module

This module contains a classe that helps store other class objs
"""
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'data.json'
    __objects = dict()

    def all(self) -> dict:
        """Returns all objects in a dictionary"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """Sets a new obj in self.__objects with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{str(obj.id)}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objs and saves to json file"""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

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
