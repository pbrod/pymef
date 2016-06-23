
import numpy as np
from numpy.random import uniform


class Metropolis(object):
    def __init__(self, ef):
        self._ef = ef
        self._alpha = 10.0

    def __call__(self, n):
        return self.draw(n)

    def draw(self, n):
        alpha = self._alpha
        pdf = self._ef.pdf
        dim = self._ef.dim
        points = np.empty((n, dim))
        count = 0

        x0 = self._ef.mean()
        while count < n:
            x = uniform(x0-alpha, x0+alpha)
            u = uniform(0.0, 1.0)

            a = pdf(x) / pdf(x0)
            if u < a:
                points[count] = x
                x0 = x
                count += 1

        return points


def demo_metropolis_gaussian():
    from .families import UnivariateGaussian

    gaussian = UnivariateGaussian()
    gaussian.source((3.0, 5.0))

    metropolis = Metropolis(gaussian)
    data = metropolis(10000)

    print np.mean(data), np.var(data)

    from pylab import hist, show
    hist(data, 100)
    show()


def demo_metropolis_multivariate():
    from .families import MultivariateGaussian

    gaussian = MultivariateGaussian(2)
    gaussian.source(([3.0, 12.0], [[5.0, 1.0], [1.0, 3.0]]))

    metropolis = Metropolis(gaussian)
    data = metropolis(10000)

    print np.mean(data, 0), np.cov(data, rowvar=0)

    from pylab import scatter, show
    data = gaussian.rand(10000)
    scatter(data[:, 0], data[:, 1])
    show()


if __name__ == "__main__":
    demo_metropolis_gaussian()
    demo_metropolis_multivariate()
