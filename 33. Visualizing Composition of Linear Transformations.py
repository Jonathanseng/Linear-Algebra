import matplotlib.pyplot as plt
import numpy as np


def visualize_composition(A, B):
  """
  This function visualizes the composition of two linear transformations.

  Args:
    A: The first linear transformation.
    B: The second linear transformation.

  Returns:
    A plot of the composition of the two transformations.
  """

  n = 100
  x = np.linspace(-1, 1, n)
  y = np.linspace(-1, 1, n)

  # Create a grid of points.
  points = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)

  # Apply the first transformation to the points.
  transformed_points = A @ points

  # Apply the second transformation to the transformed points.
  composed_points = B @ transformed_points

  # Plot the original points, the transformed points, and the composed points.
  plt.plot(points[:, 0], points[:, 1], 'o', color='black')
  plt.plot(transformed_points[:, 0], transformed_points[:, 1], 'o', color='red')
  plt.plot(composed_points[:, 0], composed_points[:, 1], 'o', color='green')

  plt.show()


if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  B = np.array([[5, 6], [7, 8]])

  visualize_composition(A, B)
