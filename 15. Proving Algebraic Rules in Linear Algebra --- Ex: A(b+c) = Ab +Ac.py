import numpy as np

def matrix_vector_addition(v1, v2):
  """Returns the sum of the vectors v1 and v2."""
  n = v1.shape[0]
  y = np.zeros(n)
  for i in range(n):
    y[i] = v1[i] + v2[i]
  return y

def matrix_vector_multiplication(A, x):
  """Returns the product of the matrix A and the vector x."""
  n, m = A.shape
  y = np.zeros(n)
  for i in range(n):
    for j in range(m):
      y[i] += A[i, j] * x[j]
  return y

def main():
  # Define a matrix and two vectors
  A = np.array([[1, 2], [3, 4]])
  b = np.array([1, 2])
  c = np.array([3, 4])

  # Calculate A(b+c)
  y = matrix_vector_multiplication(A, matrix_vector_addition(b, c))

  # Calculate Ab + Ac
  z = matrix_vector_multiplication(A, b) + matrix_vector_multiplication(A, c)

  # Check if y == z
  print(np.allclose(y, z))

if __name__ == "__main__":
  main()
