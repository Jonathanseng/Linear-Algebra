import numpy as np
import matplotlib.pyplot as plt

def visualize_diagonalization(A, eigenvectors):
  """Visualizes the diagonalization of A."""
  eigenvalues, _ = np.linalg.eig(A)
  for i in range(len(eigenvalues)):
    eigenvector = eigenvectors[:, i]
    plt.plot([0, eigenvalues[i]], [0, eigenvector[0]], 'o-')
    plt.plot([0, eigenvalues[i]], [0, eigenvector[1]], 'o-')
  plt.show()

def main():
  A = np.array([[1, 2], [2, 3]])
  eigenvectors = np.array([[1, 2], [-2, 1]])
  visualize_diagonalization(A, eigenvectors)

if __name__ == "__main__":
  main()
