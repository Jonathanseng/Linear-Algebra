import numpy as np

def orthogonal_decomposition(A):
  """
  Performs the Orthogonal Decomposition Theorem on the matrix A.

  Args:
    A: The matrix to be decomposed.

  Returns:
    Q: The orthogonal matrix.
    R: The upper triangular matrix.
  """

  Q = np.eye(A.shape[0])
  R = np.zeros_like(A)

  for i in range(A.shape[0]):
    v = A[:, i]
    r = np.linalg.norm(v)
    R[i, i] = r
    Q[:, i] = v / r

    for j in range(i + 1, A.shape[0]):
      R[i, j] = np.dot(Q[:, i], A[:, j])
      v = A[:, j] - R[i, j] * Q[:, i]
      r = np.linalg.norm(v)
      R[j, j] = r
      Q[:, j] = v / r

  return Q, R

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  Q, R = orthogonal_decomposition(A)
  print(Q)
  print(R)
