import numpy as np


def is_invertible(A):
  """
  This function checks if a matrix is invertible.

  Args:
    A: The matrix to be checked.

  Returns:
    True if the matrix is invertible, False otherwise.
  """

  try:
    np.linalg.det(A)
    return True
  except np.linalg.LinAlgError:
    return False


def main():
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[1, 0], [0, 0]])

  print(is_invertible(A))
  print(is_invertible(B))


if __name__ == "__main__":
  main()
