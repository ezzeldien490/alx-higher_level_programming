#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for c in i:
            print("{:d}".format(c), end=" " if c != i[-1] else "")
        print()
