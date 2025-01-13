# Eigen values & Eigen vectors of a matrix

import numpy as np

m = np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])

print("\nOriginal matrix:\n\n", m)

eigen_values, eigen_vectors = np.linalg.eig(m)

print("\nEigen values:\n\n", eigen_values)

print("\nEigen vectors:\n\n", eigen_vectors)
print("\n")
