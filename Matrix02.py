import numpy as np
matrix = np.array([[1,2],
                   [4,5]])

print(np.random.random(3))
print(np.random.randint(0,11,3))
print(np.random.normal(0,1.0,3)) #평균이 0이고 표준편차가 1인 3개의 수를 뽑음
print(np.random.logistic(0.0, 1.0, 3)) #평균이 0.0이고 스케일이 1.0인 로지스틱 분포에서 세 개의 수를 뽑음
print(np.random.uniform(1.0,2.0,3)) #1.0보다 크거나 같고 2.0보다 작은 세 개의 수를 뽑는다.
print(np.random.rand(2,3))
print(np.random.randint(0,1,10)) #0 이상 1 미만 , 0을 10개 출력
print(np.random.choice([0,1,5], 5)) # 0, 1, 5 셋 중에 5번 랜덤하게 뽑는다.
a = matrix.flatten()
print(a)
print(np.random.permutation(a))
