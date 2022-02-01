#!/usr/bin/python3
"""
my int class
"""


class MyInt(int):
    """ my int class """
    def __eq__(self, nb):
        """ eq fn        """
        return False

    def __ne__(self, nb):
        """ ne fn """
        return True
