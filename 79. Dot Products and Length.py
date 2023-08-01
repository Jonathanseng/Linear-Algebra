import numpy as np

def dot_product(v1, v2):
  """Computes the dot product of v1 and v2."""
  return np.sum(v1 * v2)

def length(v):
  """Computes the length of v."""
  return np.sqrt(dot_product(v, v))

def main():
  v1 = np.array([1, 2])
  v2 = np.array([3, 4])
  print(dot_product(v1, v2))
  print(length(v1))

if __name__ == "__main__":
  main()
