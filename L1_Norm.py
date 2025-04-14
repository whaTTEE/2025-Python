import numpy as np
from sklearn.preprocessing import Normalizer

features = np.array([[0.5, 0.5],
                    [1.1, 3.4],
                    [1.5, 20.2],
                    [1.63, 34.4],
                    [10.9, 3.3]])

#변환기 객체를 만든다.
Normalizer = Normalizer(norm="l1") 
#맨허튼 노름
#특성 행렬을 만든다.
result = Normalizer.transform(features)
print(result)

#샘플들의 특성값의 합을 1로 만든다. 
#실제로 이러한 성질이 필요할 때가 있다고 한다.
