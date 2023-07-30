import numpy as np

def is_in_span(v, vectors):
  """Returns True if v is in the span of vectors, False otherwise."""
  for s in range(len(vectors)):
    v_prime = v - s * vectors[0]
    for i in range(1, len(vectors)):
      v_prime = v_prime - vectors[i]
    if np.allclose(v_prime, np.zeros(v.shape)):
      return True
  return False

if __name__ == "__main__":
  # Define three vectors
  v1 = np.array([1, 2])
  v2 = np.array([3, 4])
  v3 = np.array([5, 6])

  # Check if v3 is in the span of v1 and v2
  print(is_in_span(v3, [v1, v2]))

  # Check if v1 is in the span of v2 and v3
  print(is_in_span(v1, [v2, v3]))
