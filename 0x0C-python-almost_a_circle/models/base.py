#!/usr/bin/python3
"""
base class
"""
import json
import os.path


class Base:
    """A class named Base
    Attributes:
    attr1(__nb_objects): number of objects
    attr2(id): object id
    """
    __nb_object = 0

    def __init__(self, id=None):
        """Initiliazes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        l = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
                file.write(Base.to_json_string(l))
            return l
        for model in list_objs:
            list_dictionaries.append(model.to_dictionary())
        with open(cls.__name__ + ".json", "w",  encoding='utf-8') as file:
            file.write(Base.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        L = []
        if json_string is None or json_string == "":
            return L
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create a dummy
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances from a file
        """
        filename = cls.__name__ + ".jason"
        L = []
        if os.path.isfile(filename) is False:
            return L
        else:
            with open(filename, encoding="UTF8") as Myfile:
                rd = Myfile.read()
                t = cls.from_json_string(rd)
                for i in t:
                    L.append(cls.create(**i))
                return L
