#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    N = {}
    N.update(a_dictionary)
    for i in N:
        N[i] = N[i] * 2 
    return N
