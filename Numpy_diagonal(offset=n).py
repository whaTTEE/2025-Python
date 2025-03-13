import numpy as np
from scipy import sparse

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix.diagonal(offset=1)) #대각원소 하나 위를 반환한다.
print(matrix.diagonal(offset=-2)) # 두개 아래 반환
