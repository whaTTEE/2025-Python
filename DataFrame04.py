import pandas as pd
url = "https://bit.ly/3Tb15qr"
dataframe = pd.read_csv(url)
# dataframe[dataframe["Sex"] == "female"].head(2)
dataframe[(dataframe["Sex"] == "female") & (dataframe["Age"] >= 65)]
