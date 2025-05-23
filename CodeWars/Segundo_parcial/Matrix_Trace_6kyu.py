"""
Calculate the trace of a square matrix. A square matrix has n rows and n columns, where n is any integer > 0. The entries of the matrix can contain any number of integers. The function should return the calculated trace of the matrix, or nil/None if the array is empty or not square; you can otherwise assume the input will be valid (of the form described below).

The trace of an n-by-n square matrix A is defined to be the sum of the elements on the main diagonal (the diagonal from the upper left to the lower right) of A.

A matrix will be defined as an array of arrays, where the 1st entry represents the 1st row, the 2nd entry the 2nd row, and so on.

For example, the following code....

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
represents the matrix

|1 2 3|
|4 5 6|
|7 8 9|
which has a trace of 1 + 5 + 9 = 15.
"""


def trace(matrix):
    # Verificar si la matriz no esta vacia o si no es escuadra
    if not matrix or any(len(fila) != len(matrix) for fila in matrix):
        return None

    # Calcular el trazo
    return sum(matrix[i][i] for i in range(len(matrix)))

if __name__ == '__main__':
    print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))