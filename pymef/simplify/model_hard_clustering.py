import numpy

from ..kmeans import kMeans
from ..mixture_model import MixtureModel


def poincare_halfplane2poincare_disk(x):
    dtype = x.dtype
    x.dtype = numpy.complex
    z = (x - 1j) / (x + 1j)
    z.dtype = numpy.double
    x.dtype = dtype
    return z


def poincare_disk2poincare_halfplane(x):
    dtype = x.dtype
    x.dtype = numpy.complex
    z = 1j * (x + 1) / (1 - x)
    z.dtype = numpy.double
    x.dtype = dtype
    return z


def poincare_disk2klein_disk(p):
    q = numpy.empty(p.shape)
    for i in xrange(q.shape[0]):
        q[i] = 2 * p[i] / (1 + numpy.dot(p[i], p[i]))
    return q


def klein_disk2poincare_disk(p):
    q = numpy.empty(p.shape)
    for i in xrange(q.shape[0]):
        norm = numpy.dot(p[i], p[i])
        q[i] = (1 - numpy.sqrt(1 - norm)) / norm * p[i]
    return q


def klein_disk2minkowski(p):
    d = 3
    q = numpy.zeros((p.shape[0], 3))
    for i in xrange(p.shape[0]):
        norm = numpy.sqrt(1 - numpy.dot(p[i], p[i]))
        q[i, 0:d-1] = p[i] / norm
        q[i, d-1] = 1 / norm
    return q


def minkowski2klein_disk(p):
    q = numpy.empty((2,))
    q[0] = p[0] / p[2]
    q[1] = p[1] / p[2]
    return q


def poincare_halfplane2klein_disk(x):
    return poincare_disk2klein_disk(poincare_halfplane2poincare_disk(x))


def klein_disk2poincare_halfplane(x):
    return poincare_disk2poincare_halfplane(klein_disk2poincare_disk(x))


def div_klein(p, q):
    up = 1 - numpy.dot(p, q)
    down = numpy.sqrt((1 - numpy.dot(p, p)) * (1 - numpy.dot(q, q)))
    return numpy.arccosh(up / down)


def centroid(data, weights):
    data = klein_disk2minkowski(data)
    c = weights[0] * data[0]
    for i in xrange(1, data.shape[0]):
        c += weights[i] * data[i]

    norm = c[0]**2
    for i in xrange(1, data.shape[1]):
        norm -= c[i]**2

    c = minkowski2klein_disk(c / norm)

    return c


class ModelHardClustering(kMeans):
    def __init__(self, mixture, k, max_iter=100, init="random"):
        self._mm = mixture
        self._k = k
        data = mixture.source().copy()
        self._dtype = data.dtype
        data.dtype = numpy.float
        data = data.reshape((-1, 2))
        self._data = poincare_halfplane2klein_disk(data)
        self._data_weights = mixture.weights.copy()
        self._size = len(mixture)
        self._dtype = self._data.dtype
        self._guess = None
        self.dim = mixture.dim

        self._div = div_klein
        self._centroid = centroid
        self._max_iter = max_iter
        self._init = init

    def run(self):
        kMeans.run(self)
        return self.mixture()

    def mixture(self):
        mixture = MixtureModel(self._k, self._mm._efclass, self._mm._efparam)
        mixture.weights = self._weights.copy()
        sites = klein_disk2poincare_halfplane(self._sites)
        sites.dtype = self._dtype
        mixture.source(sites)
        return mixture


if __name__ == "__main__":
    import sys
    from ..families import UnivariateGaussian
    from ..mixture_model import MixtureModel

    k = 4
    # mm = MixtureModel(UnivariateGaussian(), fromtxt = sys.argv[1])
    mm = MixtureModel(8, UnivariateGaussian, ())
    mm[0].source((9, 1))
    mm[1].source((11, 1))
    mm[2].source((19, 1))
    mm[3].source((21, 1))
    mm[4].source((29, 1))
    mm[5].source((31, 1))
    mm[6].source((39, 1))
    mm[7].source((41, 1))
    hc = ModelHardClustering(mm, k)

    hc.initialize()
    for e in hc:
        print "Error", e
    mms = hc.mixture()

    print mms.savetxt(sys.stdout)

    import numpy
    from matplotlib import pyplot

    pyplot.subplot(2, 1, 1)
    x = numpy.arange(0,50,0.1)
    pyplot.plot(x, mm(x))
    pyplot.xlim(0,50)

    pyplot.subplot(2, 1, 2)
    x = numpy.arange(0,50,0.1)
    pyplot.plot(x, mms(x))
    pyplot.xlim(0,50)
    pyplot.show()
