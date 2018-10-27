#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from math import log

def plogp(p):
	return 0 if (p==0) else p*log(p,2)

def main():


	file = open("survey_data.csv", "r")
	data = file.readlines()
	file.close()

	file = open("survey_data.csv", "r")
	data = file.readlines()
	file.close()

	data = [line[:len(line)-1].split(",")[1:] for line in data[:(len(data) - 1)]] + [data[len(data) - 1].split(",")[1:]]

	columns = data[0][1:]
	data = data[1:]

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

	entropy = [-(plogp(ess[i]/13)+plogp(nice[i]/13)+plogp(noOneCares[i]/13)+plogp(useless[i]/13)) for i in range(len(ess))]
	columns = [x for _,x in sorted(zip(entropy,columns))]
	entropy = sorted(entropy)

	N = len(ess)
	ind = np.arange(N)    
	width = 0.35       

	p1 = plt.bar(ind, entropy, width)	


	plt.ylabel('entropy')
	plt.title('opinion')
	plt.xticks(ind, columns, rotation = "vertical")
	plt.yticks(np.arange(0, -50, 5))
	# plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Essential', 'Nice to have', 'Dont care one way or another', 'Utterly useless'))

	plt.savefig("contr.png")

if __name__ == '__main__':
	main()