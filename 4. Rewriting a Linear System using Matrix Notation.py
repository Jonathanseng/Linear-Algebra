import numpy as np

def rewrite_linear_system(A, b):
  """
  Rewrites a linear system using matrix notation.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    A string representing the linear system in matrix notation.
  """

  string = "A * x = b"
  string = string.replace("A", str(A))
  string = string.replace("b", str(b))
  return string

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  print(rewrite_linear_system(A, b))
