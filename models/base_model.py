#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4
"""Contains all common modules for the AirBnB clone project

    Returns:
        _type_: string format
"""


class BaseModel:
    """
    Base Model
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return "{}".format(self.__dict__)

    def save(self):
        update_at = datetime.now()

    def to_dict(self):
        toDict = {}

        toDict["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                toDict[key] = val.isoformat()
            else:
                toDict[key] = val
        return toDict

