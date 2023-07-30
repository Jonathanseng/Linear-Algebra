import numpy as np
import matplotlib.pyplot as plt

def visualize_solutions(A, b):
  """Visualizes the solutions to Ax=b."""
  n = A.shape[0]
  x = np.linspace(-1, 1, n)
  y = np.zeros(n)
  for i in range(n):
    Ai = np.delete(A, i, 0)
    bi = np.delete(b, i, 0)
    y[i] = determinant(Ai) / determinant(A)
  plt.plot(x, y)
  plt.show()

def main():
  # Define a matrix and a vector
  A = np.array([[1, 2], [3, 4]])
  b = np.array([1, 2])

  # Visualize the solutions to Ax=b
  visualize_solutions(A, b)

if __name__ == "__main__":
  main()
