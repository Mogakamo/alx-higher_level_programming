#!/usr/bin/python3
# 1-rectangle.py

"""Defines a Rectangle class
"""

class Rectangle:
    """Represent a rectangle
    """

    def __init__(self, width = 0, height = 0):
        """Initialize a new Rectangle
        
        Args:
            width (int): The width of the new rectangle
            height (int): The height of a new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
