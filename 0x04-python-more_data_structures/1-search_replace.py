#!/usr/bin/python3
def search_replace(my_list, search, replace):
    N = []
    for i in my_list:
        if i == search:
            N.append(replace)
        else:
            N.append(i)
    return (N)
