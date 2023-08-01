def polynomial(x):
  """
  Returns the value of the polynomial p(x) = 2x^3 + 3x^2 - 5x + 1.

  Args:
    x: The value to evaluate the polynomial at.

  Returns:
    The value of the polynomial at x.
  """

  return 2 * x ** 3 + 3 * x ** 2 - 5 * x + 1


if __name__ == "__main__":
  print(polynomial(2))
  # Output: 23
  print(polynomial(-1))
  # Output: -1
