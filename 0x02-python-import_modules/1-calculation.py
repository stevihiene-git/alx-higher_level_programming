#!/usr/bin/python3
if __name__ == "__main__":
    """

    Prints the result of the addition, substract, multiplication
    and division between two numbers

    """
    from calculator_1 import add,sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a,b)))
    print("{} - {} = {}".format(a, b, sub(a,b)))
    print("{} * {} = {}".format(a, b, mul(a,b)))
    print("{} / {} = {}".format(a, b, div(a,b)))
