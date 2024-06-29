#!/usr/bin/python3
"""
This is the class FileSrorage.
"""


import json


class FileStorage:
    """Definition of the FileStorage class."""

    def __init__(self):
        """Initializes the FileStorage Class."""

        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Returns the dict __objects which stores all objects."""
        return (self.__objects)

    def new(self, obj):
        """Adds a new object to __objects."""

        class_name = obj.__class__.__name__
        object_id = obj.id
        key = (f"{class_name}.{object_id}")
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""

        object_dict = {}
        for key, obj in self.__objects.items():
            object_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(object_dict, file)

    def reload(self):
        """Deserialaizes the JSON file to __objects."""

        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                object_dict = json.load(file)

                for key, value in object_dict.items():
                    class_name = value.pop('__class__')
                    cls = globals()[class_name]
                    instance = cls(**value)
                    self.__objects[key] = instance

        except FileNotFoundError:
            pass
