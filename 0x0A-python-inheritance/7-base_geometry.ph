#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        area geometry function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator value
        Args:
            name(string): name
            value(int): given value
        Raises:
            TypeError: when value is not integer
            ValueError: when value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
