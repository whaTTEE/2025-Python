import numpy as np

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
b = b.reshape(2,3,2)
print(np.matmul(a,b))

