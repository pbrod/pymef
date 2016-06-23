#! /usr/bin/env python

import numpy
from pylab import imread
import sys
from matplotlib import pyplot

from pyMEF.Build import BregmanSoftClustering, KDE
from pyMEF.Simplify import BregmanHardClustering
from pyMEF.Families import *

if len(sys.argv) < 4:
    print "usage: %s method k image [output]" % sys.argv[0]
    sys.exit(1)

method = sys.argv[1]
k = int(sys.argv[2])
im_path = sys.argv[3]
output = None
if len(sys.argv) > 4:
    output = sys.argv[4]
init = "random"

print "Loading image",
sys.stdout.flush()

im = imread(im_path)
if im.dtype != numpy.uint8:
    im = 256 * im

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
print "."

print "Generating mixture",
sys.stdout.flush()

if method == "em":
    em = BregmanSoftClustering(data, k, MultivariateGaussian, (5,), k, verbose=True)
    mm = em.run()
elif method == "kde":
    mm = KDE(data, MultivariateGaussian, (5,), covariance_factor=0.001)
    if k > 0:
        kmeans = BregmanHardClustering(mm, k)
        mm = kmeans.run()
else:
    print "Unknown method: choose between em or kde !"
    sys.exit(1)
print "."

print "Creating statistical image",
sys.stdout.flush()

count = width * height
needed = 10

newim = numpy.zeros((width, height, 3), dtype=numpy.float)
counts = numpy.zeros((width, height), dtype=numpy.float)

i = 0
while counts.min() < needed:# and i < 100:
    print "At least %i samples by point (need %i, iteration %i, max %i)" % (counts.min(), needed, i, counts.max())
    print numpy.count_nonzero(counts)
    i += 1
    points = mm.rand(count)
    
    for RGBxy in points:
        x = int(RGBxy[3])
        y = int(RGBxy[4])
        # print x, y, RGBxy[0:3], width, height
        if x >= 0 and x < width and y >= 0 and y < height:
            # print "position ok"
            rgb = RGBxy[0:3]
            if rgb[0] >= 0 and rgb[0] < 256 and rgb[1] >= 0 and rgb[1] < 256 and rgb[2] >= 0 and rgb[2] < 256:
                # print "color ok"
                newim[x, y] += rgb
                counts[x, y] += 1
                # print newim[x, y], counts[x, y], counts.sum()

print "."

for i in xrange(width):
    for j in xrange(height):
        if counts[i, j] > 0:
            newim[i, j] /= 256 * counts[i, j]
pyplot.imshow(newim)

if output:
    pyplot.imsave(output)
else:
    pyplot.show()
