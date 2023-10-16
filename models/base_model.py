#!/usr/bin/python3
""" creates the base model for airbnb project"""


from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    contains all public instance attributes that will be access by all methods.
    """

    def __init__(self, *args, **kwargs):

        if len(kwargs) is not 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates date and time after changes have been made"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """string representation of name and id values

        Returns:
            str: paired values in dictionary format
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_json(self):
        """returns values in json format"""
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if isinstance(value, (datetime, uuid.UUID, tuple, set)):
                if type(value) is datetime:
                    value = value.isoformat()
                new_dict.update({key: str(value)})
        new_dict['__class__'] = str(self.__class__.__name__)
        return new_dict

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictFormat[key] = value.isoformat()
            else:
                dictFormat[key] = value
        return dictFormat
