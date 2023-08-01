import numpy as np

def orthogonal_decomposition_part_2(A):
  """
  Performs the Orthogonal Decomposition Theorem Part II on the matrix A.

  Args:
    A: The matrix to be decomposed.

  Returns:
    Q: The orthogonal matrix.
    R: The upper triangular matrix.
    P: The projection matrix.
  """

  Q = np.eye(A.shape[0])
  R = np.zeros_like(A)
  P = np.zeros_like(A)

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
      P[:, j] = v / r

  return Q, R, P

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  Q, R, P = orthogonal_decomposition_part_2(A)
  print(Q)
  print(R)
  print(P)
