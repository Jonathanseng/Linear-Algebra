import numpy as np

def column_space(A):
  """
  Returns the column space of the matrix A.

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
  print(column_space(A))
  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
