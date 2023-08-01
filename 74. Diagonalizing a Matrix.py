import numpy as np

def diagonalize_matrix(A):
  """Diagonalizes the matrix A."""
  eigenvalues, eigenvectors = np.linalg.eig(A)
  diagonal_matrix = np.zeros_like(A)
  for i in range(len(eigenvalues)):
    diagonal_matrix[i, i] = eigenvalues[i]
  return diagonal_matrix, eigenvectors

def main():
  A = np.array([[1, 2], [2, 3]])
  diagonal_matrix, eigenvectors = diagonalize_matrix(A)
  print(diagonal_matrix)
  print(eigenvectors)

if __name__ == "__main__":
  main()
