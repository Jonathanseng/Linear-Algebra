import numpy as np

def compute_power_of_matrix_via_diagonalization(A, n):
  """Computes the power of the matrix A via diagonalization."""
  eigenvalues, eigenvectors = np.linalg.eig(A)
  diagonal_matrix = np.zeros_like(A)
  for i in range(len(eigenvalues)):
    diagonal_matrix[i, i] = eigenvalues[i] ** n
  diagonalized_matrix = np.dot(eigenvectors, np.diag(diagonal_matrix))
  return np.dot(diagonalized_matrix, np.linalg.inv(eigenvectors))

def main():
  A = np.array([[1, 2], [2, 3]])
  n = 3
  computed_matrix = compute_power_of_matrix_via_diagonalization(A, n)
  print(computed_matrix)

if __name__ == "__main__":
  main()
