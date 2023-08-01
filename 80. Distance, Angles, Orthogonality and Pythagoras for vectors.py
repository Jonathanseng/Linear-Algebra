import numpy as np

def distance(v1, v2):
  """Computes the distance between v1 and v2."""
  return np.sqrt(np.sum((v1 - v2)**2))

def angle(v1, v2):
  """Computes the angle between v1 and v2."""
  return np.arccos(dot_product(v1, v2) / (length(v1) * length(v2)))

def orthogonality(v1, v2):
  """Computes whether v1 and v2 are orthogonal."""
  return abs(dot_product(v1, v2)) < 1e-10

def pythagoras(a, b):
  """Computes the length of the hypotenuse of a right triangle."""
  return np.sqrt(a**2 + b**2)

def main():
  v1 = np.array([1, 2])
  v2 = np.array([3, 4])
  print(distance(v1, v2))
  print(angle(v1, v2))
  print(orthogonality(v1, v2))
  print(pythagoras(3, 4))

if __name__ == "__main__":
  main()
