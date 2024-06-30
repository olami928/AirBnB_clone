#!/usr/bin/python3
"""This is a FileStorage Class."""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, val in self.all().items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    cls_name = obj_data['__class__']
                    cls = globals()[cls_name]
                    obj = cls(**obj_data)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
