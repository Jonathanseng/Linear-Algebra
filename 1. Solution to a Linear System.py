import numpy as np

def solve_linear_system(A, b):
  """
  Solves the linear system Ax = b.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    The solution vector x.
  """

  x = np.linalg.solve(A, b)
  return x

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  x = solve_linear_system(A, b)
  print(x)
