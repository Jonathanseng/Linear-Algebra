import numpy as np

def create_diagonal_matrix(values):
  """Creates a diagonal matrix."""
  diagonal_matrix = np.zeros((len(values), len(values)))
  for i in range(len(values)):
    diagonal_matrix[i, i] = values[i]
  return diagonal_matrix

def main():
  values = [1, 2, 3]
  diagonal_matrix = create_diagonal_matrix(values)
  print(diagonal_matrix)

if __name__ == "__main__":
  main()
