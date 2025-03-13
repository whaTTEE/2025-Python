import numpy as np
from scipy import sparse

array = np.array([[3,6,1],[2,7,6],[2,5,5]])
def function(i):
    return i * 100
vertorized_function = np.vectorize(function)
a = vertorized_function(array)
print(a)
