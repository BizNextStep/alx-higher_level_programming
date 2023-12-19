#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class represents a square with a private size attribute"""

    def __init__(self, size=0):
        """Initializes the square with a specified size."""
        self.__size = size

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

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
