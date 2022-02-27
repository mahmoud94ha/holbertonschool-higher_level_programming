#!/usr/bin/python3
"""
square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> -
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, s):
        """ size setter """
        if not isinstance(s, int):
            raise TypeError("width must be an integer")
        if s <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = s

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.size = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a square
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
