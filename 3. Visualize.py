import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_solutions(A, b):
  """
  Visualizes the solutions to the linear system Ax = b.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    A 3D plot of the solutions.
  """

  x = np.linalg.solve(A, b)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot(x[0], x[1], x[2], 'o')
  plt.show()

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  b = np.array([10, 11, 12])
  visualize_solutions(A, b)
