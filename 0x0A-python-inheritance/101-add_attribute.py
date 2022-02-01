#!/usr/bin/python3
"""
add attribute function
"""


def add_attribute(ob_, name, value):
    """ add fn """
    if not hasattr(ob_, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob_, name, value)
