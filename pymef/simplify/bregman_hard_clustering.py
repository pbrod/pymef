from ..kmeans import kMeans
from ..divergence import BregmanDivergence
from ..mixture_model import MixtureModel


class BregmanHardClustering(kMeans):
    def __init__(self, mixture, k, max_iter=100, init="random"):
        self._mm = mixture
        self._k = k
        self._data = mixture.natural()
        self._data_weights = mixture.weights.copy()
        self._size = len(mixture)
        self._dtype = self._data.dtype
        self._guess = None
        self.dim = mixture.dim

        bregman = BregmanDivergence(mixture._efclass(*mixture._efparam))
        self._div = bregman
        self._centroid = bregman.left_centroid
        self._max_iter = max_iter
        self._init = init

    def run(self):
        kMeans.run(self)
        return self.mixture()

    def mixture(self):
        mixture = MixtureModel(self._k, self._mm._efclass, self._mm._efparam)
        mixture.weights = self._weights.copy()
        mixture.natural(self._sites)
        return mixture

    def guess(self, mm):
        kMeans.guess(self, mm.natural())

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
    hc = BregmanHardClustering(mm, k)

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
