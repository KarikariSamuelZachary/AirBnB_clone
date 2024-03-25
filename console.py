#!/usr/bin/python3
"""Console module

This model contains a class that implements the
main entry point to a command line interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """This function does nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
