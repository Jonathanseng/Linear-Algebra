import numpy as np

def is_linearly_independent(vectors):
  """
  Returns True if the given vectors are linearly independent, False otherwise.

  Args:
    vectors: A list of numpy.ndarray vectors.

  Returns:
    True if the vectors are linearly independent, False otherwise.
  """

  n = len(vectors)
  matrix = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      matrix[i, j] = vectors[i].dot(vectors[j])

  # The determinant of the matrix is zero if and only if the vectors are linearly dependent.

  determinant = np.linalg.det(matrix)
  return determinant != 0

def main():
  """
  Example usage of the `is_linearly_independent` function.
  """

  vectors = np.array([[1, 2], [3, 4], [5, 6]])
  print(is_linearly_independent(vectors))

if __name__ == "__main__":
  main()
