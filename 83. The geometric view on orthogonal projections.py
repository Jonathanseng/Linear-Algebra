import numpy as np
import matplotlib.pyplot as plt

def orthogonal_projection(v, u):
  """
  Performs the orthogonal projection of the vector v onto the vector u.

  Args:
    v: The vector to be projected.
    u: The vector onto which to project.

  Returns:
     The projection of v onto u.
  """

  projection = np.dot(v, u) * u / np.linalg.norm(u)**2
  return projection

def main():
  v = np.array([1, 2, 3])
  u = np.array([2, 0, 0])
  projection = orthogonal_projection(v, u)

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot([0, v[0]], [0, v[1]], [0, v[2]], 'b')
  ax.plot([0, u[0]], [0, u[1]], [0, u[2]], 'r')
  ax.plot([0, projection[0]], [0, projection[1]], [0, projection[2]], 'g')
  plt.show()

if __name__ == "__main__":
  main()
