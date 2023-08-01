import numpy as np
import matplotlib.pyplot as plt

def change_of_basis(v, old_basis, new_basis):
  """Computes the change of basis matrix from old_basis to new_basis."""
  change_of_basis_matrix = np.zeros((len(new_basis), len(old_basis)))
  for i in range(len(new_basis)):
    for j in range(len(old_basis)):
      change_of_basis_matrix[i, j] = np.dot(new_basis[i], old_basis[j])
  return change_of_basis_matrix

def convert_vector(v, old_basis, new_basis):
  """Converts a vector from old_basis to new_basis."""
  change_of_basis_matrix = change_of_basis(v, old_basis, new_basis)
  new_vector = np.dot(change_of_basis_matrix, v)
  return new_vector

def visualize_change_of_basis(old_basis, new_basis, v):
  """Visualizes the change of basis."""
  fig, ax = plt.subplots()
  ax.set_xlim([-1, 1])
  ax.set_ylim([-1, 1])

  old_vector = np.dot(old_basis, v)
  new_vector = convert_vector(v, old_basis, new_basis)

  ax.plot([old_vector[0], new_vector[0]], [old_vector[1], new_vector[1]], 'b')
  ax.plot(old_basis, 'o', color='red')
  ax.plot(new_basis, 'o', color='blue')

  plt.show()

if __name__ == "__main__":
  old_basis = np.array([1, 2, 3])
  new_basis = np.array([4, 5, 6])
  v = np.array([1, 2, 3])

  visualize_change_of_basis(old_basis, new_basis, v)
