#!/usr/bin/python3
"""This is the class for review."""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class to store review information."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the review class."""

        super().__init__(*args, **kwargs)
