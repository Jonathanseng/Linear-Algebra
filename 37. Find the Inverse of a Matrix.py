import numpy as np


def inverse_matrix(A):
  """
  This function finds the inverse of a matrix.

  Args:
    A: The matrix to be inverted.

  Returns:
    The inverse of the matrix.
  """

  try:
    return np.linalg.inv(A)
  except np.linalg.LinAlgError:
    return None


def main():
  A = [[1, 2], [3, 4]]
  B = inverse_matrix(A)

  print(B)


if __name__ == "__main__":
  main()
