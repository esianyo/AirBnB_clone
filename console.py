#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models import storage
import json
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ class method for command line entry point"""
    prompt = "(hbnb) "

    def Quit(self, command):
        """handles the exit"""
        return True
    
    def Help(self, command):
        """Handles help.

        Args:
            command (string): Command Input
        """
        return True
    
    def Eof(self, command):
        """Handles end of file.

        Args:
            command (empty): no command entered
        """
        return True

    def Create(self, command):
        """creates and saves new instance of basemodel to json file"""
        command = command.split()
        if not command:
            print("** class name missing **")
        elif command[0] not in classes:
            print ("** class doesn't exist **")
        else:
            new_instance = classes.get(command[0])()
            print(new_instance.id)
            storage.save()

    def Show(self, command):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        command = command.split()
        if len is not 2:
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, val in storage.all().items():
                if command[1] == val.id:
                    print(val)
                    return;
            print("** no instance found **")

    def All(self, command):
        """
        string representation of all instances 
        based or not on the class name
        """
        command = command.split()
        if not command:
            for key, val in storage.all().items():
                print(val)
        elif command[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, val in storage.all().items():
                if command[0] == val.__class__.__name__:
                    print(val)
                    return""
            print("[]")

    def Update(self, command):
        """Updates an instance based on the class name and id"""
        command = command.split()
        if command is None:
            print("** class name missing **")
            return""
        elif len(command) < 2:
            print("** class doesn't exist **")
            return""
        elif len(command) < 3:
            print("** attribute name missing **")
            return""
        elif len(command) < 4:
            print("** value missing **")
            return""
            
        if command[0] not in classes:
            print("** class doesn't exist **")
            return""
        for key, val in storage.all().items():
            if command[1] == val.id:
                command[3] = command[3].strip('"')
                try:
                    command[3] = int(command[3])
                except:
                    pass
                setattr(val, command[2], command[3])
                storage.save()
                return""
            print("** no instance found **")

    def Destroy(self, command):
        """ destroys instances for class name and id """
        command = command.split()
        if command is None:
            print("** class name missing **")
            return""
        elif len(command) < 2:
            print("** instance id missing **")
            return""
        if command[0] not in classes:
            print("** class doesn't exist **")
            return""
        for key, val in storage.all().items():
            if command[1] == val.id:
                del storage.all()[k]
                storage.save()
                return""
        print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()        

    
        