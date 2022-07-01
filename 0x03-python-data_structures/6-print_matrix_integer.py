#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    total = len(matrix)
    for i in range(total):
        for j in range(total):
            print("{}".format(matrix[i][j]))
        print()
