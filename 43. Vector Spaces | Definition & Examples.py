def is_vector_space(V):
  """
  This function checks if a set is a vector space.

  Args:
    V: The set to be checked.

  Returns:
    True if the set is a vector space, False otherwise.
  """

  # Check if the set is closed under addition.

  for v1 in V:
    for v2 in V:
      if v1 + v2 not in V:
        return False

  # Check if the set is closed under scalar multiplication.

  for v in V:
    for c in range(-10, 11):
      if c * v not in V:
        return False

  # Check if the set has a zero vector.

  if 0 not in V:
    return False

  return True


def main():
  V = {(1, 2), (3, 4), (5, 6)}

  print(is_vector_space(V))


if __name__ == "__main__":
  main()
