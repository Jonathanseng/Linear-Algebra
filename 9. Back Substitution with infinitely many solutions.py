import numpy as np

def back_substitution(U, b):
  """Solve a system of linear equations Ux = b for x."""
  n = U.shape[0]
  x = np.zeros(n)
  x[-1] = b[-1] / U[-1, -1]
  for i in range(n - 2, -1, -1):
    x[i] = (b[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
  return x

def main():
  # Example matrix
  U = np.array([[1, 0, 0], [1, 1, 0], [1, 2, 1]])
  b = np.array([1, 2, 3])

  # Print the solution
  print(back_substitution(U, b))

if __name__ == "__main__":
  main()
