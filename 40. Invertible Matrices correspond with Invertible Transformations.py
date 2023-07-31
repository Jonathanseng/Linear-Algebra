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
    np.linalg.inv(A)
    return True
  except np.linalg.LinAlgError:
    return False


def is_invertible_transformation(A):
  """
  This function checks if a matrix represents an invertible transformation.

  Args:
    A: The matrix to be checked.

  Returns:
    True if the matrix represents an invertible transformation, False otherwise.
  """

  n = len(A)

  # Check if the determinant of the matrix is non-zero.

  if np.linalg.det(A) != 0:
    return True

  # Check if the columns of the matrix are linearly independent.

  for i in range(n):
    v = A[:, i]
    if np.all(v == 0):
      return False

  return True


def main():
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[1, 0], [0, 0]])

  print(is_invertible(A))
  print(is_invertible_transformation(A))
  print(is_invertible(B))
  print(is_invertible_transformation(B))


if __name__ == "__main__":
  main()
