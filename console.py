#!/usr/bin/python3
"""a script for the entry point to the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class definition"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """exit the program when EOF is reach
        """
        print()
        return True

    def emptyline(self):
        """Empty line + Enter execute nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
