#!/usr/bin/python3
"""
Command interpreter for AirBnB clone
"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
