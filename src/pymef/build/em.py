import numpy

from sklearn.mixture import GMM

from ..families import UnivariateGaussian, MultivariateGaussian
from ..mixture_model import MixtureModel


class EM(MixtureModel):
    def __init__(self, data, k, efclass, efparam):
        assert(efclass is UnivariateGaussian or
               efclass is MultivariateGaussian)

        self.dim = data.shape[1]
        self._size = k

        self._efclass = efclass
        self._efparam = efparam

        MixtureModel.__init__(self, self._size, efclass, efparam)
        gmm = GMM(n_components=k)
        self._gmm = gmm
        gmm.fit(data)

        assert(self.dim == self._ef.dim)

        for i in xrange(self._size):
            self[i].source((gmm.means[i], gmm.covars[i]))

        self.weights = gmm.weights

if __name__ == "__main__":
    from pylab import imread
    import sys

    k = 8
    im = imread("examples/data/ar.ppm")
    data = (im.sum(axis=2)/3.0).flatten().reshape((-1, 1))
    print data.shape
    mm = EM(data, 8, UnivariateGaussian, ())
    mm.savetxt(sys.stdout)

    from matplotlib import pyplot

    pyplot.subplot(2, 1, 1)
    pyplot.hist(data, 256)
    pyplot.xlim(0, 256)

    pyplot.subplot(2, 1, 2)
    x = numpy.arange(0, 255, 0.1)
    pyplot.plot(x, mm(x))
    pyplot.xlim(0, 256)
    pyplot.show()
