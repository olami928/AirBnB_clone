#!/usr/bin/python3
"""This si the city class."""


from models.base_model import BaseModel


class City(BaseModel):
    """City class for storing city information."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the city class."""

        super().__init__(*args, **kwargs)
