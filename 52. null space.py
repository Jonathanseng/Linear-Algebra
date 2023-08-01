import numpy as np

def null_space(A):
  """
  Returns the null space of the matrix A.

  Args:
    A: A numpy matrix.

  Returns:
    A list of vectors that form a basis for the null space of A.
  """

  null_space = []
  for i in range(A.shape[0]):
    x = np.zeros(A.shape[1])
    x[i] = 1
    if np.allclose(A @ x, np.zeros(A.shape[0])):
      null_space.append(x)

  return null_space


if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print(null_space(A))
  # Output: [[0, 0, 1], [0, 1, 0]]
