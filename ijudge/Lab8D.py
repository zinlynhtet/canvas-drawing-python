"""
Module to perform matrix operations: addition, multiplication, and transpose.
Reads two matrices from input and computes (Matrix1^T) * (Matrix1 + Matrix2).
"""

class Matrix:
    """
    Class representing a matrix of integers.
    Supports element access, transposition, addition, and multiplication.
    """

    def __init__(self, m, n):
        """
        Initialize an m x n matrix with all elements set to 0.
        """
        self.row_count = m
        self.col_count = n
        self.data = [[0 for _ in range(n)] for _ in range(m)]

    def set(self, i, j, x):
        """Set the element at row i and column j to x."""
        self.data[i][j] = x

    def get(self, i, j):
        """Return the element at row i and column j."""
        return self.data[i][j]

    def transpose(self):
        """Return a new Matrix that is the transpose of this matrix."""
        result = Matrix(self.col_count, self.row_count)
        for i in range(self.row_count):
            for j in range(self.col_count):
                result.set(j, i, self.get(i, j))
        return result

    def __add__(self, other):
        """Return the sum of this matrix and another matrix, or None if dimensions mismatch."""
        if self.row_count != other.row_count or self.col_count != other.col_count:
            return None
        result = Matrix(self.row_count, self.col_count)
        for i in range(self.row_count):
            for j in range(self.col_count):
                result.set(i, j, self.get(i, j) + other.get(i, j))
        return result

    def __mul__(self, other):
        """Return the product of this matrix and another matrix, or None if dimensions mismatch."""
        if self.col_count != other.row_count:
            return None
        result = Matrix(self.row_count, other.col_count)
        for i in range(self.row_count):
            for j in range(other.col_count):
                total = 0
                for k in range(self.col_count):
                    total += self.get(i, k) * other.get(k, j)
                result.set(i, j, total)
        return result


def read_matrix(m, n):
    """Read a matrix of size m x n from input."""
    mat = Matrix(m, n)
    for i in range(m):
        row = list(map(int, input().split()))
        for j in range(n):
            mat.set(i, j, row[j])
    return mat


def print_matrix(mat):
    """Print the matrix in row-major order, elements separated by space."""
    for i in range(mat.row_count):
        for j in range(mat.col_count):
            print(mat.get(i, j), end=' ' if j != mat.col_count - 1 else '')
        print()


# Read input matrices
mat1 = read_matrix(int(input()), int(input()))
mat2 = read_matrix(int(input()), int(input()))

# Compute (Matrix1^T) * (Matrix1 + Matrix2)
result = mat1.transpose() * (mat1 + mat2)

# Print the resulting matrix
print_matrix(result)
