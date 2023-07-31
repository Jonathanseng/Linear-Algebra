import numpy as np


def determinant(A, row=0, column=0):
  """
  This function computes the determinant of a matrix along a given row or column.

  Args:
    A: The matrix whose determinant is to be computed.
    row: The row along which the determinant is to be computed.
    column: The column along which the determinant is to be computed.

  Returns:
    The determinant of the matrix along the given row or column.
  """

  n = len(A)

  # Check if the row or column is out of bounds.

  if row < 0 or row >= n:
    raise IndexError("Row index out of bounds")
  if column < 0 or column >= n:
    raise IndexError("Column index out of bounds")

  # Compute the determinant along the given row or column.

  determinant = 0
  for i in range(n):
    v = A[i]
    if i != row:
      determinant += v[column] * determinant(A, row, i)

  return determinant


def main():
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  print(determinant(A, 0))
  print(determinant(A, 1))


if __name__ == "__main__":
  main()
