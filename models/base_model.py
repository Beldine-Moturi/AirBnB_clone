#!/usr/bin/python3
"""
The Base Model module
Defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    The "BaseModel" class
    Defines all common attributes/methods for other model classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel object"""

        if len(kwargs) > 0:     # kwargs is not empty
            for key in kwargs:
                if key not in ['__class__', 'created_at', 'updated_at']:
                    setattr(self, key, kwargs[key])
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(kwargs[key],
                                              "%Y-%m-%dT%H:%M:%S.%f"))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values\
             of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        # test -> what is in new_dict
        # print("\n ======== {}=======\n".format(new_dict))
        new_dict["created_at"] = str(new_dict["created_at"].isoformat())
        if "updated_at" in new_dict:
            new_dict["updated_at"] = str(new_dict["updated_at"].isoformat())

        new_dict["__class__"] = type(self).__name__

        return new_dict
