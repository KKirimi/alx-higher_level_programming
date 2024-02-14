s matrix_divided
Divides each element of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    Args:
    matrix(list) :  list of lists of integers or floats.
    div(int, float) : divider >= 0
    """
    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error)
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error)
    for k in range(len(matrix)):
        if len(matrix[k]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for l in matrix[k]:
            if type(l) is int or type(l) is float:
                new_matrix[k].append(round(l / div, 2))
            else:
                raise TypeError(error)
    return new_matrix
