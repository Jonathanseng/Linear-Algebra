def matrix_multiplication(A, B):
  """
  This function multiplies two matrices A and B.

  Args:
    A: The first matrix.
    B: The second matrix.

  Returns:
    The product of A and B.
  """

  n = len(A)
  m = len(A[0])
  p = len(B[0])

  C = [[0 for i in range(p)] for j in range(n)]

  for i in range(n):
    for j in range(p):
      for k in range(m):
        C[i][j] += A[i][k] * B[k][j]

  return C


def main():
  A = [[1, 2], [3, 4]]
  B = [[5, 6], [7, 8]]

  C = matrix_multiplication(A, B)

  print(C)


if __name__ == "__main__":
  main()
