#!/usr/bin/env python
""" generated source for module Tutorial1 """
from __future__ import print_function
# package: Tutorials
class Tutorial1(object):
    """ generated source for class Tutorial1 """
    # 
    # 	 * Converts valid points (>0) to integer.
    # 	 * @param   points  point set in \f$R^d\f$.
    # 	 * @return          a point set in \f$N^d\f$.
    # 	 
    @classmethod
    def checkPoints(cls, points):
        """ generated source for method checkPoints """
        #  Count how many point are >0
        n = 0
        i = 0
        while len(points):
            pass
            i += 1
        #  Convert valid points as integer
        new_points = [None] * n
        idx = 0
        i = 0
        while len(points):
            pass
            i += 1
        return new_points

    # 
    # 	 * Compute the NMI.
    # 	 * @param  points  set of points
    # 	 * @param  f       initial mixture model
    # 	 * @param  g       estimated mixture model
    # 	 * @return         NMI
    # 	 
    @classmethod
    def NMI(cls, points, f, g):
        """ generated source for method NMI """
        m = int()
        n = f.size
        p = [None] * n
        i = 0
        while i < m:
            f_label = 0
            g_label = 0
            f_max = 0
            g_max = 0
            j = 0
            while j < n:
                f_tmp = f.weight[j] * f.EF.density(points[i], f.param[j])
                g_tmp = g.weight[j] * g.EF.density(points[i], g.param[j])
                if f_tmp > f_max:
                    f_max = f_tmp
                    f_label = j
                if g_tmp > g_max:
                    g_max = g_tmp
                    g_label = j
                j += 1
            p[f_label][g_label] += 1
            i += 1
        i = 0
        while i < n:
            pass
            i += 1
        fl = [None] * n
        gl = [None] * n
        i = 0
        while i < n:
            f_sum = 0
            g_sum = 0
            j = 0
            while j < n:
                f_sum += p[i][j]
                g_sum += p[j][i]
                j += 1
            fl[i] = f_sum
            gl[i] = g_sum
            i += 1
        mi = 0
        i = 0
        while i < n:
            pass
            i += 1
        hf = 0
        hg = 0
        i = 0
        while i < n:
            hf += fl[i] * log(fl[i])
            hg += gl[i] * log(gl[i])
            i += 1
        nmi = mi / sqrt(hf * hg)
        return nmi

    @classmethod
    def testGaussian(cls, m):
        """ generated source for method testGaussian """
        out = [None] * 3
        f = MixtureModel(3)
        f.EF = UnivariateGaussianFixedVariance(25)
        f.weight[0] = 1.0 / 3.0
        f.weight[1] = 1.0 / 3.0
        f.weight[2] = 1.0 / 3.0
        p1 = PVector(1)
        p2 = PVector(1)
        p3 = PVector(1)
        p1.array[0] = 10
        p2.array[0] = 20
        p3.array[0] = 40
        f.param[0] = p1
        f.param[1] = p2
        f.param[2] = p3
        points = f.drawRandomPoints(m)
        points = cls.checkPoints(points)
        clusters = KMeans.run(points, 3)
        mog = None
        mog = BregmanSoftClustering.initialize(clusters, UnivariateGaussianFixedVariance(25))
        mog = BregmanSoftClustering.run(points, mog)
        out[0] = cls.NMI(points, f, mog)
        mop = None
        mop = BregmanSoftClustering.initialize(clusters, Poisson())
        mop = BregmanSoftClustering.run(points, mop)
        out[1] = cls.NMI(points, f, mop)
        mob = None
        mob = BregmanSoftClustering.initialize(clusters, BinomialFixedN(100))
        mob = BregmanSoftClustering.run(points, mob)
        out[2] = cls.NMI(points, f, mob)
        return out

    @classmethod
    def testPoisson(cls, m):
        """ generated source for method testPoisson """
        out = [None] * 3
        f = MixtureModel(3)
        f.EF = Poisson()
        f.weight[0] = 1.0 / 3.0
        f.weight[1] = 1.0 / 3.0
        f.weight[2] = 1.0 / 3.0
        p1 = PVector(1)
        p2 = PVector(1)
        p3 = PVector(1)
        p1.array[0] = 10
        p2.array[0] = 20
        p3.array[0] = 40
        f.param[0] = p1
        f.param[1] = p2
        f.param[2] = p3
        points = f.drawRandomPoints(m)
        points = cls.checkPoints(points)
        clusters = KMeans.run(points, 3)
        mog = None
        mog = BregmanSoftClustering.initialize(clusters, UnivariateGaussianFixedVariance(25))
        mog = BregmanSoftClustering.run(points, mog)
        out[0] = cls.NMI(points, f, mog)
        mop = None
        mop = BregmanSoftClustering.initialize(clusters, Poisson())
        mop = BregmanSoftClustering.run(points, mop)
        out[1] = cls.NMI(points, f, mop)
        mob = None
        mob = BregmanSoftClustering.initialize(clusters, BinomialFixedN(100))
        mob = BregmanSoftClustering.run(points, mob)
        out[2] = cls.NMI(points, f, mob)
        return out

    @classmethod
    def testBinomial(cls, m):
        """ generated source for method testBinomial """
        out = [None] * 3
        f = MixtureModel(3)
        f.EF = BinomialFixedN(100)
        f.weight[0] = 1.0 / 3.0
        f.weight[1] = 1.0 / 3.0
        f.weight[2] = 1.0 / 3.0
        p1 = PVector(1)
        p2 = PVector(1)
        p3 = PVector(1)
        p1.array[0] = 0.1
        p2.array[0] = 0.2
        p3.array[0] = 0.4
        f.param[0] = p1
        f.param[1] = p2
        f.param[2] = p3
        points = f.drawRandomPoints(m)
        points = cls.checkPoints(points)
        clusters = KMeans.run(points, 3)
        mog = None
        mog = BregmanSoftClustering.initialize(clusters, UnivariateGaussianFixedVariance(25))
        mog = BregmanSoftClustering.run(points, mog)
        out[0] = cls.NMI(points, f, mog)
        mop = None
        mop = BregmanSoftClustering.initialize(clusters, Poisson())
        mop = BregmanSoftClustering.run(points, mop)
        out[1] = cls.NMI(points, f, mop)
        mob = None
        mob = BregmanSoftClustering.initialize(clusters, BinomialFixedN(100))
        mob = BregmanSoftClustering.run(points, mob)
        out[2] = cls.NMI(points, f, mob)
        return out

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        title = ""
        title += "+-------------------------+\n"
        title += "| Bregman soft clustering |\n"
        title += "+-------------------------+\n"
        print(title, end="")
        m = 1000
        loop = 100
        NMI_Gaussian = [None] * loop
        NMI_Poisson = [None] * loop
        NMI_Binomial = [None] * loop
        l = 0
        while l < loop:
            NMI_Gaussian[l] = cls.testGaussian(m)
            NMI_Poisson[l] = cls.testPoisson(m)
            NMI_Binomial[l] = cls.testBinomial(m)
            l += 1
        means = [None] * 3
        vars = [None] * 3
        i = 0
        while i < 3:
            gm = 0
            gv = 0
            pm = 0
            pv = 0
            bm = 0
            bv = 0
            l = 0
            while l < loop:
                tmpg = NMI_Gaussian[l][i]
                tmpp = NMI_Poisson[l][i]
                tmpb = NMI_Binomial[l][i]
                gm += tmpg
                pm += tmpp
                bm += tmpb
                gv += tmpg * tmpg
                pv += tmpp * tmpp
                bv += tmpb * tmpb
                l += 1
            gm /= loop
            pm /= loop
            bm /= loop
            gv = gv / loop - gm * gm
            pv = pv / loop - pm * pm
            bv = bv / loop - bm * bm
            means[0][i] = gm
            means[1][i] = pm
            means[2][i] = bm
            vars[0][i] = sqrt(gv)
            vars[1][i] = sqrt(pv)
            vars[2][i] = sqrt(bv)
            i += 1


if __name__ == '__main__':
    import sys
    Tutorial1.main(sys.argv)

