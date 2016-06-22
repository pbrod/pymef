#!/usr/bin/env python
""" generated source for module Tutorial2 """
from __future__ import print_function
# package: Tutorials
class Tutorial2(object):
    """ generated source for class Tutorial2 """
    # 
    # 	 * Main function.
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  Display
        title = ""
        title += "+----------------------------------------+\n"
        title += "| Bregman soft clustering & classical EM |\n"
        title += "+----------------------------------------+\n"
        print(title, end="")
        #  Variables
        n = 3
        m = 1000
        #  Initial mixture model
        mm = MixtureModel(n)
        mm.EF = UnivariateGaussian()
        i = 0
        while i < n:
            param = PVector(2)
            param.array[0] = 10 * (i + 1)
            param.array[1] = 2 * (i + 1)
            mm.param[i] = param
            mm.weight[i] = i + 1
            i += 1
        mm.normalizeWeights()
        print("Initial mixure model \n" + mm + "\n")
        #  Draw points from initial mixture model and compute the n clusters
        points = mm.drawRandomPoints(m)
        clusters = KMeans.run(points, n)
        #  Classical EM
        mmc = None
        mmc = ExpectationMaximization1D.initialize(clusters)
        mmc = ExpectationMaximization1D.run(points, mmc)
        print("Mixure model estimated using classical EM \n" + mmc + "\n")
        #  Bregman soft clustering
        mmef = None
        mmef = BregmanSoftClustering.initialize(clusters, UnivariateGaussian())
        mmef = BregmanSoftClustering.run(points, mmef)
        print("Mixure model estimated using Bregman soft clustering \n" + mmef + "\n")


if __name__ == '__main__':
    import sys
    Tutorial2.main(sys.argv)

