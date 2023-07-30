import numpy as np

def simplify_linear_system_elementary_row_operations(A, b):
  """
  Simplifies a linear system using elementary row operations.

  Args:
    A: The coefficient matrix.
    b: The right-hand side vector.

  Returns:
    A simplified version of the linear system.
  """

  n = len(A)
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

  return A, b

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [3, 4, 5], [-1, -2, -3]])
  b = np.array([1, 2, 3])
  A, b = simplify_linear_system_elementary_row_operations(A, b)
  print(A)
  print(b)
