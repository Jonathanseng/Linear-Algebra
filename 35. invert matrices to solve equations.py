import numpy as np


def invert_matrix(A):
  """
  This function inverts a matrix.

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
  A = np.array([[1, 2], [3, 4]])
  B = invert_matrix(A)

  print(B)


if __name__ == "__main__":
  main()
