#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


"""Module handling city
"""


class City(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    state_id = ""
    name = ""

    def __init__(self, **kwargs):
        """_summary_
        """
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
