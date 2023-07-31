def is_invertible(A):
  """
  This function checks if a matrix is invertible.

  Args:
    A: The matrix to be checked.

  Returns:
    True if the matrix is invertible, False otherwise.
  """

  try:
    np.linalg.inv(A)
    return True
  except np.linalg.LinAlgError:
    return False


def main():
  A = [[1, 2], [3, 4]]
  B = [[1, 0], [0, 0]]

  print(is_invertible(A))
  print(is_invertible(B))


if __name__ == "__main__":
  main()
