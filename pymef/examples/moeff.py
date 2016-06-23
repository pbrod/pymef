#! /usr/bin/env python

from pyMEF.Families import *
from pyMEF.Build import BregmanSoftClustering

import numpy
from pylab import imread
import sys

if len(sys.argv) < 4:
    print "usage: %s ef k image [output]" % sys.argv[0]
    sys.exit(1)

ef = eval(sys.argv[1])
k  = int(sys.argv[2])
im = imread(sys.argv[3])
if im.dtype != numpy.uint8:
    im = 256 * im
output = None
if len(sys.argv) > 4:
    output = sys.argv[4]

d = ef.dim
init = "random"

if d == 1:
    data = numpy.array(PointSet.intensity(im), dtype=numpy.float)
    init = "uniqrandom"
elif d <= 3:
    data = PointSet.rgb(im)[:,0:d]
elif d <= 5:
    data = PointSet.rgbxy(im)[:,0:d]
else:
    print "Error, invalid dimension"
    sys.exit(2)
em = BregmanSoftClustering(ef, k, data, init)

em.initialize()
for e in em:
    print  "logLikelihood", e

mm = em.mixture()
print mm.Source()
print mm.weights

if output:
    mm.savetxt(output)
else:
    if d == 1:
        import numpy
        from matplotlib import pyplot
        import pyMEF.display
        
        pyplot.subplot(2, 1, 1)
        pyplot.hist(data, 256)
        pyplot.xlim(0,256)
        
        pyplot.subplot(2, 1, 2)
        pyMEF.display.plot1D(mm, numpy.arange(0, 255, 0.1), components = True)
        pyplot.xlim(0,256)
        
        pyplot.show()
