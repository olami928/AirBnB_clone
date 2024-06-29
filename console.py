#!/usr/bin/python3
"""This is the cmd module class defintion."""


import cmd
from models import storage
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel
        or User, saves it, and prints the id"""
        if not args:
            print("** class name missing **")
            return
        try:
            if args == "BaseModel":
                obj = BaseModel()
            elif args == "User":
                obj = User()
            else:
                print("** class doesn't exist **")
                return
            obj.save()
            print(obj.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of
        an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        class_name = arg_list[0]
        instance_id = arg_list[1]
        key = class_name + "." + instance_id
        try:
            obj = storage.all()[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        class_name = arg_list[0]
        instance_id = arg_list[1]
        key = class_name + "." + instance_id
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representations of all
        instances based or not on the class name"""
        if not args:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args.split()[0]
            if class_name not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name])

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if len(arg_list) < 4:
            print("** instance id missing**" if len(arg_list) == 1 else "** attribute name missing **" if len(arg_list) == 2 else "** value missing **")
            return
        class_name = arg_list[0]
        instance_id = arg_list[1]
        attr_name = arg_list[2]
        attr_value = arg_list[3]
        key = class_name + "." + instance_id
        try:
            obj = storage.all()[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except KeyError:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
