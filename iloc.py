import pandas as pd
url = "https://bit.ly/47Hl2t5"
dataframe = pd.read_csv(url)
print(dataframe.iloc[:3])

#iloc는 index, 숫자로 불러올때 사용
#loc는 라벨, 이름으로 불러올때 사용
