import numpy as np

def gram_schmidt(A):
  """
  Performs the Gram-Schmidt process on the matrix A.

  Args:
    A: The matrix to be orthogonalized.

  Returns:
    Q: The orthogonal matrix.
  """

  Q = np.eye(A.shape[0])

  for i in range(A.shape[1]):
    v = A[:, i]
    r = np.linalg.norm(v)
    Q[:, i] = v / r

    for j in range(i + 1, A.shape[1]):
      R = np.dot(Q[:, i], A[:, j])
      v = A[:, j] - R * Q[:, i]
      r = np.linalg.norm(v)
      Q[:, j] = v / r

  return Q

if __name__ == "__main__":
  A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  Q = gram_schmidt(A)
  print(Q)
