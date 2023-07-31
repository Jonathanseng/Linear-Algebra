import matplotlib.pyplot as plt
import numpy as np


def visualize_transformation(A, x):
  """
  This function visualizes the transformation of a point by a matrix.

  Args:
    A: The matrix that represents the transformation.
    x: The point to be transformed.

  Returns:
    A plot of the original point, the transformed point, and the line connecting the two points.
  """

  transformed_x = A @ x

  plt.plot([x[0], transformed_x[0]], [x[1], transformed_x[1]], 'o-')
  plt.plot([x[0], transformed_x[0]], [x[1], transformed_x[1]], 'k')

  plt.show()


def main():
  A = np.array([[1, 2], [3, 4]])
  x = np.array([1, 2])

  visualize_transformation(A, x)


if __name__ == "__main__":
  main()
