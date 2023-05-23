#!/usr/bin/python3
def fizbuz():
    for i in range(1,101):
        """Print the numbers from 1 to 100 separated by a space.
    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
        if  i%3 == 0 and i%5 == 0:
                print("fizzbuzz", end=" ")
        elif i%3 == 0 :
            print("fizz", end=" ")
        elif i%5 == 0:
            print("buzz", end=" ")
        else:
            print("{}".format(i), end=" ")


