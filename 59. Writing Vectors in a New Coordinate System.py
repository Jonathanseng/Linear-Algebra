import numpy as np

def write_vector_in_new_coordinate_system(vector, basis):
  """
  Converts a vector from one coordinate system to another.

  Args:
    vector: A numpy vector.
    basis: A numpy matrix that represents the new coordinate system.

  Returns:
    A numpy vector that represents the vector in the new coordinate system.
  """

  new_vector = basis @ vector

  return new_vector


if __name__ == "__main__":
  vector = np.array([1, 2, 3])
  basis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
  print(write_vector_in_new_coordinate_system(vector, basis))
  # Output: [1, 2, 3]
