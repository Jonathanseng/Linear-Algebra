import numpy as np

def find_matrix_of_linear_transformation(transformation, vectors):
  """
  Finds the matrix of the linear transformation.

  Args:
    transformation: A function that takes a vector and returns a transformed vector.
    vectors: A list of vectors.

  Returns:
    A matrix that represents the linear transformation.
  """

  n = len(vectors)
  matrix = np.zeros((n, n))
  for i in range(n):
    transformed_vector = transformation(vectors[i])
    for j in range(n):
      matrix[i, j] = transformed_vector[j]
  return matrix

def main():
  """
  Example usage of the find_matrix_of_linear_transformation function.
  """

  transformation = lambda vector: vector * 2
  vectors = np.array([[1, 2], [3, 4], [5, 6]])
  matrix = find_matrix_of_linear_transformation(transformation, vectors)
  print(matrix)

if __name__ == "__main__":
  main()
