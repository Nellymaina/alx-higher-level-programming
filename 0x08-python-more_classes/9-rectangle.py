#!/usr/bin/python3
"""Definition of a Rectangle class"""


class Rectangle:
    """Declaration of the Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of the Rectangle instance"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the with of a Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int) : new with of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int) : new height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        str_arr = []
        for i in range(self.__height):
            new_arr = []
            [new_arr.append(str(self.print_symbol))
             for j in range(self.__width)]
            str_arr.append("".join(new_arr))
        return "\n".join(str_arr)

    def __repr__(self):
        """Returns a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints text when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based of the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if (area_1 > area_2 or area_1 == area_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with the
        dimension of a square
        """
        return cls(size, size)
