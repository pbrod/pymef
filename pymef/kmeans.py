import numpy
from numpy.random import randint
from functools import reduce


class InitError(Exception):
    pass


class L2(object):

    def __call__(self, p, q):
        tmp = (p - q)**2
        if tmp.ndim == 1:
            return tmp.sum()
        else:
            return tmp.sum(axis=1)

    def centroid(self, data, weights):
        return numpy.average(data, axis=0, weights=weights)


class kMeans(object):

    def __init__(self, data, k, div=L2(), weights=None, max_iter=100,
                 init="random"):
        assert(len(data.shape) >= 2)
        self._k = k
        self._data = data
        self._size = data.shape[0]
        self.dim = data.shape[1]
        self._dtype = data.dtype
        self._div = div
        self._centroid = div.centroid
        self._max_iter = max_iter
        self._init = init
        self._guess = None
        if weights is None:
            self._data_weights = numpy.ones(self._size) / self._size
        else:
            self._data_weights = weights

    def __len__(self):
        return self._size

    def __call__(self):
        return self.run()

    def repartition(self):
        return self._repartition

    def sites(self):
        return self._sites

    def weights(self):
        return self._weights

    def run(self):
        self.initialize()

        while self._count < self._max_iter and numpy.all(
                self._repartition != self._old_repartition):
            self.updateRepartition()
            self.updateCentroids()
            self._count += 1
        self.updateError()

        return self

    def guess(self, sites):
        self._guess = sites

    def initialize(self):
        self._count = 0
        self._repartition = numpy.zeros((self._size,), dtype=int) - 1
        self._old_repartition = numpy.zeros((self._size,))
        self._weights = numpy.ones(self._k) / self._k
        self._sites = None

        if self._guess is not None:
            self._sites = self._guess.copy()
            return

        # Takes the first k points
        if self._init == "first":
            self._sites = self._data[0:self.k]

        # Takes k random points
        if self._init == "random":
            perm = numpy.random.permutation(self._size)[0:self._k]
            self._sites = self._data[perm]

        # Takes k random points, ensuring different ones
        if self._init == "uniqrandom":
            self._sites = numpy.empty((self._k, self.dim), dtype=self._dtype)
            perm = numpy.random.permutation(self._size)
            i = 0
            p = 0
            while p < self._k and i < self._size:
                c = self._data[perm[i]]
                ok = True
                for j in xrange(p):
                    if (self._sites[j] == c).all():
                        ok = False
                if ok:
                    self._sites[p] = c
                    p += 1
                i += 1

        if self._init == "kmeans++":
            # http://blogs.sun.com/yongsun/entry/k_means_and_k_means
            X = self._data
            div = self._div
            k = self._k
            n = X.shape[0]

            'choose the 1st seed randomly, and store D(x)^2 in D[]'
            centers = [X[randint(n)]]
            D = [div(x, centers[0]) for x in X]

            for _count in range(k - 1):
                bestDsum = bestIdx = -1

                for i in range(n):
                    'Dsum = sum_{x in X} min(D(x)^2,||x-xi||^2)'
                    Dsum = reduce(lambda x, y: x + y,
                                  (min(D[j], div(X[j], X[i])) for j in xrange(n)))

                    if bestDsum < 0 or Dsum < bestDsum:
                        bestDsum, bestIdx = Dsum, i

                centers.append(X[bestIdx])
                D = [min(D[i], div(X[i], X[bestIdx])) for i in xrange(n)]

            self._sites = numpy.array(centers)

        if self._sites is None:
            raise InitError(self._init)

    def __iter__(self):
        while not(self._count > self._max_iter or numpy.all(
                self._repartition == self._old_repartition)):
            self.updateRepartition()
            self.updateCentroids()
            self.updateError()
            self._count += 1
            yield self._error

    def updateRepartition(self):
        self._old_repartition = self._repartition.copy()
        div = self._div

        for i in xrange(self._size):
            p = self._data[i]
            best_dist = float('inf')
            best_index = -1

            # dists = div(p, self.sites)
            # best_index = numpy.argsort(dists)[0]
            # best_dist = dists[best_index]
            # print dists, best_dist, best_index
            for j in xrange(self._k):
                c = self._sites[j]
                d = div(c, p)
                if d < best_dist:
                    best_dist = d
                    best_index = j
            self._repartition[i] = best_index

    def updateCentroids(self):
        centroid = self._centroid
        for i in xrange(self._k):
            cell = numpy.compress(
                numpy.equal(
                    self._repartition,
                    i),
                self._data,
                0)
            weights = numpy.compress(
                numpy.equal(
                    self._repartition,
                    i),
                self._data_weights,
                0)
            if cell.shape[0] > 0:
                self._sites[i] = centroid(cell, weights)
                self._weights[i] = weights.sum()

    def updateError(self):
        error = 0
        for i in xrange(self._size):
            error += self._data_weights[i] * self._div(
                self._data[i],
                self._sites[
                    self._repartition[i]])
        self._error = error

    def error(self):
        return self._error

if __name__ == "__main__":
    data = numpy.array(
        [[0.0, 0.0], [1.0, 1.0], [0.9, 0.9], [1.0, 0.0], [0.9, 0.1]])
    kmeans = kMeans(data, 3, L2())

    kmeans.initialize()
    for e in kmeans:
        print e
    print kmeans.repartition()

    kmeans.run()
    print kmeans.repartition()
