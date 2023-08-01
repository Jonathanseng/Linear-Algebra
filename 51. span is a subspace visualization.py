import matplotlib.pyplot as plt
import numpy as np

def span_is_subspace(S):
  """
  Visualizes the span of a set of vectors and shows that it is a subspace.

  Args:
    S: A set of vectors in R^2.

  Returns:
    None.
  """

  fig, ax = plt.subplots()

  for vector in S:
    ax.plot([vector[0], vector[0] + vector[1]], [vector[1], 0], 'b')

  ax.plot([0, 1], [0, 1], 'k')
  ax.set_xlabel('x')
  ax.set_ylabel('y')

  plt.show()


if __name__ == "__main__":
  S = {(1, 2), (3, 4), (5, 6)}
  span_is_subspace(S)
