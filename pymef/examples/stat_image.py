#! /usr/bin/env python

import numpy
from pylab import imread
import sys
from matplotlib import pyplot

from pyMEF.Build import BregmanSoftClustering#, MixtureModel
from pyMEF.Families import *

if len(sys.argv) < 4:
    print "usage: %s ef k image [mixture] [output]" % sys.argv[0]
    sys.exit(1)

ef = eval(sys.argv[1])
k = int(sys.argv[2])
im = imread(sys.argv[3])
if im.dtype != numpy.uint8:
    im = 256 * im
# mixture = None
# if len(sys.argv) > 4:
#     mixture = sys.argv[4]
output = None
# if len(sys.argv) > 5:
#     output = sys.argv[5]
init = "random"

width = im.shape[0]
height = im.shape[1]

data = numpy.empty((width*height, 5))
cur = 0
for i in xrange(width):
    for j in xrange(height):
        data[cur, 0] = im[i, j, 0]
        data[cur, 1] = im[i, j, 1]
        data[cur, 2] = im[i, j, 2]
        data[cur, 3] = i
        data[cur, 4] = j
        cur += 1

em = BregmanSoftClustering(data, k, ef, (5,), k, verbose=True)
mm = em.run()

count = 100 * width * height
points = mm.rand(count)
newim = numpy.zeros((width, height, 3), dtype=numpy.float)
counts = numpy.zeros((width, height), dtype=numpy.float)

for RGBxy in points:
    x = int(RGBxy[3])
    y = int(RGBxy[4])
    if x >= 0 and x < width and y >= 0 and y < height:
        rgb = RGBxy[0:3]
        if rgb[0] > 0 and rgb[0] < 256 and rgb[1] > 0 and rgb[1] < 256 and rgb[2] > 0 and rgb[2] < 256:
            newim[x, y] += rgb
            counts[x, y] += 1

for i in xrange(width):
    for j in xrange(height):
        if counts[i, j] > 0:
            newim[i, j] /= 256 * counts[i, j]
pyplot.imshow(newim)

if output:
    pyplot.imsave(output)
else:
    pyplot.show()
