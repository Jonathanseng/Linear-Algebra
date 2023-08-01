import numpy as np
import matplotlib.pyplot as plt

def visualize_eigenvalues_and_eigenvectors(A, v):
  """Visualizes the eigenvalues and eigenvectors of A."""
  fig, ax = plt.subplots()
  ax.set_xlim([-1, 1])
  ax.set_ylim([-1, 1])

  eigenvalues, eigenvectors = np.linalg.eig(A)
  for i in range(len(eigenvalues)):
    eigenvector = eigenvectors[:, i]
    ax.plot([0, eigenvector[0]], [0, eigenvector[1]], 'o-', label='eigenvector {}'.format(i))
    ax.plot(eigenvector[0] * eigenvalues[i], eigenvector[1] * eigenvalues[i], 'o', label='eigenvalue {}'.format(i))

  ax.legend()

if __name__ == "__main__":
  A = np.array([[1, 2], [2, 3]])
  v = np.array([1, 1])
  visualize_eigenvalues_and_eigenvectors(A, v)
