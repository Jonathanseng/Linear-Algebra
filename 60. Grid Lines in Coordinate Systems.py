import numpy as np
import matplotlib.pyplot as plt

def plot_grid_lines(xmin, xmax, ymin, ymax, nx, ny):
  """
  Plots grid lines in a coordinate system.

  Args:
    xmin: The minimum x-coordinate.
    xmax: The maximum x-coordinate.
    ymin: The minimum y-coordinate.
    ymax: The maximum y-coordinate.
    nx: The number of grid lines in the x-direction.
    ny: The number of grid lines in the y-direction.
  """

  x_values = np.linspace(xmin, xmax, nx)
  y_values = np.linspace(ymin, ymax, ny)

  for x in x_values:
    plt.plot([x, x], [ymin, ymax], 'k', linewidth=1)

  for y in y_values:
    plt.plot([xmin, xmax], [y, y], 'k', linewidth=1)


if __name__ == "__main__":
  xmin = -1
  xmax = 1
  ymin = -1
  ymax = 1
  nx = 10
  ny = 10

  plot_grid_lines(xmin, xmax, ymin, ymax, nx, ny)

  plt.show()
