#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

def print_matrix_integer(matrix=[[]]):
    for elm in matrix:
        print(" ".join("{:d}".format(i) for i in elm))
