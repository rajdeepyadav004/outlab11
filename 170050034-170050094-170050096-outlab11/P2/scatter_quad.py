#!/usr/bin/env python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin


def main():
	data = np.loadtxt("3dpd.out", delimiter = "," )

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	a, b, c = 3,1,2
	# color = [(lambda x, y, z: 'r' if (a*z+b*(x**2+y**2)+c>0) else 'b')(x, y, z) for x, y, z in data]
	color = [(lambda x, y, z: 'r' if (sin(a*x+b*y+c*z)>0) else 'b')(x, y, z) for x, y, z in data]

	ax.scatter(data[:,0], data[:,1], data[:,2], c=color, marker='o')
	plt.show()

if __name__ == '__main__':
	main()