#!/usr/bin/python3
if __name__ == "__main__":
    """
    Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """

    import sys
    arg_count = len(sys.argv)-1

    if arg_count == 0:
        print("0 argument")
    elif arg_count == 1:
        print("1 argument")
    else:
        for x in range(arg_count):
            print("{} : {}".format(x+1, sys.argv[x+1]))
