import numpy as np

def determinant(A):
  """Returns the determinant of the matrix A."""
  n = A.shape[0]
  if n == 1:
    return A[0, 0]
  elif n == 2:
    return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
  else:
    d = 0
    for i in range(n):
      c = 1 if i % 2 == 0 else -1
      d += c * A[0, i] * determinant(np.delete(A, 0, 0))
    return d

def main():
  # Define a matrix
  A = np.array([[1, 2], [3, 4]])

  # Calculate the determinant of the matrix
  d = determinant(A)

  # Print the determinant
  print(d)

if __name__ == "__main__":
  main()
