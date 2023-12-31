#!/usr/bin/python3
"""a script for the entry point to the command interpreter"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class definition"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """The default cmd behaviour for invalid  inputs"""
        args_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        exact = re.search(r"\.", arg)
        if exact is not None:
            args = [arg[:exact.span()[0]], arg[exact.span()[1]:]]
            exact = re.search(r"\((.*?)\)", args[1])
            if exact is not None:
                command = [args[1][:exact.span()[0]], exact.group()[1:-1]]
                if command[0] in args_dict.keys():
                    call = "{} {}".format(args[0], command[1])
                    return args_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Retrieve the number of instances of a given class.
        Usage: count <class> or <class>.count()
        """
        args = split(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        Usage: show <class_name> <id>
        """
        args = split(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = split(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all [<class name>]
        """
        args = split(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        """
        args = split(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = val_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
            storage.save()
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for ki, va in eval(args[2]).items():
                if (ki in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[ki]), {str, int, float}):
                    val_type = type(obj.__class__.__dict__[ki])
                    obj.__dict__[ki] = val_type(va)
                else:
                    obj.__dict__[ki] = va
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
