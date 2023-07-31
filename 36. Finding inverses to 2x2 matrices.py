def inverse_2x2(A):
  """
  This function finds the inverse of a 2x2 matrix.

  Args:
    A: The 2x2 matrix to be inverted.

  Returns:
    The inverse of the matrix.
  """

  det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
  if det == 0:
    return None

  inv = [[A[1][1] / det, -A[0][1] / det],
          [-A[1][0] / det, A[0][0] / det]]
  return inv


def main():
  A = [[1, 2], [3, 4]]
  B = inverse_2x2(A)

  print(B)


if __name__ == "__main__":
  main()
