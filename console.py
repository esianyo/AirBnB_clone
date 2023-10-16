#!/usr/bin/python3
"""console for the airbnb clone program"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ class method for command line entry point"""
    prompt = '(hbnb) '

    def do_quit(self, s):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, s):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        """an empty line and ENTER should not execute anything"""
        pass

    def do_create(self, args):
        """creates and saves new instance of basemodel to json file"""
        args = args.split()
        if args is None:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes.get(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = args.split()
        if len(args) != 2:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args[1] == v.id:
                    print(v)
                    return
            print("** no instance found **")

    def do_all(self, args):
        """
        string representation of all instances
        based or not on the class name
        """
        args = args.split()
        if not args:
            for k, v in storage.all().items():
                print(v)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if args[0] == v.__class__.__name__:
                    print(v)
                    return
            print('[]')

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                args[3] = args[3].strip('"')
                try:
                    args[3] = int(args[3])
                except:
                    pass
                setattr(v, args[2], args[3])
                storage.save()
                return
            print("** no instance found **")

    def do_destroy(self, args):
        """ destroys instances for class name and id """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()