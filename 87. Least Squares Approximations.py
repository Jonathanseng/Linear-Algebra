import numpy as np

def least_squares_approximation(x, y):
  """
  Performs least squares approximation on the data points (x, y).

  Args:
    x: The x-coordinates of the data points.
    y: The y-coordinates of the data points.

  Returns:
    m: The slope of the least squares line.
    b: The y-intercept of the least squares line.
  """

  n = len(x)
  S_xx = np.sum(x**2)
  S_xy = np.sum(x * y)
  S_yy = np.sum(y**2)

  m = (S_xy - S_x * S_y / n) / (S_xx - S_x**2 / n)
  b = S_y / n - m * S_x / n

  return m, b

if __name__ == "__main__":
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 4, 6, 8, 10])
  m, b = least_squares_approximation(x, y)
  print(m, b)
