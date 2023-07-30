import numpy as np
import matplotlib.pyplot as plt

def visualize_solutions(A, b):
  """
  Visualizes the solutions to the linear system Ax = b.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    A plot of the solutions.
  """

  x = np.linalg.solve(A, b)
  plt.plot(x[0], x[1], 'o')
  plt.show()

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  visualize_solutions(A, b)
