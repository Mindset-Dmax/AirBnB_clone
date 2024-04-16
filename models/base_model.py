#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

"""
contains Base function
"""


class BaseModel:
    """
    class that defines all common attributes/methods for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates update_at with current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all the key/values of __dict__
        """
        dictFormat = self.__dict__.copy()
        dictFormat["__class__"] = self.__class__.__name__
        dictFormat["created_at"] = self.created_at.isoformat()
        dictFormat["updated_at"] = self.updated_at.isoformat()

        return dictFormat

    def __str__(self):
        """
        string representation of class instance or attributes
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
