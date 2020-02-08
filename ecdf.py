import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
	n = len(data)
	x = np.sort(data)
	y = np.arange(1, n+1) / n
	return x, y

if __name__ == '__main__':
	l = [2,2,2,3,4,4,5,5,5,5,5,5,5,5,6,7,8,9,10,10,10]

	l_mean = np.mean(l)
	print("... l_mean ....")
	print(l_mean)

	l_median = np.median(l)
	print("... l_median ....")
	print(l_median)


	a, b = ecdf(l)
	print("x {}".format(a))
	print("y {}".format(b))
	plt.plot(a, b, marker=".", linestyle='none')
	plt.xlabel('datos generados')
	plt.ylabel("ECDF")
	plt.show()

