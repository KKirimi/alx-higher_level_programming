#!/usr/bin/python3
# Write a class Square that defines a square by: (based on 5-square.py)
"""Define a class Square."""


class Square:
    """Square class."""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method for the class.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter and setter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Getter and setter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
        type(value[0]) is not int or type(value[1]) is not int or \
        value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return

        for k in range(self.__position[1]):
            print()

        for k in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
