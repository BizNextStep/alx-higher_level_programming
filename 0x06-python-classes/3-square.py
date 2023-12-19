#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Class Square with size attribute and area method"""

    def __init__(self, size=0):
        """Initializes the square with a specified size."""
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Validates the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes and returns the area of the square."""
        return self.__size ** 2
