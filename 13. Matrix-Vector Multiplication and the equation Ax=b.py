import numpy as np

def matrix_vector_multiplication(A, x):
  """Returns the product of the matrix A and the vector x."""
  n, m = A.shape
  y = np.zeros(n)
  for i in range(n):
    for j in range(m):
      y[i] += A[i, j] * x[j]
  return y

def main():
  # Define a matrix and a vector
  A = np.array([[1, 2], [3, 4]])
  x = np.array([1, 2])

  # Calculate the product of the matrix and the vector
  y = matrix_vector_multiplication(A, x)

  # Print the product
  print(y)

if __name__ == "__main__":
  main()
