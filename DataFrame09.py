import pandas as pd
import numpy as np
url = "https://bit.ly/3Tb15qr"
dataframe = pd.read_csv(url) # 데이터를 적재
dataframe["Sex"].unique() # 고유한 값을 찾음
dataframe["PClass"].value_counts() 
dataframe[dataframe["Age"].isnull()].head(2)  # 누락된 값을 선택하고, 두 개의 행을 출력
dataframe["Sex"] = dataframe["Sex"].replace("male, NaN")
dataframe["Sex"] = dataframe["Sex"].replace("male", np.nan)
dataframe = pd.read_csv(url,na_values=[np.nan, "NONE", -999])
null_entry = dataframe[dataframe["Age"].isna()].head(1) #누락된 값이 있는 행 한 개를 추출해라
print(null_entry)
null_entry.fillna(dataframe["Age"].mean()) #누락된 값을 승객의 평균 나이로 채운다.
dataframe = pd.read_csv(url, na_filter=False)
dataframe[12:14]
dataframe.drop("Age", axis=1).head(2) #열을 삭제하고 행 두 개를 출력
dataframe.drop(["Age","Sex"], axis=1).head(2) #열 두 개를 동시에 삭제
dataframe.drop(dataframe.columns[1], axis=1).head(2)
