import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

data = [2,2,2,3,4,4,5,5,5,5,5,5,5,5,6,7,8,9,10,10,10]
all_data = []
for x in data:
	all_data.append(["x", x])
print(all_data)

df = pd.DataFrame(all_data, columns=["Variable", "Datos"])


if __name__ == '__main__':

	print("percentiles...")
	percentiles = np.percentile(df['Datos'], [25,50,75])
	print(percentiles)

	print("head .....")
	print(df.head())

	_ = sns.swarmplot(x='Variable', y='Datos', data=df)
	_ = plt.xlabel("state")
	_ = plt.ylabel("Datos")
	plt.show()

