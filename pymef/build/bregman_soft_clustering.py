import sys

import numpy as np
from ..mixture_model import MixtureModel
from ..kmeans import kMeans


class BregmanSoftClustering:
    def __init__(self, data, k, ef, efparam, max_iter=10, init="uniqrandom",
                 verbose=False):
        self._data = data
        self._efclass = ef
        self._efparam = efparam
        self._ef = ef(*efparam)
        self._k = k
        self._threshold = 0.0
        self._size = data.shape[0]
        self._max_iter = max_iter
        self._init = init
        self._verbose = verbose

        self.reset()

    def reset(self):
        self._mm = MixtureModel(self._k, self._efclass, self._efparam)

        self._expectation = np.empty(self._k,
                                     dtype=self._mm._expectation_dtype)
        for i in xrange(self._k):
            self._mm[i].expectation(self._expectation[i])

        self._p = np.empty((self._size, self._k))

    def __call__(self):
        self.run()

    def initialize(self):
        if self._verbose:
            print "I",
        self._count = 0
        self._ll = 0
        self._ll_old = self._threshold

        kmeans = kMeans(self._data, self._k, init=self._init)
        repartition = kmeans().repartition()

        # for all clusters
        for i in xrange(self._k):
            content = np.compress(np.equal(repartition, i), self._data, 0)
            size = content.shape[0]

            # # If all the elements of a clusters are equal, we'll get a
            # # normal distribution with sigma = 0...
            # # Only for d = 1
            # if self.dim == 1 and (content[0] == content).all():
            #     if self.verbose:
            #         print "Adding some noise"
            #     d = self.dim
            #     content += dnp.random.multivariate_normal(np.zeros(d),
            #                0.01 * np.diag(content[0]), size)

            self._mm.weights[i] = float(size) / float(self._size)
            t = self._ef.t(content)

            eta = self._mm[i].expectation()
            for label in self._mm._expectation_dtype.names:
                tmp = t[label].sum(axis=0) / size

                if eta[label].ndim == 0:
                    eta[label] = tmp
                else:
                    eta[label][:] = tmp

        self.logLikelihood()
        self._threshold = np.abs(0.01 * self._ll)

        if self._verbose:
            print "."

    def run(self):
        self.initialize()
        for _e in self:
            pass
        return self._mm

    def __iter__(self):
        # while not (self._count > self._max_iter):
        while not (self._count > self._max_iter or
                   np.abs(self._ll_old - self._ll) < self._threshold):
            self.expectation()
            self.maximisation()
            # self._mm.savetxt(sys.stdout)
            self.logLikelihood()
            self._count += 1
            yield self._ll

    def expectation(self):
        if self._verbose:
            print "E",
        p = self._p
        mm = self._mm
        w = mm.weights
        G = self._ef.G
        gradG = self._ef.gradG
        inner = self._ef.inner
        t = self._ef.t(self._data)

        for i in xrange(self._size):
            s = 0.0
            for j in xrange(self._k):
                eta = self._mm[j].expectation()
                gG = gradG(eta)

                diff = np.empty(t[i].shape, dtype=eta.dtype)
                for labelE in eta.dtype.names:
                    diff[labelE] = t[i][labelE] - eta[labelE]

                p[i, j] = w[j] * np.exp(G(eta) + inner(diff, gG))

                s += p[i, j]

            for j in xrange(self._k):
                p[i, j] /= s

        if self._verbose:
            print "."

    def maximisation(self):
        if self._verbose:
            print "M",
        p = self._p
        w = self._mm.weights
        t = self._ef.t(self._data)

        for j in xrange(self._k):
            s = p[:, j].sum()
            w[j] = s / self._size
            spt = np.zeros(1, dtype=self._mm._expectation_dtype)
            for labelE in self._mm._expectation_dtype.names:
                spt[labelE] = (p[:, j] * t[:][labelE].T).T.sum()
                eta = self._mm[j].expectation()
                eta[labelE] = spt[labelE] / s

        if self._verbose:
            print "."

    def logLikelihood(self):
        if self._verbose:
            print "L",
        mm = self._mm
        self._ll_old = self._ll
        self._ll = mm.logLikelihood(self._data)

        assert not(np.isnan(self._ll))
        if self._verbose:
            print self._ll
        return self._ll

    def mixture(self):
        return self._mm

if __name__ == "__main__":
    from ..families import UnivariateGaussian
    from pylab import imread
    import sys

    k = 8
    im = imread("examples/data/ar.ppm")
    data = (im.sum(axis=2)/3.0).flatten().reshape((-1, 1))
    print data.shape
    em = BregmanSoftClustering(data, k, UnivariateGaussian, ())
    mm = em.run()
    mm.savetxt(sys.stdout)

    from matplotlib import pyplot

    pyplot.subplot(2, 1, 1)
    pyplot.hist(data, 256)
    pyplot.xlim(0, 256)

    pyplot.subplot(2, 1, 2)
    x = np.arange(0, 255, 0.1)
    pyplot.plot(x, mm(x))
    pyplot.xlim(0, 256)
    pyplot.show()
