import numpy
import munkres
# from fastemd import emd_hat
from pyemd import emd as emd_hat
from ..divergence import KullbackLeibler as KLEF


class Munkres(object):
    def __init__(self, gd=None):
        self._gd = gd

    def __call__(self, p, q):
        assert(len(p) == len(q))
        assert(len(p) < 10000)
        gd = self._gd
        n = len(p)

        m = numpy.empty((n, n))

        for i in xrange(n):
            for j in xrange(n):
                m[i, j] = gd(p[i], q[j])

        transport = munkres.Munkres()
        # Munkres does not work with numpy arrays:
        path = transport.compute(m.tolist())
        cost = 0.0
        for row, column in path:
            cost += m[row][column]

        return cost


class FastEMD(object):
    def __init__(self, alpha=100000, gd=None):
        self._alpha = alpha
        self._gd = gd

    def __call__(self, p, q):
        assert(len(p) == len(q))
        assert(len(p) < 10000)
        gd = self._gd
        n = len(p)

        m = numpy.empty((n, n))

        for i in xrange(n):
            for j in xrange(n):
                m[i, j] = gd(p[i], q[j])

        cost = emd_hat(p.weights, q.weights, m, self._alpha, gd_metric=False)

        return cost


kl = KLEF()


def gd_majkl(wp, p, wq, q):
    return wp * (numpy.log(wp / wq) + kl(p, q))


class MajKL:
    def __call__(self, p, q):
        assert(len(p) == len(q))
        assert(len(p) < 10000)
        n = len(p)

        m = numpy.empty((n, n))

        for i in xrange(n):
            for j in xrange(n):
                m[i, j] = gd_majkl(p.weights[i], p[i], q.weights[j], q[j])

        transport = munkres.Munkres()
        # Munkres does not work with numpy arrays:
        path = transport.compute(m.tolist())
        cost = 0.0
        for row, column in path:
            cost += m[row][column]

        return cost

if __name__ == "__main__":
    from ..mixture_model import MixtureModel
    from ..families import UnivariateGaussian
    from ..divergence import KullbackLeibler

    d = Munkres(gd=KullbackLeibler())
    # d = FastEMD(gd=KullbackLeibler())
    # d = MajKL()

    mm1 = MixtureModel(8, UnivariateGaussian, ())
    mm1[0].source((9, 1))
    mm1[1].source((11, 1))
    mm1[2].source((19, 1))
    mm1[3].source((21, 1))
    mm1[4].source((29, 1))
    mm1[5].source((31, 1))
    mm1[6].source((39, 1))
    mm1[7].source((41, 1))
    print d(mm1, mm1)

    mm2 = MixtureModel(8, UnivariateGaussian, ())
    mm2[0].source((19, 1))
    mm2[1].source((31, 1))
    mm2[2].source((11, 1))
    mm2[3].source((39, 1))
    mm2[4].source((29, 1))
    mm2[5].source((9, 1))
    mm2[6].source((21, 1))
    mm2[7].source((41, 1))
    print d(mm1, mm2)

    mm3 = MixtureModel(8, UnivariateGaussian, ())
    mm3[0].source((4, 1))
    mm3[1].source((11, 1))
    mm3[2].source((19, 1))
    mm3[3].source((21, 1))
    mm3[4].source((29, 1))
    mm3[5].source((31, 1))
    mm3[6].source((39, 1))
    mm3[7].source((41, 1))
    print d(mm1, mm3)

    mm4 = MixtureModel(8, UnivariateGaussian, ())
    mm4[0].source((9, 1.2))
    mm4[1].source((11, 1))
    mm4[2].source((19, 4))
    mm4[3].source((21, 5))
    mm4[4].source((29, 1))
    mm4[5].source((31, 12))
    mm4[6].source((39, 9))
    mm4[7].source((41, 0.5))
    print d(mm1, mm4)

    mm5 = MixtureModel(8, UnivariateGaussian, ())
    mm5[0].source((9.2, 1))
    mm5[1].source((11.5, 1))
    mm5[2].source((18, 1))
    mm5[3].source((23, 1))
    mm5[4].source((27, 1))
    mm5[5].source((30.5, 1))
    mm5[6].source((39.1, 1))
    mm5[7].source((40.9, 1))
    print d(mm1, mm5)

    mm6 = MixtureModel(8, UnivariateGaussian, ())
    mm6[0].source((100, 1))
    mm6[1].source((11.5, 1))
    mm6[2].source((18, 1))
    mm6[3].source((31, 1))
    mm6[4].source((9, 1))
    mm6[5].source((30, 1))
    mm6[6].source((55, 1))
    mm6[7].source((40, 1))
    print d(mm1, mm6)
