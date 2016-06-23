""" Main class for mixture models

Description
-----------
A mixture model is a powerful framework commonly used to estimate the
probability density function (PDF) of a random variable.

Let us consider a mixture model \f$f\f$ of size \f$n\f$. The probability
density function \f$f\f$ evaluated at \f$x \in R^d\f$ is given by

     \f[ f(x) = \sum_{i=1}^n \alpha_i f_i(x)\f]

where \f$\alpha_i \in [0,1]\f$ denotes the weight of the \f$i^{\textrm{th}}\f$
mixture component \f$f_i\f$ such as \f$\sum_{i=1}^n \alpha_i=1\f$.

The MixtureModel class provides a convenient way to create and manage mixture
of exponential families.

"""

from bisect import bisect
import numpy

from .families import Distribution


class MixtureModel(Distribution):
    """
    #
    #      * Constant for serialization.
    #
    serialVersionUID = 1

    #
    #      * Exponential family of the mixture model.
    #
    EF = None

    #
    #      * Number of components in the mixture model.
    #
    size = int()

    #
    #      * Array containing the weights of the mixture components.
    #
    weight = []

    #
    #      * Array containing the parameters of the mixture components.
    #
    param = []

    #
    #      * Class constructor.
    #      * @param n  number of components in the mixture models.

    """
    def __init__(self, size, efclass, efparam):
        self._size = size
        self._efclass = efclass
        self._efparam = efparam

        self._ef = efclass(*efparam)
        self.dim = self._ef.dim
        self._source_dtype = self._ef._source_dtype
        self._natural_dtype = self._ef._natural_dtype
        self._expectation_dtype = self._ef._expectation_dtype

        self._components = []
        self.weights = numpy.ones(self._size, dtype=numpy.float) / float(self._size)

        self._source = None
        self._natural = None
        self._expectation = None

        for i in xrange(size):
            ef = efclass(*efparam)
            self._components.append(ef)

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in xrange(self._size):
            yield (self.weights[i], self._components[i])

    def __getitem__(self, idx):
        return self._components[idx]

    def source(self, data=None, weights=None):
        if data is not None:
            if isinstance(data, numpy.ndarray):
                data.dtype = self._source_dtype
            else:
                data = numpy.array(data, dtype = self._source_dtype)
            if weights is not None:
                self.weights = weights

            self._source = data
            self._natural = None
            self._expectation = None

            for i in xrange(self._size):
                self[i].source(self._source[i])

            return data
        else:
            if self._source is not None:
                return self._source
            else:
                self._source = numpy.empty(self._size, dtype=self._source_dtype)
                for i in xrange(self._size):
                    self._source[i] = self[i].source()
                return self._source

    def natural(self, data=None, weights=None):
        if data is not None:
            if isinstance(data, numpy.ndarray):
                data.dtype = self._natural_dtype
            else:
                data = numpy.array(data, dtype = self._natural_dtype)
            if weights is not None:
                self.weights = weights

            self._source = None
            self._natural = data
            self._expectation = None

            for i in xrange(self._size):
                self[i].natural(self._natural[i])

            return data
        else:
            if self._natural is not None:
                return self._natural
            else:
                self._natural = numpy.empty(self._size, dtype=self._natural_dtype)
                for i in xrange(self._size):
                    self._natural[i] = self[i].natural()
                return self._natural

    def expectation(self, data=None, weights=None):
        if data is not None:
            if isinstance(data, numpy.ndarray):
                data.dtype = self._expectation_dtype
            else:
                data = numpy.array(data, dtype = self._natural_dtype)
            if weights is not None:
                self.weights = weights

            self._source = None
            self._natural = None
            self._expectation = data

            for i in xrange(self._size):
                self[i].expectation(self._expectation[i])

            return data
        else:
            if self._expectation is not None:
                return self._expectation
            else:
                self._expectation = numpy.empty(self._size, dtype=self._expectation_dtype)
                for i in xrange(self._size):
                    self._expectation[i] = self[i].expectation()
                return self._expectation

    def density(self, x):
        d = 0.
        for i in xrange(self._size):
            d += self.weights[i] * self[i](x)

        return d

    def rand(self, size = 1):
        n = numpy.array(size).prod()
        output = numpy.empty((n, self.dim))
        thresholds = self.weights.cumsum()[:-1]
        t = numpy.random.rand(n)

        for i in xrange(n):
            k = bisect(thresholds, t[i])
            output[i] = self._components[k].rand()

        if type(size) == int:
            return output.reshape([size, -1])
        else:
            return output.reshape(size + (-1,))

    def savetxt(self, fname):
        if isinstance(fname, str):
            f = open(fname, "w")
        else:
            f = fname

        print >>f, str(self._efclass) + str(self._efparam)
        for i in xrange(len(self)):
            source = self[i].source()
            source = source.reshape(1)
            source = source.view(numpy.double)
            print >>f, i, ":", self.weights[i], ' ',
            numpy.savetxt(f, source, newline=" ")
            print >>f

        if isinstance(fname, str):
            f.close()

    def loadtxt(self, fname):
        if isinstance(fname, str):
            f = open(fname)
        else:
            f = fname

        components = []
        weights = []

        f.readline()
        for l in f:
            (_, remaining) = l.split(":")
            tmp = remaining.split()
            weight = float(tmp[0])
            params = numpy.fromstring(" ".join(tmp[1:]), sep=" ")
            params.dtype = self._source_dtype
            ef = self._efclass(*self._efparam)
            ef.source(params)
            components.append(ef)
            weights.append(weight)

        self._size = len(components)
        self._components = components
        self.weights = numpy.array(weights)

        if isinstance(fname, str):
            f.close()

    def fromlist(self, l):
        components = []
        weights = []

        for (w, c) in l:
            components.append(c)
            weights.append(w)

        self._size = len(components)
        self._components = components
        self.weights = numpy.array(weights)
        self.weights /= self.weights.sum()


def demo_mixture_models():
    import sys
    if len(sys.argv) > 1:
        from Families.UnivariateGaussian import UnivariateGaussian
        mm = MixtureModel(0, UnivariateGaussian, ())
        mm.loadtxt(sys.argv[1])

        from matplotlib import pyplot
        x = numpy.arange(0,100,0.1)
        pyplot.plot(x, mm(x))
        pyplot.show()
    else:
        from Families.UnivariateGaussian import UnivariateGaussian
        mm = MixtureModel(4, UnivariateGaussian, ())
        mm[0].source((2, 1))
        mm[1].source((5, 1))
        mm[2].source((15, 1))
        mm.weights[2] = 0.20
        mm[3].source((20, 1))
        mm.weights[3] = 0.05

        for (w, ef) in mm:
            print w, ef.source()

        mm.savetxt(sys.stdout)

        import StringIO
        f = StringIO.StringIO()
        mm.savetxt(f)
        f.seek(0)
        mm2 = MixtureModel(4, UnivariateGaussian, ())
        mm2.loadtxt(f)
        mm2.savetxt(sys.stdout)

        from matplotlib import pyplot
        x = numpy.arange(0,30,0.1)
        pyplot.plot(x, mm(x))
        pyplot.show()

        pyplot.hist(mm.rand(10000), 100)
        pyplot.show()


if __name__ == "__main__":
    demo_mixture_models()
