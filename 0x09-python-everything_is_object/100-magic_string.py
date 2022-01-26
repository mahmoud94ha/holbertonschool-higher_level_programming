#!/usr/bin/python3
def magic_string():
    magic_string.c = 0 if not hasattr(magic_string, "c") else magic_string.c+1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
