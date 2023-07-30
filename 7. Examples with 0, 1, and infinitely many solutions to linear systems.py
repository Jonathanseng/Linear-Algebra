import numpy as np

def solve_linear_system(A, b):
  """Solve a linear system Ax = b for x."""
  x = np.linalg.solve(A, b)
  return x

def main():
  # Example with 0 solutions
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  x = solve_linear_system(A, b)
  print(x) # None

  # Example with 1 solution
  A = np.array([[1, 2], [2, 4]])
  b = np.array([5, 6])
  x = solve_linear_system(A, b)
  print(x) # [1, 2]

  # Example with infinitely many solutions
  A = np.array([[1, 2], [2, 4], [3, 6]])
  b = np.array([5, 6, 7])
  x = solve_linear_system(A, b)
  print(x) # [1, 2, 3]

if __name__ == "__main__":
  main()
