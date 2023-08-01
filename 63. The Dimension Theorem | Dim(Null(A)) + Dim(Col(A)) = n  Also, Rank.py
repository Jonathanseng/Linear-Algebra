import numpy as np

def null_space(A):
  """Computes the dimension of the null space of A."""
  rank = np.linalg.matrix_rank(A)
  null_space_dim = A.shape[0] - rank
  return null_space_dim

def column_space(A):
  """Computes the dimension of the column space of A."""
  column_space_dim = np.linalg.matrix_rank(A)
  return column_space_dim

def dimension_theorem(A):
  """Computes the dimension of the null space and column space of A."""
  null_space_dim = null_space(A)
  column_space_dim = column_space(A)
  return null_space_dim + column_space_dim

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  print("The dimension of the null space of A is:", null_space(A))
  print("The dimension of the column space of A is:", column_space(A))
  print("The dimension of the null space and column space of A is:", dimension_theorem(A))
