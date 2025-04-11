import numpy as np
from sklearn.preprocessing import Normalizer

#특성 행렬을 만든다.
features = np.array([[0.5, 0.5],
                     [1.1, 3.4],
                     [1.5, 20.2],
                     [1.63, 34.4],
                     [10.9, 3.3]])

#변환기 객체를 만든다.
normalizer = Normalizer(norm="l2")
#특성 행렬을 변환한다.
result = normalizer.transform(features)
print(result)
