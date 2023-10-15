#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


"""
Module handling state
"""

class State(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """'__init__ for state"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
