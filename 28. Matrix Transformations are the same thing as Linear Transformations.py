import numpy as np

def linear_transformation(vector):
  """
  A linear transformation that adds 1 to each component of a vector.

  Args:
    vector: A vector.

  Returns:
    A vector with 1 added to each component.
  """

  new_vector = vector + np.ones(len(vector))
  return new_vector

def matrix_transformation(vector):
  """
  A matrix transformation that multiplies a vector by the matrix [[2, 0], [0, 2]].

  Args:
    vector: A vector.

  Returns:
    A vector that has been multiplied by the matrix [[2, 0], [0, 2]].
  """

  matrix = np.array([[2, 0], [0, 2]])
  new_vector = np.dot(matrix, vector)
  return new_vector

def main():
  """
  Example usage of the linear_transformation and matrix_transformation functions.
  """

  vector = np.array([1, 2])
  print(linear_transformation(vector))
  print(matrix_transformation(vector))

if __name__ == "__main__":
  main()
