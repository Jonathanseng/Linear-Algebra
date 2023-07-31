import numpy as np

def linear_transformation(matrix, vector):
  """
  Applies a linear transformation to a vector.

  Args:
    matrix: A 2x2 transformation matrix.
    vector: A 2-dimensional vector.

  Returns:
    A 2-dimensional vector representing the transformed vector.
  """

  product = np.dot(matrix, vector)
  return product

def main():
  """
  Example usage of the linear_transformation function.
  """

  matrix = np.array([[1, 2], [3, 4]])
  vector = np.array([1, 2])
  transformed_vector = linear_transformation(matrix, vector)
  print(transformed_vector)

if __name__ == "__main__":
  main()
