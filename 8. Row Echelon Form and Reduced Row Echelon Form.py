import numpy as np

def rref(A):
  """Returns the reduced row echelon form of A."""
  n = A.shape[0]
  for i in range(n):
    # Find the pivot element in row i.
    pivot = i
    for j in range(i + 1, n):
      if abs(A[j, i]) > abs(A[pivot, i]):
        pivot = j

    # Swap rows i and pivot.
    A[[i, pivot]] = A[[pivot, i]]

    # Make all elements below the pivot equal to 0.
    for j in range(i + 1, n):
      if A[j, i] != 0:
        A[j] = A[j] - A[i] * A[j, i] / A[i, i]

  return A

def main():
  # Example matrix
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  # Print the original matrix
  print(A)

  # Print the reduced row echelon form of A
  print(rref(A))

if __name__ == "__main__":
  main()
