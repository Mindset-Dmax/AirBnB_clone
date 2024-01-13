#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

"""
contains Base function
"""


class BaseModel:
    """
    class taht defines all common attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string representation of class instance or attributes
        """
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """
        updates update_at with current datetime
        """
        updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all the key/values of __dict__
        """
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat
