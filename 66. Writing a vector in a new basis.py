import numpy as np

def write_vector_in_new_basis(v, old_basis, new_basis):
  """Writes a vector in a new basis."""
  change_of_basis_matrix = np.zeros((len(new_basis), len(old_basis)))
  for i in range(len(new_basis)):
    for j in range(len(old_basis)):
      change_of_basis_matrix[i, j] = np.dot(new_basis[i], old_basis[j])
  new_vector = np.dot(change_of_basis_matrix, v)
  return new_vector

if __name__ == "__main__":
  old_basis = np.array([1, 2, 3])
  new_basis = np.array([4, 5, 6])
  v = np.array([1, 2, 3])
  new_vector = write_vector_in_new_basis(v, old_basis, new_basis)
  print("The new vector is:", new_vector)
