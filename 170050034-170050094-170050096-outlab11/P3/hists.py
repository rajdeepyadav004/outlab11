#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def main():

	file = open("survey_data.csv", "r")
	data = file.readlines()
	file.close()

	data = [line[:len(line)-1].split(",")[1:] for line in data[:(len(data) - 1)]] + [data[len(data) - 1].split(",")[1:]]

	columns = data[0][1:]
	data = data[1:]

	N = len(data[0])

	def count(catagory, res):
		ans = 0
		for i in range(len(data)):
			if (data[i][catagory] == res):
				ans +=1
		return ans

	ess = [count(i, "Essential") for i in range(len(data[0]))]
	nice = [count(i, "Nice to have") for i in range(len(data[0]))]
	noOneCares = [count(i, "Dont care one way or another") for i in range(len(data[0]))]
	useless = [count(i, "Utterly useless") for i in range(len(data[0]))]


	print(ess)
	print(nice)
	print(noOneCares)
	print(useless)

	N = len(data[0])
	menMeans = (20, 35, 30, 35, 27)
	womenMeans = (25, 32, 34, 20, 25)
	menStd = (2, 3, 4, 1, 2)
	womenStd = (3, 5, 2, 3, 3)
	ind = np.arange(N)    # the x locations for the groups
	print(N)
	width = 0.35       # the width of the bars: can also be len(x) sequence

	# p1 = plt.bar(ind, menMeans, width, yerr=menStd)
	# p2 = plt.bar(ind, womenMeans, width,
	#              bottom=menMeans, yerr=womenStd)

	p1 = plt.bar(ind, ess, width)
	p2 = plt.bar(ind, nice, width, bottom = ess)
	p3 = plt.bar(ind, noOneCares, width, bottom = [nice[i]+ess[i] for i in range(len(ess))])
	p4 = plt.bar(ind, useless, width, bottom = [nice[i]+ess[i]+noOneCares[i] for i in range(len(ess))])


	plt.ylabel('number of opinions')
	plt.title('opinions by option')
	plt.xticks(ind, columns, rotation = "vertical")
	plt.yticks(np.arange(0, 21, 4))
	plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Essential', 'Nice to have', 'Dont care one way or another', 'Utterly useless'))

	plt.savefig("hists.png")


if __name__ == '__main__':
	main()