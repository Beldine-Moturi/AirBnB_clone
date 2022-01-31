#!/usr/bin/python3
"""
The Base Model module which defines the BaseModel class
which is the base class for all other classes in this project
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    The "BaseModel" class
    Defines all common attributes/methods for other model classes
    """

    def __init__(self):
        """Initializes a BaseModel object"""

        self.id = str(uuid.uuid4())
