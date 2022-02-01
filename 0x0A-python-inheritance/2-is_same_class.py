#!/usr/bin/python3
"""compare obj to instance"""


def is_same_class(obj, a_class):
    """function to comapre obj to instance"""
    if type(obj) == a_class:
        return True
    else:
        return False
