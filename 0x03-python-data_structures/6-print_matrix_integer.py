#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for k in range(len(matrix)):
            for l in range(len(matrix[k])):
                if l != len(matrix[k]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[k][l]), end=endspace)
            print()
