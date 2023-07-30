import numpy as np

def cramer_rule(A, b):
  """Returns the solutions to Ax=b in vector form."""
  n = A.shape[0]
  x = np.zeros(n)
  for i in range(n):
    Ai = np.delete(A, i, 0)
    bi = np.delete(b, i, 0)
    x[i] = determinant(Ai) / determinant(A)
  return x

def main():
  # Define a matrix and a vector
  A = np.array([[1, 2], [3, 4]])
  b = np.array([1, 2])

  # Calculate the solutions to Ax=b
  x = cramer_rule(A, b)

  # Print the solutions
  print(x)

if __name__ == "__main__":
  main()
