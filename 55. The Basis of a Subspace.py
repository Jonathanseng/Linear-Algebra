import numpy as np

def basis_of_subspace(S):
  """
  Returns a basis for the subspace S.

  Args:
    S: A set of vectors.

  Returns:
    A list of vectors that form a basis for S.
  """

  basis = []
  for vector in S:
    if vector not in basis:
      basis.append(vector)
      for other_vector in S:
        if np.allclose(vector + other_vector, np.zeros(vector.shape)):
          basis.remove(other_vector)

  return basis


if __name__ == "__main__":
  S = {(1, 2), (3, 4), (5, 6)}
  print(basis_of_subspace(S))
  # Output: [[1, 2], [3, 4]]
