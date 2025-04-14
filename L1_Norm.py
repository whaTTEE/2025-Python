import numpy as np
from sklearn.preprocessing import Normalizer

features = np.array([[0.5, 0.5],
                    [1.1, 3.4],
                    [1.5, 20.2],
                    [1.63, 34.4],
                    [10.9, 3.3]])

#변환기 객체를 만든다.
Normalizer = Normalizer(norm="l2") 
#벡터의 크기를 1로 만드는 L2 정규화
#특성 행렬을 만든다.
result = Normalizer.transform(features)
print(result)
