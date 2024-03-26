#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for AirBnB """
    prompt = '(hbnb) '

    def emptyline(self):
        """ Do nothing if an empty is entered """
        pass

    def default(self, arg):
        """ Default behavior for console """
        methods = {
                "all": self.do_all,
                "show": self.do_show,
                "count": self.do_count,
                "destroy": self.do_destroy,
                "update": self.do_update
                }
        line = re.search(r"\.", arg)
        if line is not None:
            cls = arg[:line.span()[0]].strip()
            method_args = arg[line.span()[1]:]
            method_args_ = re.search(r"\((.*?)\)", method_args)
            if method_args_ is not None:
                method = method_args[:method_args_.start()]
                args = method_args_.group(1).replace('"', '').replace(',', '')
            if cls in classes and method in methods:
                call = f"{cls} {args}"
                methods[method](call)
            else:
                print(f"** Unknown syntax: {arg}")

    @classmethod
    def line_check(self, arg):
        """ Checks for emptyline or class existing """
        if len(arg) == 0:
            print('** class name missing **')
            return False
        elif arg not in classes:
            print("** class doesn't exist **")
            return False
        return True

    @classmethod
    def parse(self, arg):
        braces_search = re.search(r"\{(.*?)\}", arg)
        brackets_search = re.search(r"\[(.*?)\]", arg)
        if braces_search is None:
            if brackets_search is None:
                return [i.strip(",") for i in split(arg)]
            else:
                lexer = split(arg[:brackets_search.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets_search.group())
                return retl
        else:
            lexer = split(arg[:braces_search.span()[0]])
            ret_l = [i.strip(",") for i in lexer]
            ret_l.append(braces_search.group())
            return ret_l

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit the program also\n'
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel and saves it """
        if self.line_check(arg):
            cls = classes[arg]
            obj = cls()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation base on the class name and id """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            cls = arg.split(' ')[0]
            if self.line_check(cls):
                if len(arg.split(" ")) == 1:
                    print('** instance id missing **')
                else:
                    id_ = arg.split(' ')[1]
                    key = f"{cls}.{id_}"
                    try:
                        print(storage._FileStorage__objects[key])
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an object from storage engine """
        cls = arg.split(' ')[0]
        dictobj = storage.all()
        if self.line_check(cls):
            if len(arg.split(" ")) == 1:
                print('** instance id missing **')
            else:
                try:
                    id_ = arg.split(" ")[1]
                    key = f"{cls}.{id_}"
                    del dictobj[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, arg):
        """ Prints all string representaton of all instances """
        arg = arg.strip()
        all_objs = storage.all()
        str_repr = ""
        if len(arg) == 0:
            for key, value in all_objs.items():
                str_repr += str(value)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
            else:
                for key, value in all_objs.items():
                    cls = key.split(".")[0]
                    if cls == arg:
                        str_repr += str(value)
        if len(str_repr) != 0:
            print(str_repr)

    def do_count(self, arg):
        """ Returns the number of instances of arg """
        arg = arg.strip()
        count = 0
        for obj in storage.all().values():
            if arg == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>)"""
        argl = self.parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
