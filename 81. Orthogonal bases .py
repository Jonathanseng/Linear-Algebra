import numpy as np

def orthogonalize(vectors):
  """Orthogonalizes the vectors in vectors."""
  new_vectors = []
  for i in range(len(vectors)):
    v = vectors[i]
    for j in range(i):
      v -= dot_product(v, vectors[j]) * vectors[j]
    v = v / np.linalg.norm(v)
    new_vectors.append(v)
  return new_vectors

def main():
  vectors = np.array([[1, 2], [3, 4], [5, 6]])
  orthogonalized_vectors = orthogonalize(vectors)
  print(orthogonalized_vectors)

if __name__ == "__main__":
  main()
