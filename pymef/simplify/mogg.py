import numpy

from ..families import UnivariateGeneralizedGaussian
# from ..kmeans import kMeans
from ..mixture_model import MixtureModel


class MoG2MoGG(object):
    def __init__(self, mixture, k):
        self._mixture = mixture
        self._k = k

    def run(self):
        pass
        # clusterize
        # foreach cluster:
        #   recenter
        #   solve the moment equation
        #   build the GG
        # build the mixture with the GG

if __name__ == "__main__":
    mm = MixtureModel(4, UnivariateGeneralizedGaussian, ())

    mm[0].source((3.0,))
    mm[0].beta = 2.0
    mm[0].mu = 0.0
    print mm[0]

    mm[1].source((3.0,))
    mm[1].beta = 1.0
    mm[1].mu = 10.0
    print mm[1]

    mm[2].source((3.0,))
    mm[2].beta = 1.5
    mm[2].mu = -10.0
    print mm[2]

    mm[3].source((3.,))
    mm[3].beta = 10.0
    mm[3].mu = 15.0
    print mm[3]

    print mm.weights

    from matplotlib import pyplot
    pyplot.subplot(2, 1, 1)
    x = numpy.arange(-30, 30, 0.1)
    pyplot.plot(x, mm(x))

    pyplot.subplot(2, 1, 2)
    pyplot.xlim(-30, 30)
    pyplot.hist(mm.rand(10000), 100)
    pyplot.show()
