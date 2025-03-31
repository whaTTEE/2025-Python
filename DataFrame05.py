import pandas as pd
url = "https://bit.ly/3Tb15qr"
dataframe = pd.read_csv(url)
dataframe["Sex"].replace(["female","male"],["Woman","Man"]).head(5)
