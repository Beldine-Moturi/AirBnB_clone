#!/usr/bin/python3
"""
The Base Model module
Defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    The "BaseModel" class
    Defines all common attributes/methods for other model classes
    """
    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel object"""

        if len(kwargs) > 0:     #kwargs is not empty
            for key in kwargs:
                if key not in ['__class__', 'created_at', 'updated_at']:
                    setattr(self, key, kwargs[key])

            for key in ['created_at', 'updated_at']:
                # Converting the keys in this list to datetime objects
                setattr(self, key, datetime.strptime(kwargs[key],
                "%Y-%m-%dT%H:%M:%S.%f"))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel object"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """'save' method
        Updates the public instance attribute 'updated_at'\
             with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values\
             of __dict__ of the instance"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        new_dict = {}

        for k, v in self.__dict__.items():
            if k not in new_dict:
                new_dict.update({k: v})
        if '__class__' not in self.__dict__.items():
            new_dict.update({'__class__': self.__class__.__name__})

        return new_dict
