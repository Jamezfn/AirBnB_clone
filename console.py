#!/usr/bin/python3
"""
Command interpreter for AirBnB clone
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'State': State,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
        }

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""
    prompt = "(hbnb) "
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOL(self, ags):
        """EOL command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on emptyline input"""
        pass

    def help_quit(self, args):
        """Quit commant to exit the program"""
        print("Quit command to exit the program")

    def do_create(self, arg):
        """create <class name>: create new instance, save, and print id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class names"""
        args = shlex.split(arg)
        objs = storage.all()
        out_list = []
        if len(args) == 0:
            for obj in objs.values():
                out_list.append(str(obj))
        else:
            cls_name = args[0]
            if cls_name not in classes:
                print("** class doesn't exist **")
                return
            for key, obj in objs.items():
                if key.startswith(f"{cls_name}"):
                    out_list.append(str(obj))

        print(out_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attr = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attr_value = args[3]
        obj = objs[key]
        if hasattr(obj, attr_value):
            current = getattr(obj, attr_value)
            cast_value = None
            try:
                if isinstance(current, int):
                    cast_value = int(attr_value)
                elif isinstance(current, float):
                    cast_value = float(attr_value)
                else:
                    cast_value = attr_value
            except Exception:
                cast_value = attr_value
        else:
            if attr_value.isdigit():
                cast_value = int(attr_value)
            else:
                try:
                    cast_value = float(attr_value)
                except ValueError:
                    cast_value = attr_value
        setattr(obj, attr, cast_value)
        obj.save()

    def default(self, arg):
        """Retrieves all instances of a class; <class name>.all()"""
        if '.' not in arg:
            return False
        args_list = arg.split('.')
        cls_name, method = args_list
        if cls_name in classes and method == "all()":
                return self.do_all(cls_name)
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
