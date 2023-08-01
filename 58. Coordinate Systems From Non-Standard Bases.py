import numpy as np

def change_of_basis(A, B):
  """
  Returns the change of basis matrix from the basis B to the basis A.

  Args:
    A: A numpy matrix that represents the basis A.
    B: A numpy matrix that represents the basis B.

  Returns:
    A numpy matrix that represents the change of basis from B to A.
  """

  change_of_basis = np.linalg.inv(B) @ A

  return change_of_basis


if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
  print(change_of_basis(A, B))
  # Output: [[1, 0, 0], [2, 1, 0], [3, 2, 1]]
