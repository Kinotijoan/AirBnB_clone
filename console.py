#!/usr/bin/python3
"""Entry pont to the command interptater"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """class for the command interprater"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print('Exiting...')
        return True

    def default(self, line):
        """Handle unknown commands"""
        print(f"Unknown command: {line}")
        return False

    def emptyline(self):
        """Handle empty input lines"""
        pass

    def help(self):
        """Print help message"""
        print("This is a command interpreter. Commands:")
        print("  quit - quit the program")
        print("EOF - End of file ")
        print("  help - print this message")

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        obj = storage.classes[class_name]()
        storage.new(obj)
        storage.save()
        print(obj.id)

    def do_show(self, arg):
        """prints the string representation of the class"""
        args = arg.split()
        if args == "":
            print("**Class name missing**")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("**class doesn't exist**")
            return
        class_id = args[1]
        if class_id == []:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """deletes an instance based on class name and id"""
        args = arg.split()
        if args == "":
            print("**Class name missing**")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("**class doesn't exist**")
            return
        class_id = args[1]
        if class_id == []:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        if arg != "":
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == args[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, arg):
        """Counts the instances of a class.
        """
        args = arg.split(' ')
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    args[0] + '.')]
            print(len(matches))

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
