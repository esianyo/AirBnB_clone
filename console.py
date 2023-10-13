#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

import cmd


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
