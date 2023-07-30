import numpy as np

def is_homogeneous(A):
  """Returns True if the system Ax=0 is homogeneous, False otherwise."""
  n = A.shape[0]
  for i in range(n):
    if np.sum(A[i, :]) != 0:
      return False
  return True

def find_one_solution(A):
  """Returns one solution to the system Ax=0."""
  n = A.shape[0]
  x = np.ones(n)
  for i in range(n):
    x[i] = 0
  return x

def main():
  # Define a matrix
  A = np.array([[1, 2], [3, 4]])

  # Check if the system Ax=0 is homogeneous
  print(is_homogeneous(A))

  # Find one solution to the system Ax=0
  x = find_one_solution(A)
  print(x)

if __name__ == "__main__":
  main()
