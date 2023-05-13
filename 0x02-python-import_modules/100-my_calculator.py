#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """
    Handles basic operations

    Performs basic operations like addition, substraction,
    multiplication and division between two numbers.

    The program will execute an operation between two numbers
    selected by the operator sent to the program.
    """
    arg_len = len(argv) - 1

    if arg_len == 3:
        operator = argv[2]
        num_a = int(argv[1])
        num_b = int(argv[3])
        if operator == '+':
            func = add(num_a, num_b)
            print('{:d} + {:d} = {:d}'.format(num_a, num_b, func))
            exit(0)
        elif operator == '-':
            func = sub(num_a, num_b)
            print('{:d} - {:d} = {:d}'.format(num_a, num_b, func))
            exit(0)
        elif operator == '*':
            func = mul(num_a, num_b)
            print('{:d} * {:d} = {:d}'.format(num_a, num_b, func))
            exit(0)
        elif operator == '/':
            func = div(num_a, num_b)
            print('{:d} / {:d} = {:d}'.format(num_a, num_b, func))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
