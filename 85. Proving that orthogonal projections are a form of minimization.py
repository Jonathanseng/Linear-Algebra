import numpy as np

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

  # Calculate the squared error of the projection.
  error = np.linalg.norm(v - projection)**2

  # Show that the squared error is minimized.
  for i in range(3):
    new_projection = orthogonal_projection(v - u * i, u)
    new_error = np.linalg.norm(v - new_projection)**2
    assert error <= new_error

if __name__ == "__main__":
  main()
