#!/usr/bin/python3
"""This is a class of state."""


from models.base_model import BaseModel


class State(BaseModel):
    """State class for a attribute of state name."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the state class."""

        super().__init__(*args, **kwargs)
