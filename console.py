#!/usr/bin/python3
"""
Command interpreter for AirBnB project
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the airBnB project"""
    prompt = '(hbnb) '

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emptyline(self):
        """Empty line input handler"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_quit(self):
        """Help command for quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Help command for EOF"""
        print("EOF command to exit the program\n")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = globals()[arg]()
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            obj_dict = storage.all()[args[0] + "." + args[1]].to_dict()
            print(obj_dict)
        except IndexError:
            if globals().get(args[0]) is None:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            del storage.all()[args[0] + "." + args[1]]
            storage.save()
        except IndexError:
            if globals().get(args[0]) is None:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        if len(args) == 0:
            objects = storage.all().values()
        elif globals().get(args[0]) is None:
            print("** class doesn't exist **")
            return
        else:
            objects = [obj for obj in storage.all().values()
                       if type(obj).__name__ == args[0]]
        print([str(object) for object in objects])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if globals().get(args[0]) is None:
            print("** class doesn't exist **")
            return

        try:
            obj = storage.all()[args[0] + "." + args[1]]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            attr_name = args[2]
            attr_value = args[3][1:-1]

            if attr_name in ['created_at', 'updated_at', 'id']:
                print(f"Can't update {attr_name}")
                return
            if hasattr(obj, attr_name):
                attr_value = type(getattr(obj, attr_name))(attr_value)
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                setattr(obj, attr_name, attr_value)
                obj.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    # def do_update(self, arg):
    #     """
    #     Update a class instance of a given id by adding or updating
    #     a given attribute key/value pair or dictionary
    #     """
    #     args = arg.split()
    #     objdic = storage.all()
    #     if len(args) == 0:
    #         print('** class name missing **')
    #         return
    #     elif globals().get(args[0]) is None:
    #         print("** class doesn't exist **")
    #         return False
    #     elif len(args) == 1:
    #         print('** instance id missing **')
    #         return False
    #     elif "{}.{}".format(args[0], args[1]) not in objdic.keys():
    #         print("** no instance found **")
    #         return False
    #     if len(args) == 2:
    #         print("** attribute name missing **")
    #         return False
    #     elif len(args) == 3:
    #         try:
    #             type(eval(args[2])) != dict
    #         except NameError:
    #             print("** value missing **")
    #             return False

    #     if len(args) == 4:
    #         obj = objdic[f"{args[0]}.{args[1]}"]
    #         if args[2] in obj.__class__.__dict__.keys():
    #             valtype = type(obj.__class__.__dict__[args[2]])
    #             obj.__dict__[args[2]] = valtype(args[3])
    #         else:
    #             obj.__dict__[args[2]] = args[3]
    #     elif type(eval(args[2])) == dict:
    #         obj = objdic["{}.{}".format(args[0], args[1])]
    #         for key, value in eval(args[2]).items():
    #             if (key in obj.__class__.__dict__.keys() and
    #                     type(type(obj).__dict__[key]) in {str, int, float}):
    #                 valtype = type(obj.__class__.__dict__[key])
    #                 obj.__dict__[key] = valtype(value)
    #             else:
    #                 obj.__dict__[key] = value
    #     storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""
        args = arg.split()
        count = 0
        try:
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
        except IndexError:
            pass
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        validcmds = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        match = re.search(r"\.", arg)
        if match is not None:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in validcmds.keys():
                    call = "{} {}".format(args[0], command[1])
                    return validcmds[command[0]](call)
        return super().default(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
