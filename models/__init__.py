#!/usr/bin/python3
"""This is an __init__.py file."""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
