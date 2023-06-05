#!/usr/bin/python3
#6-rectangle.py
"""define a class Rectangle"""


class Rectangle:
    """represent a Rectangle

    Attribute:
        number_of_instances: The number of rectangle instances.
        print_symbol: the symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

	
    def __init__(self, width=0,height=0):
	"""initialize a new Rectangle
		
	Args:
	    width (int):The width of the new Rectangle.
	    height (int):The height of the new Rectangle.
	"""
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

