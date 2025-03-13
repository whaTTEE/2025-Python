import numpy as np
from scipy import sparse

matrix01 = np.array([[3,6,1],[2,7,6],[2,5,5]])
matrix02 = np.array([[3,6,1],[2,7,6],[2,5,5]])

result = [matrix01, matrix02]
a = np.ravel(result)
print(a)
