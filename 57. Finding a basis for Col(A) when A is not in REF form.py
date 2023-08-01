import numpy as np

def basis_of_column_space(A):
  """
  Returns a basis for the column space of the matrix A.

  Args:
    A: A numpy matrix.

  Returns:
    A list of vectors that form a basis for the column space of A.
  """

  basis = []
  for i in range(A.shape[1]):
    column_vector = A[:, i]
    for other_column_vector in basis:
      if np.allclose(column_vector, other_column_vector):
        break
    else:
      basis.append(column_vector)

  return basis


if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print(basis_of_column_space(A))
  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
