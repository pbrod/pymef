import numpy as np
from numpy import dot, log, pi, sqrt, exp, outer
from numpy.linalg import inv, det
from math import factorial
from scipy.special import gamma
from ..metropolis import Metropolis

__all__ = ['Distribution', 'ExponentialFamily', 'MultivariateGaussian',
           'UnivariateGaussian', 'UnivariateGeneralizedGaussian']


class Distribution(object):
    def __call__(self, x):
        return self.density(x)

    def pdf(self, x):
        return self.density(x)

    def mean(self):
        return self.moment(1, centered=False, reduced=False)

    def variance(self):
        return self.moment(2, reduced=False)

    def skewness(self):
        return self.moment(3, reduced=False)

    def kurtosis(self):
        return self.moment(4, reduced=False)

    def __str__(self):
        return self.__class__.__name__ + "()"

    def logLikelihood(self, data):
        return (log(self.density(data))).sum()


class ExponentialFamily(Distribution):
    def __init__(self, source=None, natural=None, expectation=None):
        self._source = None
        self._natural = None
        self._expectation = None
        if source is not None:
            self._source = source
        elif natural is not None:
            self._natural = natural
        elif expectation is not None:
            self._expectation = expectation

    def inner(self, p, q):
        s = 0.
        expectation = self._expectation_dtype.names
        natural = self._natural_dtype.names

        for (e, n) in zip(expectation, natural):
            if p[e].ndim <= 1:
                s += dot(p[e], q[n])
            else:
                if p[e].ndim == 2:
                    s += np.trace(dot(p[e].T, q[n]))
        return s

    def theta2lambda(self, data):
        raise NotImplementedError

    def eta2lambda(self, data):
        raise NotImplementedError

    def lambda2theta(self, data):
        raise NotImplementedError

    def lambda2eta(self, data):
        raise NotImplementedError

    def theta2eta(self, data):
        return self.gradF(data)

    def eta2theta(self, data):
        return self.gradG(data)

    def mode(self):
        raise NotImplementedError

    def source(self, data=None):
        if data is not None:
            if isinstance(data, np.ndarray):
                data.dtype = self._source_dtype
            else:
                data = np.array(data, dtype=self._source_dtype)

            self._source = data
            self._natural = None
            self._expectation = None

            return data
        else:
            if self._source is not None:
                return self._source
            if self._natural is not None:
                self._source = self.theta2lambda(self._natural)
                return self._source
            if self._expectation is not None:
                self._source = self.eta2lambda(self._expectation)
                return self._source

    def natural(self, data=None):
        if data is not None:
            if isinstance(data, np.ndarray):
                data.dtype = self._natural_dtype
            else:
                data = np.array(data, dtype=self._natural_dtype)

            self._source = None
            self._natural = data
            self._expectation = None

            return data
        else:
            if self._natural is not None:
                return self._natural
            if self._source is not None:
                self._natural = self.lambda2theta(self._source)
                return self._natural
            if self._expectation is not None:
                self._natural = self.eta2theta(self._expectation)
                return self._natural

    def expectation(self, data=None):
        if data is not None:
            if isinstance(data, np.ndarray):
                data.dtype = self._expectation_dtype
            else:
                data = np.array(data, dtype=self._natural_dtype)

            self._source = None
            self._natural = None
            self._expectation = data

            return data
        else:
            if self._expectation is not None:
                return self._expectation
            if self._source is not None:
                self._expectation = self.lambda2eta(self._source)
                return self._expectation
            if self._natural is not None:
                self._expectation = self.theta2eta(self._natural)
                return self._expectation


class MultivariateGaussian(ExponentialFamily):
    def __init__(self, dim, **kwargs):
        self.dim = dim
        self._source_dtype = np.dtype([
                ("mu", (np.double, dim)),
                ("Sigma", (np.double, (dim, dim))),
                ])
        self._natural_dtype = np.dtype([
                ("theta", (np.double, dim)),
                ("Theta", (np.double, (dim, dim))),
                ])
        self._expectation_dtype = np.dtype([
                ("eta", (np.double, dim)),
                ("Eta", (np.double, (dim, dim))),
                ])

        ExponentialFamily.__init__(self, **kwargs)

    def mode(self):
        return self.source()['mu']

    def moment(self, order, centered=True, reduced=True):
        order = int(order)

        if centered or reduced or order >= 2:
            raise NotImplementedError

        if order == 1:
            return self.source()['mu']
        elif order == 2:
            return self.source()['Sigma']

    def lambda2theta(self, l):
        assert(l.dtype == self._source_dtype)

        t = np.empty(1, dtype=self._natural_dtype)
        inv_Sigma = inv(l['Sigma'])
        t['theta'][0] = dot(inv_Sigma, l['mu'])
        t['Theta'][0] = 0.5 * inv_Sigma

        return t[0]

    def theta2lambda(self, t):
        assert(t.dtype == self._natural_dtype)

        l = np.empty(1, dtype=self._source_dtype)

        inv_Theta = inv(t['Theta'])
        l['mu'][0] = 0.5 * dot(inv_Theta, t['theta'])
        l['Sigma'][0] = 0.5 * inv_Theta

        return l[0]

    def eta2lambda(self, e):
        """
        Converts expectation parameters to source parameters.
        """
        assert(e.dtype == self._expectation_dtype)

        l = np.empty(1, dtype=self._source_dtype)

        l['mu'][0] = e['eta']
        l['Sigma'][0] = - (e['Eta'] + outer(e['eta'], e['eta']))

        return l[0]

    def lambda2eta(self, l):
        """
        Converts source parameters to expectation parameters.
        """
        assert(l.dtype == self._source_dtype)

        e = np.empty(1, dtype=self._expectation_dtype)

        e['eta'][0] = l['mu']
        e['Eta'][0] = - (l['Sigma'] + outer(l['mu'], l['mu']))

        return e[0]

    def t(self, x):
        """
        Computes the sufficient statistic $ t(x) $.

        Parameter
        ---------
        x : n x dim array
            a point
        """
        assert(x.shape[1] == self.dim)
        n = x.shape[0]
        e = np.empty(n, dtype=self._expectation_dtype)

        eta = e['eta'].reshape(n, self.dim)
        eta[:] = x

        for i in xrange(n):
            e['Eta'][i] = - outer(x[i], x[i])

        return e

    def k(self, x):
        """
        Computes the carrier measure $ k(x) $
        """
        n = x.shape[0]
        return np.zeros(n)

    def F(self, t):
        assert(t.dtype == self._natural_dtype)

        theta = t['theta']
        Theta = t['Theta']

        r = (0.25 * dot(inv(Theta), outer(theta, theta)).trace() -
             0.5 * log(det(Theta)) + 0.5 * self.dim * log(pi))

        return r

    def gradF(self, t):
        assert(t.dtype == self._natural_dtype)

        grad = np.empty(1, dtype=self._expectation_dtype)

        theta = t['theta']
        Theta = t['Theta']

        inv_Theta = inv(Theta)
        Tt = dot(inv_Theta, theta)
        grad['eta'][0] = 0.5 * Tt
        grad['Eta'][0] = -0.5 * inv_Theta - 0.25 * outer(Tt, Tt)

        return grad[0]

    def G(self, e):
        assert(e.dtype == self._expectation_dtype)

        eta = e['eta']
        Eta = e['Eta']
        # if det(-Eta) <= 0:
        #     print "Eta", Eta
        #     print "det(-Eta)", det(-Eta)
        r = (- 0.5 * log(1.0 + dot(eta.T, dot(inv(Eta), eta))) -
             0.5 * log(det(-Eta)) - 0.5 * self.dim * log(2 * pi * exp(1.0)))

        return r

    def gradG(self, e):
        assert(e.dtype == self._expectation_dtype)

        grad = np.empty(1, dtype=self._natural_dtype)

        eta = e['eta']
        Eta = e['Eta']
        inv_EeeT = inv(Eta + outer(eta, eta))
        grad['theta'][0] = - dot(inv_EeeT, eta)
        grad['Theta'][0] = - 0.5 * inv_EeeT

        return grad[0]

    def density(self, x):
        source = self.source()

        d = self.dim
        mu = source['mu']
        Sigma = source['Sigma']
        inv_Sigma = inv(Sigma)

        r = (exp(-0.5 * dot((x - mu).T, dot(inv_Sigma, x - mu))) /
             ((2.0 * pi)**(d/2) * sqrt(det(Sigma))))

        return r

    def rand(self, size=1):
        source = self.source()
        return np.random.multivariate_normal(source['mu'], source['Sigma'],
                                             size)


def demo_multivariate():
    p = ([3.0, 12.0], [[5.0, 1.0], [1.0, 3.0]])
    gaussian = MultivariateGaussian(2)
    print gaussian

    print "\n* source", gaussian.source(p)
    gaussian._expectation = None
    gaussian._natural = None
    print "lambda2theta", gaussian.natural()
    gaussian._expectation = None
    gaussian._source = None
    print "theta2lambda", gaussian.source()

    print "\n* source", gaussian.source(p)
    gaussian._expectation = None
    gaussian._natural = None
    print "lambda2eta", gaussian.expectation()
    gaussian._natural = None
    gaussian._source = None
    print "eta2lambda", gaussian.source()

    gaussian.source(p)
    print "\n* natural", gaussian.natural()
    gaussian._source = None
    gaussian._expectation = None
    print "theta2eta", gaussian.expectation()
    gaussian._source = None
    gaussian._natural = None
    print "eta2theta", gaussian.natural()

    gaussian.source(p)
    from pylab import scatter, show
    data = gaussian.rand(10000)
    scatter(data[:, 0], data[:, 1])
    show()


class UnivariateGaussian(ExponentialFamily):
    dim = 1

    _source_dtype = np.dtype([
            ("mu", np.double),
            ("sigma^2", np.double),
            ])
    _natural_dtype = np.dtype([
            ("theta1", np.double),
            ("theta2", np.double),
            ])
    _expectation_dtype = np.dtype([
            ("eta1", np.double),
            ("eta2", np.double),
            ])

    def mode(self):
        return self.source()['mu']

    def moment(self, order, centered=True, reduced=True):
        order = int(order)

        if centered:
            sigma2 = self.source()['sigma^2']

            if order % 2:
                k = order / 2
                m = factorial(2*k) / (2**k * factorial(k))
                if reduced:
                    return m
                else:
                    return sigma2**2 * m
            else:
                return 0.0
        elif order == 1:
            return self.source()['mu']
        else:
            raise NotImplementedError

    def lambda2theta(self, l):
        assert(l.dtype is self._source_dtype)

        t = np.empty(1, dtype=self._natural_dtype)

        mu = l['mu']
        sigma = l['sigma^2']

        t['theta1'] = mu / sigma
        t['theta2'] = - 0.5 / sigma

        return t

    def theta2lambda(self, t):
        assert(t.dtype is self._natural_dtype)

        l = np.empty(1, dtype=self._source_dtype)

        l['mu'] = - 0.5 * t['theta1'] / t['theta2']
        l["sigma^2"] = - 0.5 / t['theta2']

        return l

    def eta2lambda(self, e):
        assert(e.dtype is self._expectation_dtype)

        l = np.empty(1, dtype=self._source_dtype)

        l['mu'] = e['eta1']
        l["sigma^2"] = e['eta2'] - e['eta1']**2

        return l

    def lambda2eta(self, l):
        assert(l.dtype is self._source_dtype)

        e = np.empty(1, dtype=self._expectation_dtype)

        e['eta1'] = l['mu']
        e['eta2'] = l['mu']**2 + l["sigma^2"]

        return e

    def t(self, x):
        n = x.shape[0]
        e = np.empty(n, dtype=self._expectation_dtype)
        e['eta1'] = x.reshape(n)
        e['eta2'] = (x**2).reshape(n)

        return e

    def k(self, x):
        n = x.shape[0]

        return np.zeros(n)

    def F(self, t):
        assert(t.dtype is self._natural_dtype)
        t2 = t['theta2']
        return -0.25 * t['theta1']**2 / t2 + 0.5 * log(-pi / t2)

    def gradF(self, t):
        assert(t.dtype is self._natural_dtype)
        t2 = t['theta2']
        grad = np.empty(t.shape, dtype=self._expectation_dtype)
        grad['eta1'] = -0.5 * t['theta1'] / t2
        grad['eta2'] = 0.25 * t['theta1']**2 / t2**2 - 0.5 / t2
        return grad

    def G(self, e):
        assert(e.dtype is self._expectation_dtype)

        return - 0.5 * log(e['eta2'] - e['eta1']**2)

    def gradG(self, e):
        assert(e.dtype is self._expectation_dtype)

        grad = np.empty(e.shape, dtype=self._natural_dtype)
        tmp = e['eta1']**2 - e['eta2']
        grad['theta1'] = - e['eta1'] / tmp
        grad['theta2'] = 0.5 / tmp

        return grad

    def density(self, x):
        source = self.source()
        mu = source['mu']
        sigma = source["sigma^2"]

        return exp(-(x-mu)**2 / (2.0 * sigma)) / (sqrt(2.0 * pi * sigma))

    def rand(self, size=1):
        source = self.source()
        return np.random.normal(source['mu'], source["sigma^2"], size)


def demo_univariate_gaussian():
    p = [(3.0, 5.0)]
    gaussian = UnivariateGaussian()
    print gaussian

    print "\n* source", gaussian.source(p)
    gaussian._expectation = None
    gaussian._natural = None
    print "lambda2theta", gaussian.natural()
    gaussian._expectation = None
    gaussian._source = None
    print "theta2lambda", gaussian.source()

    print "\n* source", gaussian.source(p)
    gaussian._expectation = None
    gaussian._natural = None
    print "lambda2eta", gaussian.expectation()
    gaussian._natural = None
    gaussian._source = None
    print "eta2lambda", gaussian.source()

    gaussian.source(p)
    print "\n* natural", gaussian.natural()
    gaussian._source = None
    gaussian._expectation = None
    print "theta2eta", gaussian.expectation()
    gaussian._source = None
    gaussian._natural = None
    print "eta2theta", gaussian.natural()

    gaussian.source(p)
    from pylab import hist, show
    hist(gaussian.rand(10000), 100)
    show()


class UnivariateGeneralizedGaussian(ExponentialFamily):
    dim = 1

    _source_dtype = np.dtype([
            ("alpha", np.double),
            ])
    _natural_dtype = np.dtype([
            ("theta1", np.double),
            ])
    _expectation_dtype = np.dtype([
            ("eta1", np.double),
            ])

    def __init__(self, beta=2., mu=0., **kwargs):
        self.beta = beta
        self.mu = mu
        ExponentialFamily.__init__(self, **kwargs)

    def __str__(self):
        return '{}({}, {})'.format(self.__class__.__name__, str(self.beta),
                                   str(self.mu))

    def mode(self):
        return self.mu

    def moment(self, order, centered=True, reduced=True):
        order = int(order)

        if centered:
            raise NotImplementedError
        elif order == 1:
            return self.mu
        else:
            raise NotImplementedError

    def lambda2theta(self, l):
        assert(l.dtype is self._source_dtype)

        t = np.empty(1, dtype=self._natural_dtype)

        t['theta1'] = 1.0 / l['alpha']

        return t

    def theta2lambda(self, t):
        assert(t.dtype is self._natural_dtype)

        l = np.empty(1, dtype=self._source_dtype)

        l['alpha'] = 1.0 / t['theta1']

        return l

    def t(self, x):
        n = x.shape[0]
        e = np.empty(n, dtype=self._expectation_dtype)

        beta = self.beta
        e['eta1'] = - np.abs(x.reshape(n))**beta

        return e

    def k(self, x):
        n = x.shape[0]

        return np.zeros(n)

    def F(self, t):
        assert(t.dtype is self._natural_dtype)

        beta = self.beta
        return - log(t['theta1']) - log(beta / (2.0 * gamma(1.0 / beta)))

    def gradF(self, t):
        assert(t.dtype is self._natural_dtype)

        grad = np.empty(t.shape, dtype=self._expectation_dtype)
        grad['eta1'] = - 1.0 / t['theta1']
        return grad

    def G(self, e):
        raise NotImplementedError
        assert(e.dtype is self._expectation_dtype)

        return None

    def gradG(self, e):
        raise NotImplementedError
        assert(e.dtype is self._expectation_dtype)

        return None

    def density(self, x):
        source = self.source()
        mu = self.mu
        alpha = source['alpha']
        beta = self.beta

        return (exp(-np.abs(x-mu)**beta / alpha) * beta /
                (2.0 * alpha * gamma(1/beta)))

    def rand(self, size=1):
        metropolis = Metropolis(self)
        return metropolis.draw(size)


def demo_univariate_generalized_gaussian():
    p = (3.0,)
    gg = UnivariateGeneralizedGaussian(0.1)
    print gg

    print "\n* source", gg.source(p)
    gg._expectation = None
    gg._natural = None
    print "lambda2theta", gg.natural()
    gg._expectation = None
    gg._source = None
    print "theta2lambda", gg.source()

    # print "\n* source", gg.source(p)
    # gg._expectation = None
    # gg._natural = None
    # print "lambda2eta", gg.expectation()
    # gg._natural = None
    # gg._source = None
    # print "eta2lambda", gg.source()

    # gg.source(p)
    # print "\n* natural", gg.natural()
    # gg._source = None
    # gg._expectation = None
    # print "theta2eta", gg.expectation()
    # gg._source = None
    # gg._natural = None
    # print "eta2theta", gg.natural()

    gg.source(p)
    from matplotlib import pyplot

    pyplot.subplot(2, 1, 1)
    a = np.arange(-20.0, 20.0, 0.2)
    pyplot.plot(a, gg(a))

    pyplot.subplot(2, 1, 2)
    pyplot.xlim(-20.0, 20.0)
    pyplot.hist(gg.rand(10000), 1000)
    pyplot.show()


if __name__ == "__main__":
    demo_multivariate()
    demo_univariate_gaussian()
    demo_univariate_generalized_gaussian()
