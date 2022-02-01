#!/usr/bin/python3
""" inheritance """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """ init fn """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area fn """
        return (self.__size * self.__size)
