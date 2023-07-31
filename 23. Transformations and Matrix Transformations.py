import numpy as np

def translation(x, y):
  """
  Returns a transformation matrix that translates by (x, y).

  Args:
    x: The x-translation.
    y: The y-translation.

  Returns:
    A 2x2 transformation matrix.
  """

  matrix = np.zeros((2, 2))
  matrix[0, 0] = 1
  matrix[1, 1] = 1
  matrix[0, 1] = x
  matrix[1, 0] = y
  return matrix

def scaling(x, y):
  """
  Returns a transformation matrix that scales by (x, y).

  Args:
    x: The x-scale.
    y: The y-scale.

  Returns:
    A 2x2 transformation matrix.
  """

  matrix = np.zeros((2, 2))
  matrix[0, 0] = x
  matrix[1, 1] = y
  return matrix

def rotation(angle):
  """
  Returns a transformation matrix that rotates by the given angle.

  Args:
    angle: The angle of rotation in degrees.

  Returns:
    A 2x2 transformation matrix.
  """

  angle = angle * np.pi / 180
  c = np.cos(angle)
  s = np.sin(angle)
  matrix = np.zeros((2, 2))
  matrix[0, 0] = c
  matrix[0, 1] = -s
  matrix[1, 0] = s
  matrix[1, 1] = c
  return matrix

def main():
  """
  Example usage of the transformation functions.
  """

  matrix = translation(2, 3)
  print(matrix)

  matrix = scaling(2, 3)
  print(matrix)

  matrix = rotation(45)
  print(matrix)

if __name__ == "__main__":
  main()
