#!/usr/bin/env python
""" generated source for module BregmanHardClustering """
from __future__ import print_function
# package: jMEF
# 
#  * @author  Vincent Garcia
#  * @author  Frank Nielsen
#  * @version 1.0
#  *
#  * @section License
#  * 
#  * See file LICENSE.txt
#  *
#  * @section Description
#  * 
#  * The Bregman hard clustering is the generalization of the hard clustering (also know as k-means) towards the exponential family.
#  * Given a set of weighted distributions (mixture model), the Bregman hard clustering partition the set into a determined number of classes.
#  * The centroid of each class is a weighted distribution. As a consequence, this algorithm simplifies a mixture model.
#  
class BregmanHardClustering(object):
    """ generated source for class BregmanHardClustering """
    # 
    # 	 * Maximum number of iterations permitted.
    # 	 
    MAX_ITERATIONS = 30

    # 
    # 	 * Simplifies a mixture model f into a mixture model g of m components using Bregman hard clustering algorithm.
    # 	 * @param   f           initial mixture model
    # 	 * @param   m           number of components in g
    # 	 * @param   type        type of the Bregman divergence used (right-sided, left-sided, or symmetric)
    # 	 * @param   iterations  maximum number of iterations allowed
    # 	 * @return              simplified mixture model g of m components
    # 	 
    @classmethod
    @overloaded
    def simplify(cls, f, m, type_, iterations):
        """ generated source for method simplify """
        cls.MAX_ITERATIONS = iterations
        return cls.simplify(f, m, type_)

    # 
    # 	 * Simplifies a mixture model f into a mixture model g of m components using Bregman hard clustering algorithm.
    # 	 * @param   f     initial mixture model
    # 	 * @param   m     number of components in g
    # 	 * @param   type  type of the Bregman divergence used (right-sided, left-sided, or symmetric)
    # 	 * @return        simplified mixture model g of m components
    # 	 
    @classmethod
    @simplify.register(object, MixtureModel, int, Clustering.CLUSTERING_TYPE)
    def simplify_0(cls, f, m, type_):
        """ generated source for method simplify_0 """
        #  Initialization
        fT = mixtureL2T(f)
        gT = initialize(fT, m, type_)
        # MixtureModel gT = initialize2(fT, m);
        #  Batch k-means
        repartition = [None] * fT.size
        batchKMeans(fT, gT, type_, repartition)
        #  Return
        return mixtureT2L(gT)

    # 
    # 	 * Simplifies a mixture model f into a mixture model g of m components using Bregman hard clustering algorithm.
    # 	 * @param   f     initial mixture model
    # 	 * @param   g     initialization of the mixture model g
    # 	 * @param   type  type of the Bregman divergence used (right-sided, left-sided, or symmetric)
    # 	 * @return        simplified mixture model g of m components
    # 	 
    @classmethod
    @simplify.register(object, MixtureModel, MixtureModel, Clustering.CLUSTERING_TYPE)
    def simplify_1(cls, f, g, type_):
        """ generated source for method simplify_1 """
        #  Initialization
        fT = mixtureL2T(f)
        gT = mixtureL2T(g)
        #  Batch k-means
        repartition = [None] * fT.size
        batchKMeans(fT, gT, type_, repartition)
        #  Return
        return mixtureT2L(gT)

    # 
    # 	 * Converts a mixture model from source parameters to natural parameters.
    # 	 * @param   fL  mixture model given in source parameters
    # 	 * @return      mixture model given in natural parameters
    # 	 
    @classmethod
    def mixtureL2T(cls, fL):
        """ generated source for method mixtureL2T """
        size = fL.size
        fTheta = MixtureModel(size)
        fTheta.EF = fL.EF
        i = 0
        while i < size:
            fTheta.weight[i] = fL.weight[i]
            fTheta.param[i] = fL.EF.Lambda2Theta(fL.param[i])
            fTheta.param[i].type_ = Parameter.TYPE.NATURAL_PARAMETER
            i += 1
        return fTheta

    @classmethod
    def mixtureT2L(cls, fT):
        """ generated source for method mixtureT2L """
        size = fT.size
        fLambda = MixtureModel(size)
        fLambda.EF = fT.EF
        i = 0
        while i < size:
            fLambda.weight[i] = fT.weight[i]
            fLambda.param[i] = fT.EF.Theta2Lambda(fT.param[i])
            fLambda.param[i].type_ = Parameter.TYPE.SOURCE_PARAMETER
            i += 1
        return fLambda

    @classmethod
    def initialize2(cls, f, m):
        """ generated source for method initialize2 """
        g = MixtureModel(m)
        g.EF = f.EF
        i = 0
        while i < m:
            g.weight[i] = f.weight[i]
            g.param[i] = f.param[i]
            g.param[i].type_ = f.param[i].type_
            i += 1
        g.normalizeWeights()
        return g

    @classmethod
    def initialize(cls, f, m, type_):
        """ generated source for method initialize """
        n = f.size
        i = int()
        j = int()
        g = MixtureModel(m)
        g.EF = f.EF
        rand = Random()
        kld_mat = [None] * m
        gau = [None] * n
        while i < n:
            pass
            i += 1
        index = rand.nextInt(n)
        g.weight[0] = f.weight[index]
        g.param[0] = f.param[index]
        gau[index] = 1
        while i < n:
            if type_ == CLUSTERING_TYPE.RIGHT_SIDED:
                kld_mat[0][i] = f.EF.BD(f.param[i], g.param[0])
            elif type_ == CLUSTERING_TYPE.LEFT_SIDED:
                kld_mat[0][i] = f.EF.BD(g.param[0], f.param[i])
            elif type_ == CLUSTERING_TYPE.SYMMETRIC:
                kld_mat[0][i] = 0.5 * (f.EF.BD(f.param[i], g.param[0]) + f.EF.BD(g.param[0], f.param[i]))
            i += 1
        row = 1
        while row < m:
            kld_min = [None] * n
            idx = [None] * n
            while i < n:
                min = Double.MAX_VALUE
                while j < row:
                    pass
                    j += 1
                kld_min[i] = min
                idx[i] = i
                i += 1
            Quicksort.quicksort(kld_min, idx)
            kld_cdf = [None] * n
            cdf = 0
            while i < n:
                cdf += kld_min[i]
                kld_cdf[i] = cdf
                i += 1
            cdf_min = 0
            while i < n:
                pass
                i += 1
            value = rand.nextDouble() * (kld_cdf[n - 1] - cdf_min) + cdf_min
            index = -1
            while i < n:
                if gau[idx[i]] == 0 and (kld_cdf[i] < value or index == -1):
                    index = idx[i]
                elif kld_cdf[i] >= value:
                    break
                i += 1
            g.weight[row] = f.weight[index]
            g.param[row] = f.param[index]
            gau[index] = 1
            while i < n:
                if type_ == CLUSTERING_TYPE.RIGHT_SIDED:
                    kld_mat[row][i] = f.EF.BD(f.param[i], g.param[row])
                elif type_ == CLUSTERING_TYPE.LEFT_SIDED:
                    kld_mat[row][i] = f.EF.BD(g.param[row], f.param[i])
                elif type_ == CLUSTERING_TYPE.SYMMETRIC:
                    kld_mat[row][i] = 0.5 * (f.EF.BD(f.param[i], g.param[row]) + f.EF.BD(g.param[row], f.param[i]))
                i += 1
            row += 1
        g.normalizeWeights()
        return g

    @classmethod
    def batchKMeans(cls, f, g, type_, repartition):
        """ generated source for method batchKMeans """
        repartition_old = [None] * f.size
        iterations = 0
        while True:
            repartition_old = repartition.clone()
            computeRepartition(f, g, type_, repartition)
            computeCentroids(f, g, type_, repartition)
            iterations += 1
            if not ((not Arrays == repartition, repartition_old and iterations < cls.MAX_ITERATIONS)):
                break

    @classmethod
    def incrementalKMeans(cls, f, g, type_, repartition):
        """ generated source for method incrementalKMeans """
        cond = False
        iterations = 0
        lf_init = getLossFunction(f, g, type_)
        lf_min = lf_init
        n = f.size
        m = g.size
        i = int()
        rep_opt = [None] * n
        g_tmp = MixtureModel(m)
        count = [None] * m
        while i < n:
            pass
            i += 1
        while i < n:
            rep_tmp = Arrays.copyOf(repartition, n)
            cl = repartition[i]
            if count[cl] > 1:
                j = 0
                while j < m:
                    if j != cl:
                        rep_tmp[i] = j
                        computeCentroids(f, g_tmp, type_, rep_tmp)
                        lf = getLossFunction(f, g_tmp, type_)
                        if lf < lf_min:
                            lf_min = lf
                            rep_opt = Arrays.copyOf(rep_tmp, n)
                            iterations += 1
                            print(lf_min)
                    j += 1
            i += 1
        if (lf_min / lf_init) < 0.98:
            cond = True
            while i < n:
                pass
                i += 1
            computeCentroids(f, g, type_, repartition)
            print("--> " + getLossFunction(f, g, type_))
        return cond

    @classmethod
    def computeRepartition(cls, f, g, type_, repartition):
        """ generated source for method computeRepartition """
        n = f.size
        m = g.size
        i = 0
        while i < n:
            index = -1
            d_min = Double.MAX_VALUE
            j = 0
            while j < m:
                d = 0
                if type_ == CLUSTERING_TYPE.RIGHT_SIDED:
                    d = f.EF.BD(f.param[i], g.param[j])
                elif type_ == CLUSTERING_TYPE.LEFT_SIDED:
                    d = f.EF.BD(g.param[j], f.param[i])
                elif type_ == CLUSTERING_TYPE.SYMMETRIC:
                    d = 0.5 * (f.EF.BD(f.param[i], g.param[j]) + f.EF.BD(g.param[j], f.param[i]))
                if d < d_min:
                    d_min = d
                    index = j
                j += 1
            repartition[i] = index
            i += 1

    @classmethod
    def computeCentroids(cls, f, g, type_, repartition):
        """ generated source for method computeCentroids """
        n = f.size
        m = g.size
        i = int()
        j = int()
        count = [None] * m
        while i < n:
            pass
            i += 1
        while i < m:
            if count[i] == 0:
                g.param[i] = None
                g.weight[i] = 0
                System.err.printf("The class %d is empty. Impossible to compute the centroid.", i)
            elif count[i] == 1:
                while j < n:
                    if repartition[j] == i:
                        g.param[i] = f.param[j]
                        g.weight[i] = f.weight[j]
                        break
                    j += 1
            else:
                mix = MixtureModel(count[i])
                mix.EF = f.EF
                ind = 0
                sum = 0
                while j < n:
                    if repartition[j] == i:
                        mix.weight[ind] = f.weight[j]
                        mix.param[ind] = f.param[j]
                        sum += f.weight[j]
                        ind += 1
                    j += 1
                mix.normalizeWeights()
                g.param[i] = Clustering.getCentroid(mix, type_)
                g.weight[i] = sum
            i += 1

    @classmethod
    def getLossFunction(cls, f, g, type_):
        """ generated source for method getLossFunction """
        n = f.size
        m = g.size
        value = 0
        i = 0
        while i < n:
            min = Double.MAX_VALUE
            j = 0
            while j < m:
                if type_ == CLUSTERING_TYPE.RIGHT_SIDED:
                    min = f.EF.BD(f.param[i], g.param[j])
                elif type_ == CLUSTERING_TYPE.LEFT_SIDED:
                    min = f.EF.BD(g.param[j], f.param[i])
                elif type_ == CLUSTERING_TYPE.SYMMETRIC:
                    min = 0.5 * (f.EF.BD(f.param[i], g.param[j]) + f.EF.BD(g.param[j], f.param[i]))
                j += 1
            value += min
            i += 1
        return value

