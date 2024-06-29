#!/usr/bin/python3
"""This is the class of place."""


from models.base_model import BaseModel


class Place(BaseModel):
    """Places to store places information."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """This is the initialization of the amenity class."""

        super().__init__(*args, **kwargs)
