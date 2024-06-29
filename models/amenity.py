#!/usr/bin/python3
"""This is a class of Amenity."""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for storing amenities information."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initilaization of the amenity class."""

        super().__init__(*args, **kwargs)
