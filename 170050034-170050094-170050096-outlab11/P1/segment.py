#!/usr/bin/env python3
import sys, numpy
from scipy import misc

labels = ['sea', 'lake', 'vegetation', 'builtup']
samples = [3, 1, 4, 1]
colors = [0, 75, 128, 255]
means = numpy.zeros(shape=(4, 3))

for i in range(len(labels)):
    sumation = numpy.zeros(shape=(3,))
    count = 0
    images = map(lambda x: labels[i]+x+'.png', [''] if samples[i] == 1 else map(str, range(1, 1+samples[i])))
    for image in images:
        data = misc.imread(image)
        sumation += numpy.sum(data, axis=(0, 1))
        count += data.shape[0]*data.shape[1]
    means[i] = sumation/count
means = numpy.array(means)

if len(sys.argv) < 2 or sys.argv[1] not in ['eu', 'man']:
    print('Unknown option')
else:
    data = misc.imread('mumbai.png')
    if sys.argv[1] == 'eu':
        data = numpy.array([numpy.linalg.norm(data-mean, axis=(2,)) for mean in means])
    else:
        data = numpy.array([numpy.sum(numpy.abs(data-mean), axis=(2,)) for mean in means])
    data = numpy.argmin(data, axis=0)
    data = numpy.vectorize(lambda x: colors[x])(data)
    misc.imsave('segmented_'+sys.argv[1]+'.png', data)
