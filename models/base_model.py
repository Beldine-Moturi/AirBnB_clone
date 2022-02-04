#!/usr/bin/python3
"""
The Base Model module which defines the BaseModel class
which is the base class for all other classes in this project
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

        if len(kwargs) > 0:
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

    def save(self):
        """update updated_at with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Returns a string representation of objects"""

        return "[{}] ({}) {}".format(
                        type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Adds a new key: __class__ which holds the value of the class name
        of the object"""

        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": type(self).__name__})
        iso_created = my_dict["created_at"]
        iso_updated = my_dict["updated_at"]
        my_dict["created_at"] = str(iso_created.isoformat())
        my_dict["updated_at"] = str(iso_updated.isoformat())
        return my_dict
