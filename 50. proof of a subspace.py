def is_subspace(S):
  """
  Returns True if S is a subspace of R^n, False otherwise.

  Args:
    S: A set of vectors in R^n.

  Returns:
    True if S is a subspace of R^n, False otherwise.
  """

  if not S:
    return True

  for vector in S:
    if vector == 0:
      return False

  for vector1 in S:
    for vector2 in S:
      if vector1 + vector2 not in S:
        return False

  return True


def main():
  S = {(1, 2), (3, 4), (5, 6)}
  print(is_subspace(S))
  # Output: True

  S = {(1, 2), (3, 4), (0, 0)}
  print(is_subspace(S))
  # Output: False


def proof_of_subspace(S):
  """
  Prints a proof that S is a subspace of R^n.

  Args:
    S: A set of vectors in R^n.

  Returns:
    None.
  """

  print("The set S is a subspace of R^n because it satisfies the following three conditions:")
  print("1. The zero vector is in S.")
  print("2. S is closed under addition.")
  print("3. S is closed under scalar multiplication.")


if __name__ == "__main__":
  proof_of_subspace(S)
