import pandas as pd
import numpy as np

time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

dataframe = pd.DataFrame(index=time_index)

dataframe["Sale_Amount"] = np.random.randint(1, 10, 100000) #난수 값으로 열을 만든다.

dataframe.resample('W').sum()

dataframe.head(3)

dataframe.resample('3W').mean() #3주 단위로 그룹핑하고 평균을 계산

dataframe.resample('M').count() #한 달 간격으로 그룹핑하고 행을 카운트

dataframe.resample('M', label='left').count()

url = "https://bit.ly/3Tb15qr"

dataframe = pd.read_csv(url)

dataframe.agg("min")

# for name in dataframe["Name"][0:2]:
#          print(name.upper())

def uppercase(x):
     return x.upper()

dataframe["Name"].apply(uppercase)[0:2]

dataframe["Survived"].map({0:"Dead",1:"Live"})[:5]

dataframe["Age"].apply(lambda x, age: x < age, age=30)[:5]
