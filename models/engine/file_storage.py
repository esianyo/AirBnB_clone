#!/usr/bin/python3
"""Type module FileStorage"""

import json
import uuid


class FileStorage:
    """Type class File Storage"""
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """Type method all"""
        return self.reload()

    def new(self, obj):
        """Type method new"""
        from models.base_model import BaseModel
        import uuid

        class_name = str(obj.__class__.__name__)
        obj_id = str(obj.id)
        obj_str = class_name + "." + obj_id
        FileStorage.__objects[obj_str] = obj

    def save(self):
        """Type method save"""
        from models.base_model import BaseModel
        new_dict = {}

        for keys in FileStorage.__objects.keys():
            new_dict[keys] = (FileStorage.__objects[keys]).to_json()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Type method reaload"""
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
        try:
            with open(FileStorage.__file_path,
                      "r", encoding="utf-8") as f:
                reloaded = json.load(f)
                for key, value in reloaded.items():
                    class_n = classes.get(reloaded[key].get('__class__'))
                    self.__objects[key] = class_n(**reloaded[key])
                return self.__objects
        except:
            return {}