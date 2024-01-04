#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0  # Class attribute to track the number of instances

    def __init__(self, width=0, height=0):
        """Initialize width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    # ... (other methods remain the same)

    def __del__(self):
        """Print message when instance is 
        deleted and decrement the number of instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
