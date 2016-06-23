import numpy

__all__ = ['Divergence', 'BregmanDivergence', 'KullbackLeibler', 'BurbeaRao',
           'Bhattacharyya']


class Divergence(object):
    def __str__(self):
        return self.__class__.__name__


class BregmanDivergence(Divergence):
    def __init__(self, ef):
        self._ef = ef
        self._inner = ef.inner

    def right_centroid(self, data, weights):
        c = numpy.empty((), dtype=self._ef._natural_dtype)
        for labelN in self._ef._natural_dtype.names:
            c[labelN] = numpy.average(data[labelN], axis=0, weights=weights)
        return c

    def left_centroid(self, data, weights):
        c = numpy.empty((), dtype=self._ef._expectation_dtype)
        n = data.shape[0]
        new_data = numpy.empty(n, dtype=self._ef._expectation_dtype)
        for i in xrange(n):
            new_data[i] = self._ef.gradF(data[i])

        for label in self._ef._expectation_dtype.names:
            c[label] = numpy.average(new_data[label], axis=0, weights=weights)
        return self._ef.gradG(c)

    def __call__(self, p, q):
        assert(p.dtype == self._ef._natural_dtype)
        assert(q.dtype == self._ef._natural_dtype)

        # if p.ndim == 0:
        #     p = p.reshape(1)
        #     shape = q.shape
        # else:
        #     shape = p.shape

        diff = numpy.empty((), dtype=p.dtype)
        for labelN in self._ef._natural_dtype.names:
            diff[labelN] = p[labelN] - q[labelN]

        return (self._ef.F(p) - self._ef.F(q) -
                self._inner(self._ef.gradF(q), diff))


class KullbackLeibler(Divergence):
    def __call__(self, p, q):
        assert(p.__class__ is q.__class__)
        bd = BregmanDivergence(p)
        return bd(p.natural(), q.natural())


class BurbeaRao(Divergence):
    def __init__(self, ef):
        self._ef = ef

    def __call__(self, p, q):
        assert(p.dtype == self._ef._natural_dtype)
        assert(q.dtype == self._ef._natural_dtype)

        F = self._ef.F

        # s = 0.5 * ( p + q)
        s = numpy.empty(1, dtype=self._ef._natural_dtype)
        for label in self._ef._natural_dtype.names:
            s[label] = 0.5 * (p[label] + q[label])

        return 0.5 * (F(p) + F(q)) - F(s)

    def centroid(self, data, weights):
        # e = 0.001
        gradF = self._ef.gradF
        gradG = self._ef.gradG
        n = data.shape[0]
        count = 0

        # left KL centroid
        data1 = numpy.empty(n, dtype=self._ef._expectation_dtype)
        for i in xrange(n):
            data1[i] = gradF(data[i])

        c = numpy.empty(1, dtype=self._ef._expectation_dtype)
        for label in self._ef._expectation_dtype.names:
            c[label] = numpy.average(data1[label], axis=0, weights=weights)
        c = gradG(c)

        # c0 = c
        # while self(c0, c) > e and count < 10 or count == 0:
        while count < 10:
            # s = w_i * gradF(tmp).sum(axis = 1)
            s = numpy.zeros(1, dtype=self._ef._expectation_dtype)
            for i in xrange(n):
                # tmp = 0.5 * (data[i] + c)
                x = data[i]
                tmp = numpy.empty(1, dtype=self._ef._natural_dtype)
                for label in self._ef._natural_dtype.names:
                    tmp[label] = 0.5 * (x[label] + c[label])

                gF = gradF(tmp)
                for label in self._ef._expectation_dtype.names:
                    s[label] += weights[i] * gF[label]

            # c0 = c
            c = gradG(s)
            count += 1

        return c


class Bhattacharyya(Divergence):
    def __call__(self, p, q):
        assert(p.__class__ is q.__class__)
        bd = BurbeaRao(p)
        return bd(p.natural(), q.natural())


if __name__ == "__main__":
    from ..families import UnivariateGaussian
    from ..mixture_model import MixtureModel

    mm = MixtureModel(4, UnivariateGaussian, ())
    mm[0].source((9, 1))
    mm[1].source((11, 1))
    mm[2].source((8, 1))
    mm[3].source((12, 1))

    br = BurbeaRao(UnivariateGaussian())

    c = UnivariateGaussian()
    c.natural(br.centroid(mm.natural(), numpy.array([0.25, 0.25, 0.25, 0.25])))

    print c.source()
    print br(c.natural(), mm[0].natural())
    print br(c.natural(), mm[1].natural())

    g = UnivariateGaussian()
    g.source((10, 3))
    print br(g.natural(), mm[0].natural())
    print br(g.natural(), mm[1].natural())

    g = UnivariateGaussian()
    g.source((10, 1))
    print br(g.natural(), mm[0].natural())
    print br(g.natural(), mm[1].natural())
