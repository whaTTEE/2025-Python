import pandas as pd
url = "https://bit.ly/3Tb15qr"
dataframe = pd.read_csv(url)
dataframe.replace(1, "One").head(10)
dataframe.replace([0,1],["Zero","One"]).head(10)
