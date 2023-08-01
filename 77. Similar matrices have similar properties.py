import numpy as np

def similar_matrices_have_similar_properties(A, B):
  """Checks if two matrices are similar and have similar properties."""
  are_similar = np.allclose(np.linalg.eig(A), np.linalg.eig(B))
  if are_similar:
    print("The matrices are similar.")
  else:
    print("The matrices are not similar.")

def main():
  A = np.array([[1, 2], [2, 3]])
  B = np.array([[3, 4], [4, 5]])
  similar_matrices_have_similar_properties(A, B)

if __name__ == "__main__":
  main()
