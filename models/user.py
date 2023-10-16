#!/usr/bin/python3
from models.base_model import BaseModel


"""user module"""


class User(BaseModel):
    """class for the airbnb user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """method to handle user commands"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
