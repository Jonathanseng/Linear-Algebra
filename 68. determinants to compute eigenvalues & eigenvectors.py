import numpy as np

def compute_eigenvalues_and_eigenvectors(A):
  """Computes the eigenvalues and eigenvectors of A."""
  eigenvalues = []
  eigenvectors = []
  for i in range(A.shape[0]):
    eigenvector = np.zeros(A.shape[0])
    eigenvector[i] = 1
    submatrix = A - np.outer(eigenvector, eigenvector)
    eigenvalue = np.linalg.det(submatrix)
    eigenvalues.append(eigenvalue)
    eigenvectors.append(eigenvector)
  return eigenvalues, eigenvectors

if __name__ == "__main__":
  A = np.array([[1, 2], [2, 3]])
  eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(A)
  print("The eigenvalues of A are:", eigenvalues)
  print("The eigenvectors of A are:", eigenvectors)
