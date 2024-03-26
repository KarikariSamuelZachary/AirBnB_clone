#!/usr/bin/python3
"""Console module"""

import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a newline for better output formatting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints its id"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if not arg:
            print([str(val) for val in storage.all().values()])
        else:
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            print([str(val) for val in cls.all()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
