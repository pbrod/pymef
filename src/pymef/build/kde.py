import numpy
from scipy.stats import gaussian_kde

from ..families import *
from ..mixture_model import MixtureModel


class KDE(MixtureModel, gaussian_kde):
    """ Kernel density estimation (only for Gaussian kernels)

    Wrapper around scipy.stats.gaussian_kde providing a consistent interface.
    """

    def __init__(self, data, efclass, efparam,
                 covariance_factor="scotts_factor"):
        assert(efclass is UnivariateGaussian or
               efclass is MultivariateGaussian)

        self.dim = data.shape[1]
        self._size = data.shape[0]

        self._efclass = efclass
        self._efparam = efparam

        if covariance_factor == "silverman_factor":
            self.covariance_factor = self.silverman_factor
        elif covariance_factor == "scotts_factor":
            self.covariance_factor = self.scotts_factor
        elif isinstance(type(covariance_factor), type(1.0)):
            self.covariance_factor = lambda: covariance_factor
        elif isinstance(type(covariance_factor), type(lambda: None)):
            self.covariance_factor = covariance_factor
        else:
            raise ValueError(covariance_factor +
                             " is not a valid covariance factor")

        gaussian_kde.__init__(self, data.T)
        MixtureModel.__init__(self, self._size, efclass, efparam)

        assert(self.dim == self._ef.dim)

        self._source = numpy.empty(self._size, self._source_dtype)
        if efclass is UnivariateGaussian:
            self._source['mu'] = data.T
            self._source['sigma^2'] = self.covariance[0, 0]
        elif efclass is MultivariateGaussian:
            self._source['mu'] = data
            self._source['Sigma'] = self.covariance

        for i in xrange(self._size):
            self[i].source(self._source[i])

    def rand(self, shape):
        points = self.resample(shape)
        points = points.reshape((-1, 1))
        return points

    def density(self, data):
        return self.evaluate(data.T)

if __name__ == "__main__":
    from pylab import imread
    import sys

    k = 8
    im = imread("examples/data/ar.ppm")
    data = (im.sum(axis=2)/3.0).flatten().reshape((-1, 1))
    print data.shape
    mm = KDE(data, UnivariateGaussian, ())
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
