import numpy as np

def is_linear_combination(vectors, target):
  """
  Returns True if the target vector is a linear combination of the vectors, False otherwise.

  Args:
    vectors: A list of vectors.
    target: The target vector.

  Returns:
    True if the target vector is a linear combination of the vectors, False otherwise.
  """

  n = len(vectors)
  matrix = np.zeros((n, n))
  for i in range(n):
    for j in range(n):
      matrix[i, j] = vectors[i].dot(vectors[j])

  # The determinant of the matrix is zero if and only if the vectors are linearly dependent.

  determinant = np.linalg.det(matrix)
  if determinant != 0:
    return False

  # Otherwise, the vectors are linearly independent, so the target vector is a linear combination of the vectors.

  coefficients = np.linalg.lstsq(matrix, target)[0]
  for i in range(n):
    if coefficients[i] != 0:
      return True
  return False

def main():
  """
  Example usage of the is_linear_combination function.
  """

  vectors = np.array([[1, 2], [3, 4], [5, 6]])
  target = np.array([10, 12])
  print(is_linear_combination(vectors, target))

if __name__ == "__main__":
  main()
