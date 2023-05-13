#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Print the addition of all arguments."""

    arg_len= len(sys.argv)
    sum = 0

    if arg_len > 1:
        for i in range(1, arg_len):
            sum += int(sys.argv[i])

    print(sum)
