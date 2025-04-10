import numpy as np
from sklearn import preprocessing

feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])


#스케일러 객체를 만든다.
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
#특성의 스케일을 변환한다.
scaled_feature = minmax_scale.fit_transform(feature)
#특성을 출력한다.
print(scaled_feature)
