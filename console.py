#!/usr/bin/python3
"""
The console module which uses the cmd module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb) '
    file = None

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
