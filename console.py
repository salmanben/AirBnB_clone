#!/usr/bin/python3
"""Defines 'HBNBCommand' class."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """Defines  the command interpreter."""

    prompt = "(hbnb) "
    __av_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, line):
        """Creates instance from given class."""
        if line == '':
            print("** class name missing **")
        elif line not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        else:
            dynamic_class = globals()[line]
            new_inst = dynamic_class()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        line_arr = line.split(' ')
        if line == '':
            print("** class name missing **")
        elif line_arr[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        elif len(line_arr) <= 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == line_arr[0] and key.split('.')[1] == line_arr[1]:
                    inst = globals()[key.split('.')[0]](value)
                    print(inst)
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        line_arr = line.split(' ')
        if line == '':
            print("** class name missing **")
        elif line_arr[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        elif len(line_arr) <= 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == line_arr[0] and key.split('.')[1] == line_arr[1]:
                    del storage.all()[key]
                    storage.save()
                    break
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        if line == '':
            print("** class name missing **")
        elif line not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        else:
            my_list_str = []
            for inst in storage.all().values():
                if inst['__class__'] == line:
                    my_list_str.append(inst)
            print(my_list_str)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute."""
        type_casting_functions = {
            "int": int,
            "str": str,
            "float": float,
        }
        line_arr = line.split(' ')

        if line == '':
            print("** class name missing **")
        elif line_arr[0] not in HBNBCommand.__av_classes:
            print("** class doesn't exist **")
        elif len(line_arr) <= 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == line_arr[0] and key.split('.')[1] == line_arr[1]:
                    if len(line_arr) <= 2:
                        print("** attribute name missing **")
                    elif len(line_arr) <= 3:
                        print("** value missing **")
                    else:
                        attr_name = line_arr[2]
                        value = line_arr[3]
                        for data_type, cast_func in type_casting_functions.items():
                            if type(storage.all()[key][attr_name]).__name__ == data_type:
                                value = cast_func(value)
                                break

                        storage.all()[key][attr_name] = value
                        storage.save()
                    break

            else:
                print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
