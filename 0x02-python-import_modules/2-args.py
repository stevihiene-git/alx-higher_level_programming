#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)-1

    if arg_count == 0:
        print("0 argument")
    elif arg_count == 1:
        print("1 argument")
    else:
        for x in range(arg_count):
            print("{} : {}".format(x+1, sys.argv[x+1]))
