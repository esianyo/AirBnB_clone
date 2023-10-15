#!/usr/bin/python3
""" creates a class called filestorage"""

import models
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class FileStorage:
    __file_path = "file.json"
    __objects = {}


def all(self):
    """
    public method that returns dictionary objects
    """
    return self.__objects


def new(self, obj):
    """
    public methods that sets value in dictionary object

    Args:
        obj (_type_): value to be set
    """
    key = obj.__class__.__name__ + "." + obj.id
    self.__objects[key] = obj


def save(self):
    """ method that serializes a dictionary to json file"""
    objDict = {}
    for key, val in FileStorage.__objects.items():
        objDict[key] = val.toDict()

    with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
        json.dump(objDict, fd)


def reload(self):
    """deserialises json string to dict string"""
    objDict = None
    try:
        with open(FileStorage.__file_path, "r", encoding="utf-8") as fd:
            objDict = json.load(fd)
        for key, val in FileStorage.__objects.items():
            class_name = val["__class__"]
            class_name = models.classes[class_name]
            FileStorage.__objects[key] = class_name(**val)            
    except FileNotFoundError:
        pass
