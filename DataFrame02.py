import numpy as np
data = [["LEE", 38, True], ["Kim", 25, False]]

matrix = np.array(data)
pd.DataFrame(matrix, columns=['Name', "Age", "Driver"])
