#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


"""_summary_
"""


class Amenity(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
    