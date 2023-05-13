#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    sys_arg = sys.argv
    arg_lenght = len(sys_arg) - 1

    if arg_lenght > 1:
        print(arg_lenght, 'arguments:')
        for i in range(1, arg_lenght + 1):
            print('{:d}: {}'.format(i, sys_arg[i]))
    elif arg_lenght == 1:
        print(arg_lenght, 'argument:')
        for i in range(1, arg_lenght + 1):
            print('{:d}: {}'.format(i, sys_arg[i]))
    elif l_av == 0:
        print(arg_lenght, 'arguments.')
