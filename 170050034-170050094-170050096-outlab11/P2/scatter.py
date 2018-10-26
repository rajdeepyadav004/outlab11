#!/usr/bin/env python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def main():
	data = np.loadtxt("3dpd.out", delimiter = "," )

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')


	ax.scatter(data[:,0], data[:,1], data[:,2], c='r', marker='o')
	plt.show()

if __name__ == '__main__':
	main()