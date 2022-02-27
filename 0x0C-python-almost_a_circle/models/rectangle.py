#!/usr/bin/python3
"""
calss Rectangle
"""


from models.base import Base


class Rectangle (Base):
    """
    Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, w):
        """ width setter """
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, h):
        """ height setter """
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area value of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        by taking care of x and y
        """
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.__width = kwargs['width']
                    if i == 'height':
                        self.__height = kwargs['height']
                    if i == 'x':
                        self.__x = kwargs['x']
                    if i == 'y':
                        self.__y = kwargs['y']

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y}
