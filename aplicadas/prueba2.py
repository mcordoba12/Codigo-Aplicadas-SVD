# First, we load the image
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os  # Importa el módulo os

A = imread(os.path.join(r"C:\Users\angel\Documents\aplicadas", "image.jpg"))
X = np.mean(A, -1)  # Convert RGB to grayscale
img = plt.imshow(X)

# Take the SVD
U, S, VT = np.linalg.svd(X, full_matrices=False)
S = np.diag(S)

# Approximate matrix with truncated SVD for various ranks r
for r in (5, 20, 100):
    # Construct approximate image
    Xapprox = U[:, :r] @ S[0:r, :r] @ VT[:r, :]
    img = plt.imshow(Xapprox)
    plt.show()

    # Plot singular values and cumulative sum
    plt.semilogy(np.diag(S))
    plt.plot(np.cumsum(np.diag(S)) / np.sum(np.diag(S)))
    plt.show()
