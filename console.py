#!/usr/bin/python3
"""
The console module which uses the cmd module
"""
import cmd
from models.base_model import BaseModel
import models
import shlex    # for splitting a line along spaces
# except those in  double quotes


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb) '
    file = None

    valid_classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel \
            and prints the id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        val_classes = HBNBCommand.valid_classes
        if args[0] in val_classes:
            new_instance = val_classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance \
            based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class anme and id"""
        # Changes are saved to the JSON file
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances \
            based or not on the class name"""
        # If the class name doesn’t exist, print ** class doesn't exist **
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in HBNBCommand.valid_classes:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id \
            by adding or updating attribute"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """End of file\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the prompt\n"""
        quit()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
