#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class represents a square with a private size attribute and a private position attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a specified size and position."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character and the specified position"""
        if self.__size == 0:
            print()
        else:
            position_x, position_y = self.__position
            for i in range(self.__size):
                for j in range(self.__size):
                    print(" ", end="")
                    print("#" * self.__size, end=" ")
                    print(" ", end="")
                    position_x += 1
                    if position_x >= position_y:
                        position_y += 1
        print(" ")
