import numpy as np
import matplotlib.pyplot as plt

def visualize_linear_dependence(vectors):
  """Visualizes the linear dependence of a set of vectors."""
  n = vectors.shape[0]
  for i in range(n):
    x = np.linspace(-1, 1, n)
    y = vectors[i] * x + vectors[i, 0]
    plt.plot(x, y)

def main():
  # Define a set of vectors
  vectors = np.array([[1, 0], [2, 0], [3, 0]])

  # Visualize the linear dependence of the vectors
  visualize_linear_dependence(vectors)

  # Check if the vectors are linearly dependent
  print(np.linalg.matrix_rank(vectors))

if __name__ == "__main__":
  main()
