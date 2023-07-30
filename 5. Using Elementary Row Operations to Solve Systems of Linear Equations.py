import numpy as np

def solve_linear_system_elementary_row_operations(A, b):
  """
  Solves a system of linear equations using elementary row operations.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    The solution vector x.
  """

  n = len(A)
  x = np.zeros(n)

  for i in range(n):
    pivot = A[i, i]
    if pivot != 0:
      # Scale the row so that the pivot is equal to 1.
      A[i] /= pivot
      b[i] /= pivot

      # Add multiples of the row to other rows to eliminate the leading terms.
      for j in range(i + 1, n):
        if A[j, i] != 0:
          scale = A[j, i] / pivot
          A[j] -= scale * A[i]
          b[j] -= scale * b[i]

  return x

if __name__ == "__main__":
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  x = solve_linear_system_elementary_row_operations(A, b)
  print(x)
