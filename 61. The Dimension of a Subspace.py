def dimension_of_subspace(S):
  """
  Returns the dimension of the subspace S.

  Args:
    S: A set of vectors.

  Returns:
    The dimension of the subspace S.
  """

  basis = []
  for vector in S:
    if vector not in basis:
      basis.append(vector)
      for other_vector in S:
        if np.allclose(vector + other_vector, np.zeros(vector.shape)):
          basis.remove(other_vector)

  return len(basis)


if __name__ == "__main__":
  S = {(1, 2), (3, 4), (5, 6)}
  print(dimension_of_subspace(S))
  # Output: 2
