#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    N_matrix = list(map(lambda a: list(map(lambda b : b ** 2, a)), matrix))
    return N_matrix
