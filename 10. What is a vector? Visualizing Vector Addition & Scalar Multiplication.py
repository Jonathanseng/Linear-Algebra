import matplotlib.pyplot as plt
import numpy as np

def visualize_vector_addition(v1, v2):
  """Visualizes the addition of two vectors."""
  plt.quiver([0, 0], [0, 0], v1[0], v1[1], color='blue', scale=1)
  plt.quiver([0, 0], [0, 0], v2[0], v2[1], color='red', scale=1)
  plt.quiver([0, 0], [0, 0], v1[0] + v2[0], v1[1] + v2[1], color='green', scale=1)
  plt.show()

def visualize_scalar_multiplication(v, s):
  """Visualizes the scalar multiplication of a vector."""
  plt.quiver([0, 0], [0, 0], v[0], v[1], color='blue', scale=1)
  plt.quiver([0, 0], [0, 0], s * v[0], s * v[1], color='green', scale=1)
  plt.show()

if __name__ == "__main__":
  # Define two vectors
  v1 = np.array([1, 2])
  v2 = np.array([3, 4])

  # Visualize the addition of the vectors
  visualize_vector_addition(v1, v2)

  # Visualize the scalar multiplication of the first vector
  visualize_scalar_multiplication(v1, 2)
