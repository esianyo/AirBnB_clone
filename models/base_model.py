#!/usr/bin/python3
"""Creates a class called BaseModel"""

from datetime import datetime
from uuid import uuid4
"""Contains all common modules for the AirBnB clone project

    Returns:
        _type_: string format
"""


class BaseModel:
    """
    contains all public instance attributes that will be access by all methods.
    """

    def __init__(self):
        """ initializing public attributes for id, date, and time"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """string representation of name and id values

        Returns:
            str: paired values in dictionary format
        """
        return "{}".format(self.__dict__)

    def save(self):
        """ updates date and time after changes have been made"""
        update_at = datetime.now()

    def to_dict(self):
        """ returns date and time in isoformat"""
        toDict = {}

        toDict["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                toDict[key] = val.isoformat()
            else:
                toDict[key] = val
        return toDict

    def __init__(self, **kwargs):
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dtm_obj = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dtm_obj)

                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "\n".join(f"{key}: {val}" for key, val in self.__dict__.items())
