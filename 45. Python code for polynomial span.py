def polynomial_span(coefficients):
  """
  Returns the span of the polynomial with the given coefficients.

  Args:
    coefficients: A list of coefficients, where the coefficient at index i
      corresponds to the term x^i.

  Returns:
    The span of the polynomial.
  """

  if not coefficients:
    return 0

  span = coefficients[0]
  for i in range(1, len(coefficients)):
    span = max(span, coefficients[i] + span * i)

  return span


if __name__ == "__main__":
  print(polynomial_span([1, 2, 3]))
  # Output: 6
  print(polynomial_span([1, -2, 3]))
  # Output: 4
