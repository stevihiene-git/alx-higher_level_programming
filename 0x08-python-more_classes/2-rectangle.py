#!/usr/bin/python3
#2-rectangle.py
"""define a class Rectangle"""


class Rectangle:
    """represent a Rectangle"""
	
    def __init__(self, width=0,height=0):
	"""initialize a new Rectangle
		
	Args:
	    width (int):The width of the new Rectangle.
	    height (int):The height of the new Rectangle.
	"""
	self.width = width
	self.width = height
		
    @property
    def width(self):
	"""get/set current width of the rectangle"""
	return self.__width
		
    @width.setter
    def width(self, value):
	if not isinstance(value, int):
	    raise TypeError("width must be an integer")
	elif value < 0:
	    raise ValueError("width must be >= 0")
	self.__width = value
			
    @property
    def height(self):
	"""get/set current height of the rectangle"""
	return self.__height
		
    @height.setter
    def height(self, value):
	if not isinstance(value, int):
	    raise TypeError("height must be an integer")
	elif value < 0:
	    raise ValueError("width must be >= 0")
	self.__height = value

    def area(self):
		"""returns the area of the rectangle"""
		return (self.__width*self.__height)


    def perimeter(self):
	"""returns the area of the rectangle"""
	if self.__height == 0 or self.__width ==0:
	    return (0)
	return ((2*(self.__width + self.__height))
