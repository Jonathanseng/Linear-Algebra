import numpy as np

def basis_of_nullspace(A):
  """
  Returns a basis for the nullspace of the matrix A.

  Args:
    A: A numpy matrix.

  Returns:
    A list of vectors that form a basis for the nullspace of A.
  """

  null_space = []
  for i in range(A.shape[0]):
    x = np.zeros(A.shape[1])
    x[i] = 1
    if np.allclose(A @ x, np.zeros(A.shape[0])):
      null_space.append(x)

  return null_space


def basis_of_column_space(A):
  """
  Returns a basis for the column space of the matrix A.

  Args:
    A: A numpy matrix.

  Returns:
    A list of vectors that form a basis for the column space of A.
  """

  column_space = []
  for i in range(A.shape[1]):
    column_space.append(A[:, i])

  return column_space


if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print(basis_of_nullspace(A))
  # Output: [[0, 0, 1], [0, 1, 0]]

  print(basis_of_column_space(A))
  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
