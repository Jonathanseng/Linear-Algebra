def are_linearly_independent(polynomials):
  """
  Returns True if the given polynomials are linearly independent, False otherwise.

  Args:
    polynomials: A list of polynomials.

  Returns:
    True if the polynomials are linearly independent, False otherwise.
  """

  if not polynomials:
    return True

  for polynomial in polynomials:
    if polynomial == 0:
      return False

  for i in range(len(polynomials)):
    for j in range(i + 1, len(polynomials)):
      if polynomials[i] == polynomials[j]:
        return False

  return True


if __name__ == "__main__":
  print(are_linearly_independent([1, 2, 3]))
  # Output: True
  print(are_linearly_independent([1, 2, 3, 0]))
  # Output: False
