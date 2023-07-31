import numpy as np


def elementary_matrix(i, j, k, v):
  """
  This function creates an elementary matrix.

  Args:
    i: The row of the pivot.
    j: The column of the pivot.
    k: The value of the pivot.
    v: The value to be multiplied by the pivot.

  Returns:
    The elementary matrix.
  """

  E = np.eye(3)
  E[i, i] = v
  E[j, j] = k

  return E


def main():
  E = elementary_matrix(0, 1, 2, 3)

  print(E)


if __name__ == "__main__":
  main()
