#!/usr/bin/python3
"""This is the console class."""


import cmd
import ast  # Import ast to safely evaluate string representations of Python literals
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""
    prompt = '(hbnb) '

    def do_create(self, args):
        """Create a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        cls_name = args[0]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        cls = eval(cls_name)  # Convert string class name to class object
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, instance_id = args[0], args[1]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """Destroy an instance of a class"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, instance_id = args[0], args[1]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.delete(storage.all()[key])
        storage.save()

    def do_update(self, args):
        """Update an instance of a class"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 3:
            print("** instance id missing **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        cls_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        storage.update(obj, attr_name, attr_value)

    def do_all(self, args):
        """Show all instances of a class"""
        if args:
            if args not in ["State", "City", "Amenity", "Place", "Review", "User"]:
                print("** class doesn't exist **")
                return
            cls = eval(args)  # Convert string class name to class object
            instances = [str(obj) for obj in storage.all(cls).values()]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_class_all(self, args):
        """Retrieve all instances of a class
        using <class name>.all()"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        cls_name = args[0]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        cls = eval(cls_name)  # Convert string class name to class object
        instances = [f"[{cls.__name__}] ({obj.id}) {obj.to_dict()}"
                     for obj in storage.all(cls).values()]
        print(instances)

    def do_count(self, args):
        """Retrieve the number of instances
        of a class using <class name>.count()"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        cls_name = args[0]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        cls = eval(cls_name)  # Convert string class name to class object
        count = len(storage.all(cls))
        print(count)

    def do_show_class(self, args):
        """Retrieve an instance based on its ID
        using <class name>.show(<id>)"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, instance_id = args[0], args[1]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy_class(self, args):
        """Destroy an instance based on its ID using
        <class name>.destroy(<id>)"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, instance_id = args[0], args[1]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.delete(storage.all()[key])
        storage.save()

    def do_update_class(self, args):
        """Update an instance based on its ID using
        <class name>.update(<id>, <attribute name>, <attribute value>)"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 3:
            print("** instance id missing **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        cls_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        storage.update(obj, attr_name, attr_value)

    def do_update_dict(self, args):
        """Update an instance based on its ID with a dictionary"""
        if not args:
            print("** class name missing **")
            return
        try:
            args = args.split(maxsplit=1)
            cls_name = args[0]
            if len(args) < 2:
                print("** dictionary representation missing **")
                return
            instance_id, attr_dict_str = args[1].split(maxsplit=1)
            attr_dict = ast.literal_eval(attr_dict_str)
        except (ValueError, SyntaxError, IndexError):
            print("** invalid dictionary representation **")
            return
        if cls_name not in ["State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        for attr_name, attr_value in attr_dict.items():
            setattr(obj, attr_name, attr_value)
        storage.update(obj, **attr_dict)

    def do_quit(self, args):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, args):
        """Handle end-of-file"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
