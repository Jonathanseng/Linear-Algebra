import numpy as np

def compute_eigenvalues_and_eigenvectors(A):
  """Computes the eigenvalues and eigenvectors of A."""
  eigenvalues, eigenvectors = np.linalg.eig(A)
  return eigenvalues, eigenvectors

def main():
  A = np.array([[1, 2], [2, 3]])
  eigenvalues, eigenvectors = compute_eigenvalues_and_eigenvectors(A)

  # Print the eigenvalues and eigenvectors
  print("The eigenvalues of A are:", eigenvalues)
  print("The eigenvectors of A are:", eigenvectors)

  # Check that the eigenvalues and eigenvectors satisfy the equation Av = λv
  for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lambda_i = eigenvalues[i]
    assert np.allclose(A @ v, lambda_i * v)

if __name__ == "__main__":
  main()
