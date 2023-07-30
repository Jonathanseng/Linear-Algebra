import numpy as np

def linear_combination(v1, v2, s1, s2):
  """Returns the linear combination of v1 and v2."""
  return s1 * v1 + s2 * v2

def span(v1, v2):
  """Returns the span of v1 and v2."""
  span = set()
  for s1 in range(-2, 3):
    for s2 in range(-2, 3):
      span.add(linear_combination(v1, v2, s1, s2))
  return span

if __name__ == "__main__":
  # Define two vectors
  v1 = np.array([1, 2])
  v2 = np.array([3, 4])

  # Print the span of the two vectors
  print(span(v1, v2))
