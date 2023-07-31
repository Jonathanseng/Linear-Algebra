import numpy as np

def is_one_to_one(transformation, vectors):
  """
  Returns True if the transformation is one-to-one, False otherwise.

  Args:
    transformation: A function that takes a vector and returns a transformed vector.
    vectors: A list of vectors.

  Returns:
    True if the transformation is one-to-one, False otherwise.
  """

  for i in range(len(vectors)):
    for j in range(i + 1, len(vectors)):
      if transformation(vectors[i]) == transformation(vectors[j]):
        return False
  return True

def is_onto(transformation, vectors):
  """
  Returns True if the transformation is onto, False otherwise.

  Args:
    transformation: A function that takes a vector and returns a transformed vector.
    vectors: A list of vectors.

  Returns:
    True if the transformation is onto, False otherwise.
  """

  for vector in vectors:
    exists = False
    for i in range(len(vectors)):
      if transformation(vectors[i]) == vector:
        exists = True
        break
    if not exists:
      return False
  return True

def main():
  """
  Example usage of the is_one_to_one and is_onto functions.
  """

  transformation = lambda vector: vector * 2
  vectors = np.array([[1, 2], [3, 4], [5, 6]])
  print(is_one_to_one(transformation, vectors))
  print(is_onto(transformation, vectors))

if __name__ == "__main__":
  main()
