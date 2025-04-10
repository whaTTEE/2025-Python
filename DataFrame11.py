import pandas as pd

# 데이터 정의
data_a = {'id' : ['1', '2', '3'],
          'first' : ['Alex', 'Amy', 'Allen'],
          'last' : ['Anderson', 'Ackerman', 'Ali']}
          

dataframe_a = pd.DataFrame(data_a, columns = ['id', 'first', 'last'])

data_b = {'id' : ['1','2','3'],
          'first' : ['Billy', 'Brain', 'Bran'],
          'last' : ['Bonder', 'Black', 'Balwner']}

dataframe_b = pd.DataFrame(data_b, columns = ['id', 'first', 'last'])

# concat = pd.concat([dataframe_a,dataframe_b], axis=0)
# print(concat)
merge = pd.merge(dataframe_a,dataframe_b, on='id') #on은 merge 함수의 파라미터로써 어떤 것을 기준으로 만들지를 정해줌
print(merge)
