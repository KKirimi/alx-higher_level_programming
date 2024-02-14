#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n=4500):
    """print pascal"""
    pascal = [[0]*k for k in range(1, n+1)]
    cmpt = 0
    for k in range(n):
        pascal[k][0] = 1
        pascal[k][-1] = 1
        for j in range(0, k//2):
            pascal[k][j+1] = pascal[k-1][j] + pascal[k-1][j+1]
            pascal[k][k-j-1] = pascal[k-1][j] + pascal[k-1][j+1]

    return pascal
