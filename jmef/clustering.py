#!/usr/bin/env python
""" generated source for module Clustering """
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
#  * This class provides the functions to compute the centroid of a mixture of exponential families.
#  * The centroid, depending on the non-symmetric Bregman divergence, can be:
#  *   - right-sided,
#  *   - left-sided,
#  *   - symmetric.
#  
class Clustering(object):
    """ generated source for class Clustering """
    # 
    # 	 * Type of the Bregman divergence used.
    # 	 
    class CLUSTERING_TYPE:
        """ generated source for enum CLUSTERING_TYPE """
        LEFT_SIDED = u'LEFT_SIDED'
        RIGHT_SIDED = u'RIGHT_SIDED'
        SYMMETRIC = u'SYMMETRIC'

    # 
    # 	 * Computes the center of mass (right-sided centroid) of a mixture model f.
    # 	 * @param   f  mixture model given in natural parameters
    # 	 * @return     center of mass of f
    # 	 
    @classmethod
    def getCenterOfMass(cls, f):
        """ generated source for method getCenterOfMass """
        centroid = f.param[0].Times(f.weight[0])
        sum = f.weight[0]
        i = 1
        while i < f.size:
            centroid = centroid.Plus(f.param[i].Times(f.weight[i]))
            sum += f.weight[i]
            i += 1
        return centroid.Times(1. / sum)

    @classmethod
    def getGeneralizedCentroid(cls, EF, f):
        """ generated source for method getGeneralizedCentroid """
        centroid = EF.gradF(f.param[0]).Times(f.weight[0])
        sum = f.weight[0]
        i = 1
        while i < f.size:
            centroid = centroid.Plus(EF.gradF(f.param[i]).Times(f.weight[i]))
            sum += f.weight[i]
            i += 1
        return EF.gradG(centroid.Times(1. / sum))

    @classmethod
    def getSymmetricCentroid(cls, EF, f):
        """ generated source for method getSymmetricCentroid """
        thetageodesic = None
        centroid = None
        thetaR = None
        thetaL = None
        thetaR = cls.getCenterOfMass(f)
        thetaL = cls.getGeneralizedCentroid(EF, f)
        l = float()
        lmin = 0.0
        lmax = 1.0
        while (lmax - lmin) > 1.0e-6:
            l = (lmin + lmax) / 2.0
            thetageodesic = EF.GeodesicPoint(thetaR, thetaL, l)
            if EF.BD(thetageodesic, thetaR) > EF.BD(thetaL, thetageodesic):
                lmax = l
            else:
                lmin = l
        l = (lmin + lmax) / 2.0
        centroid = EF.GeodesicPoint(thetaR, thetaL, l)
        return centroid

    @classmethod
    def getCentroid(cls, f, type_):
        """ generated source for method getCentroid """
        centroid = None
        if type_ == cls.CLUSTERING_TYPE.RIGHT_SIDED:
            centroid = Clustering.getCenterOfMass(f)
        elif type_ == cls.CLUSTERING_TYPE.LEFT_SIDED:
            centroid = Clustering.getGeneralizedCentroid(f.EF, f)
        else:
            centroid = Clustering.getSymmetricCentroid(f.EF, f)
        return centroid

