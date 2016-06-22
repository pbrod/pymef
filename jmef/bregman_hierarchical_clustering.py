#!/usr/bin/env python
""" generated source for module BregmanHierarchicalClustering """
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
#  * The Bregman hierarchical clustering is the generalization of the hierarchical clustering towards the exponential family.
#  * Given a set of weighted distributions (mixture model), the Bregman hierarchical clustering builds a hierarchical mixture model (class HierarchicalMixtureModel).
#  * It is then possible from this hierarchical mixture model to
#  *   - quickly deduce a simpler mixture model,
#  *   - automatically learn the "optimal" number of components in the mixture model.
#  
class BregmanHierarchicalClustering(object):
    """ generated source for class BregmanHierarchicalClustering """
    # 
    # 	 * Type of the likage criterion used.
    # 	 
    class LINKAGE_CRITERION:
        """ generated source for enum LINKAGE_CRITERION """
        MINIMUM_DISTANCE = u'MINIMUM_DISTANCE'
        MAXIMUM_DISTANCE = u'MAXIMUM_DISTANCE'
        AVERAGE_DISTANCE = u'AVERAGE_DISTANCE'

    # 
    # 	 * Builds a hierarchical mixture model (class HierarchicalMixtureModel) from an input mixture model and a clustering type.
    # 	 * @param  f        input mixture model given in source parameters
    # 	 * @param  type     type of the Bregman divergence used: right-sided, left-sided, or symmetric
    # 	 * @param  linkage  linkage criterion used: minimum, maximum, or average distance
    # 	 * @return          a hierarchical mixture model
    # 	 
    @classmethod
    def build(cls, f, type_, linkage):
        """ generated source for method build """
        #  Variables
        i = int()
        j = int()
        n = f.size
        fT = mixtureL2T(f)
        hmm_array = [None] * n
        #  Build the array, each case containing a hierarchical mixture model with one parameter
        while i < n:
            mm = MixtureModel(1)
            mm.EF = fT.EF
            mm.param[0] = fT.param[i]
            mm.weight[0] = 1.0
            hmm = HierarchicalMixtureModel()
            hmm.EF = fT.EF
            hmm.weight = fT.weight[i]
            hmm.node = mm
            hmm.type_ = type_
            hmm.resolutionMax = 1
            hmm_array[i] = hmm
            i += 1
        #  General loop
        while i < n - 1:
            #  Temporary array containing new hierarchical mixture models
            hmm_array_new = [None] * n - i - 1
            #  Find two closest hierarchical mixture models in the array
            index = find2ClosestMixtureModels(hmm_array, type_, linkage)
            #  Fusion the two closest hierarchical mixture models in a new one
            hmm = None
            hmm_1 = None
            hmm_2 = None
            mm = None
            mm_1 = None
            mm_2 = None
            hmm_1 = hmm_array[index[0]]
            hmm_2 = hmm_array[index[1]]
            mm_1 = hmm_1.node
            mm_2 = hmm_2.node
            mm = MixtureModel(mm_1.size + mm_2.size)
            mm.EF = mm_1.EF
            while j < mm_1.size:
                mm.param[j] = mm_1.param[j]
                mm.weight[j] = mm_1.weight[j] * hmm_1.weight
                j += 1
            while j < mm_2.size:
                mm.param[mm_1.size + j] = mm_2.param[j]
                mm.weight[mm_1.size + j] = mm_2.weight[j] * hmm_2.weight
                j += 1
            mm.normalizeWeights()
            hmm = HierarchicalMixtureModel()
            hmm.EF = mm_1.EF
            hmm.weight = hmm_1.weight + hmm_2.weight
            hmm.node = mm
            hmm.leftChild = hmm_1
            hmm.rightChild = hmm_2
            hmm.type_ = hmm_1.type_
            hmm.resolutionMax = hmm_1.resolutionMax + 1
            hmm_1.parent = hmm
            hmm_2.parent = hmm
            hmm_array_new[0] = hmm
            #  Copy other hierarchical mixture models in the temporary array
            cpt = 1
            while j < n - i:
                if j != index[0] and j != index[1]:
                    hmm_current = hmm_array[j]
                    hmm_new = HierarchicalMixtureModel()
                    hmm_new.EF = hmm_current.EF
                    hmm_new.node = hmm_current.node
                    hmm_new.weight = hmm_current.weight
                    hmm_new.leftChild = hmm_current
                    hmm_new.type_ = hmm_current.type_
                    hmm_new.resolutionMax = hmm_current.resolutionMax + 1
                    hmm_current.parent = hmm_new
                    hmm_array_new[cpt] = hmm_new
                    cpt += 1
                j += 1
            #  Remplace the array by the temporary array
            hmm_array = hmm_array_new
            i += 1
        #  Return the root of the hierarchical mixture model
        return hmm_array[0]

    # 
    # 	 * Finds the two closest hierarchical mixture model relatively to a Bregman divergence type.	
    # 	 * @param hmmArray    array of hierarchical mixture models
    # 	 * @param type        type of the Bregman divergence used: right-sided, left-sided, or symmetric
    # 	 * @param linkage     linkage criterion used: minimum, maximum, or average distance
    # 	 * return             indexes of the two closest hierarchical mixture models
    # 	 
    @classmethod
    def find2ClosestMixtureModels(cls, hmmArray, type_, linkage):
        """ generated source for method find2ClosestMixtureModels """
        #  Variable
        index = [None] * 2
        n = int()
        dmin = Double.MAX_VALUE
        #  Loops
        i = 0
        while i < n:
            pass
            i += 1
        #  Current mixture models
        #  Distance (min, max, or mean) between the two mixture models
        #  Remember the indexes
        #  Return the indexes
        return index

    # 
    # 	 * Computes the min-distance between two mixture models relatively to a Bregman divergence type
    # 	 * @param mm1    mixture model
    # 	 * @param mm2    mixture model
    # 	 * @param type   type of the Bregman divergence used: right-sided, left-sided, or symmetric
    # 	 * @return       min-distance between mm1 and mm2
    # 	 
    @classmethod
    def computeMinDistance(cls, mm1, mm2, type_):
        """ generated source for method computeMinDistance """
        d = Double.MAX_VALUE
        i = 0
        while i < mm1.size:
            pass
            i += 1
        return d

    # 
    # 	 * Computes the max-distance between two mixture models relatively to a Bregman divergence type
    # 	 * @param mm1    mixture model
    # 	 * @param mm2    mixture model
    # 	 * @param type   type of the Bregman divergence used: right-sided, left-sided, or symmetric
    # 	 * @return       max-distance between mm1 and mm2
    # 	 
    @classmethod
    def computeMaxDistance(cls, mm1, mm2, type_):
        """ generated source for method computeMaxDistance """
        d = 0
        i = 0
        while i < mm1.size:
            pass
            i += 1
        return d

    # 
    # 	 * Computes the mean-distance between two mixture models relatively to a Bregman divergence type
    # 	 * @param mm1    first mixture model
    # 	 * @param mm2    second mixture model
    # 	 * @param type   type of the Bregman divergence used: right-sided, left-sided, or symmetric
    # 	 * @return       mean-distance between mm1 and mm2
    # 	 
    @classmethod
    def computeAverageDistance(cls, mm1, mm2, type_):
        """ generated source for method computeAverageDistance """
        d = 0
        i = 0
        while i < mm1.size:
            pass
            i += 1
        return d / (mm1.size * mm2.size)

    # 
    # 	 * Converts a mixture from source parameters to natural parameters.
    # 	 * @param   fL  mixture model given in source parameters
    # 	 * @return      mixture model given in natural parameters
    # 	 
    @classmethod
    def mixtureL2T(cls, fLambda):
        """ generated source for method mixtureL2T """
        size = fLambda.size
        fTheta = MixtureModel(size)
        fTheta.EF = fLambda.EF
        i = 0
        while i < size:
            fTheta.weight[i] = fLambda.weight[i]
            fTheta.param[i] = fLambda.EF.Lambda2Theta(fLambda.param[i])
            fTheta.param[i].type_ = Parameter.TYPE.NATURAL_PARAMETER
            i += 1
        return fTheta

