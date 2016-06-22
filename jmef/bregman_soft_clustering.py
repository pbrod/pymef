#!/usr/bin/env python
""" generated source for module BregmanSoftClustering """
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
#  * The Bregman soft clustering is the generalization of the soft clustering (also know as expectation-maximization algorithm) towards the exponential family.
#  * Given a set of points, the Bregman soft clustering algorithm estimates the parameters of the mixture model for a chosen exponential family.
#  
class BregmanSoftClustering(object):
    """ generated source for class BregmanSoftClustering """
    # 
    # 	 * Maximum number of iterations permitted.
    # 	 
    MAX_ITERATIONS = 30

    # 
    # 	 * Initializes a mixture model from clusters of points, each cluster containing a set of points.
    # 	 * @param   clusters  clusters of points
    # 	 * @param   EF        exponential family member
    # 	 * @return            initialized mixture model
    # 	 
    @classmethod
    def initialize(cls, clusters, EF):
        """ generated source for method initialize """
        #  Mixture initialization
        mm = MixtureModel()
        mm.EF = EF
        #  Amount of points
        nb = 0
        i = 0
        while len(clusters):
            pass
            i += 1
        #  Loop on clusters
        i = 0
        while len(clusters):
            #  Weight
            mm.weight[i] = (float(clusters[i].size())) / nb
            param = EF.t(clusters[i].get(0))
            j = 1
            while j < clusters[i].size():
                pass
                j += 1
            param = param.Times(1.0 / clusters[i].size())
            mm.param[i] = mm.EF.Eta2Lambda(param)
            i += 1
        return mm

    @classmethod
    @overloaded
    def run(cls, pointSet, fL, iterations):
        """ generated source for method run """
        cls.MAX_ITERATIONS = iterations
        return cls.run(pointSet, fL)

    @classmethod
    @run.register(object, PVector, MixtureModel)
    def run_0(cls, pointSet, fL):
        """ generated source for method run_0 """
        col = int()
        row = int()
        n = fL.size
        m = int()
        iterations = 0
        fH = mixtureL2H(fL)
        logLikelihoodNew = logLikelihood(pointSet, fH)
        logLikelihoodThreshold = abs(logLikelihoodNew) * 0.01
        logLikelihoodOld = float()
        while True:
            logLikelihoodOld = logLikelihoodNew
            p = [None] * m
            while row < m:
                sum = 0
                while col < n:
                    tmp = fH.weight[col] * exp(fL.EF.G(fH.param[col]) + fL.EF.t(pointSet[row]).Minus(fH.param[col]).InnerProduct(fL.EF.gradG(fH.param[col])))
                    p[row][col] = tmp
                    sum += tmp
                    col += 1
                while col < n:
                    pass
                    col += 1
                row += 1
            while col < n:
                sum = p[0][col]
                fH.param[col] = fL.EF.t(pointSet[0]).Times(p[0][col])
                while row < m:
                    sum += p[row][col]
                    fH.param[col] = fH.param[col].Plus(fL.EF.t(pointSet[row]).Times(p[row][col]))
                    row += 1
                fH.weight[col] = sum / m
                fH.param[col] = fH.param[col].Times(1. / sum)
                fH.param[col].type_ = TYPE.EXPECTATION_PARAMETER
                col += 1
            iterations += 1
            logLikelihoodNew = logLikelihood(pointSet, fH)
            if not ((iterations < cls.MAX_ITERATIONS and abs(logLikelihoodOld - logLikelihoodNew) > logLikelihoodThreshold)):
                break
        return mixtureH2L(fH)

    @classmethod
    def mixtureL2H(cls, fL):
        """ generated source for method mixtureL2H """
        size = fL.size
        fH = MixtureModel(size)
        fH.EF = fL.EF
        i = 0
        while i < size:
            fH.weight[i] = fL.weight[i]
            fH.param[i] = fL.EF.Theta2Eta(fL.EF.Lambda2Theta(fL.param[i]))
            i += 1
        return fH

    @classmethod
    def mixtureH2L(cls, fH):
        """ generated source for method mixtureH2L """
        size = fH.size
        fL = MixtureModel(size)
        fL.EF = fH.EF
        i = 0
        while i < size:
            fL.weight[i] = fH.weight[i]
            fL.param[i] = fH.EF.Theta2Lambda(fH.EF.Eta2Theta(fH.param[i]))
            i += 1
        return fL

    @classmethod
    def logLikelihood(cls, points, f):
        """ generated source for method logLikelihood """
        value = 0
        i = 0
        while len(points):
            pass
            i += 1
        return value

