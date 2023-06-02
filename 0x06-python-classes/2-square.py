#!/usr/bin/python3

class Square(self, size):
    """this represent a square"""


    def __init__(self,size=0):
        """initializing a new square
       
        Args:
        size(int):The size of the new squre.
        """
        if not isinstance(size, int):
            raise TypeError("size should be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
