import numpy as np
matrix = np.array([[1, 2, 3],
                  [4 ,5 ,6],
                  [7 ,8 ,9]])

print(matrix.reshape(-1))
print(matrix.reshape(9))
print(matrix.ravel())
print(matrix.T)
print("")
print(matrix)
print(matrix.flatten())
print(matrix.diagonal()) #대각 원소만 반환
print(matrix.trace()) # 대각합 반환
