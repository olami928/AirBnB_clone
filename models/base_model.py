#!/usr/bin/python3
"""
This is a class BaseModel of the project
"""


from datetime import datetime
import uuid


class BaseModel:
    """
    This is a class defintion of the BaseModel class.
    """
    
    def __init__(self):
        """
        Initializes a new BaseModel instance
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This is the string representation of BaseModel."""

        return (f"{[type(self).__name__]} ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance updated_at with the current datetime."""

        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ Returns a dictionary conatining all keys/values of __dict__
        of the instance.
        """

        obj_dict = {**self.__dict__}
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
