import numpy as np

def similarity_relationship_represents_change_of_basis(A, eigenvectors):
  """Checks if the similarity relationship represents a change of basis."""
  B = np.dot(eigenvectors, np.diag(np.linalg.eig(A)))
  are_equal = np.allclose(A, B)
  if are_equal:
    print("The similarity relationship represents a change of basis.")
  else:
    print("The similarity relationship does not represent a change of basis.")

def main():
  A = np.array([[1, 2], [2, 3]])
  eigenvectors = np.array([[1, 2], [-2, 1]])
  similarity_relationship_represents_change_of_basis(A, eigenvectors)

if __name__ == "__main__":
  main()
