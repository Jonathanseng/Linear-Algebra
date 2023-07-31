def is_linear_independent(S):
  """
  This function checks if a set of polynomials is linearly independent.

  Args:
    S: The set of polynomials to be checked.

  Returns:
    True if the set is linearly independent, False otherwise.
  """

  n = len(S)

  # Check if the set contains the zero polynomial.

  if 0 in S:
    return False

  # Check if any polynomial in the set can be expressed as a linear combination of the other polynomials.

  for i in range(n):
    v = S[i]
    for j in range(i):
      w = S[j]
      if v == w or v == -w:
        continue
      if v == c * w for c in range(-10, 11):
        continue
      return False

  return True


def main():
  S = [x**2 + x + 1, x**2 - x + 1, x**2 - 2*x + 1]

  print(is_linear_independent(S))


if __name__ == "__main__":
  main()
