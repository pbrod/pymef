from numpy import maximum, log


class KullbackLeibler:
    def __init__(self, count=10000):
        self._count = count

    def __call__(self, mm1, mm2, points=None):
        if points is None:
            points = mm1.rand(self._count)
            count = self._count
        else:
            count = points.shape[0]
        eps = 10e-100

        dist = (log(maximum(eps, mm1(points))) -
                log(maximum(eps, mm2(points)))).sum()
        return max(0., dist / float(count))

if __name__ == "__main__":
    from ..mixture_model import MixtureModel
    from ..families import UnivariateGaussian

    d = KullbackLeibler()

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
