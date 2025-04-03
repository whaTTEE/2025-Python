import pandas as pd
url = "https://bit.ly/3Tb15qr"
dataframe = pd.read_csv(url)
dataframe.groupby("Sex").apply(lambda x : x.count())
data_a = {"id" : ['1', '2', '3'],
          "first" : ["Alex", "Amy", "Allen"],
          "last" : ["Anderson", "Ackerman","Ali"]}
          
dataframe_a = pd.DataFrame(data_a, columns=["id", "first", "last"])

data_b = {"id" : ['4', '5', '6'],
          "first" : ["A", "y", "n"],
          "last" : ["An", "Ac","Al"]}
          
dataframe_b = pd.DataFrame(data_b, columns=["id", "first", "last"])

pd.concat([dataframe_a, dataframe_b], axis=0) #concat함수는 데이터프레임을 합치는 함수
pd.concat([dataframe_a, dataframe_b], axis=1) #concat함수는 데이터프레임을 합치는 함수
