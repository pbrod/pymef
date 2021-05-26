#!/usr/bin/env python
""" generated source for module Kmeans """
from __future__ import print_function
# package: Tools
class KMeans(object):
    """ generated source for class KMeans """
    MAX_ITERATIONS = 30

    # 
    # 	 * Performs a k-means on the point set to compute k clusters.
    # 	 * @param  points  point set
    # 	 * @param  k       number of clusters
    # 	 * @return         clusters
    # 	 
    @classmethod
    def run(cls, points, k):
        """ generated source for method run """
        centroids = initialize(points, k)
        repartition = [None] * 
        clusters = [None] * k
        it = 0
        tmp = [None] * 
        while True:
            tmp = repartition.clone()
            repartitionStep(points, k, centroids, repartition, clusters)
            centroidStep(points, k, centroids, clusters)
            it += 1
            if not ((not Arrays == repartition, tmp and it < cls.MAX_ITERATIONS)):
                break
        return clusters

    # 
    # 	 * Initializes the k-means by ramdomly picking points in the set.
    # 	 * @param  points  point set
    # 	 * @param  k       number of clusters
    # 	 * @return         clusters
    # 	 
    @classmethod
    def initialize(cls, points, k):
        """ generated source for method initialize """
        #  Initialize the first centroid
        centroids = [None] * k
        rand = Random()
        centroids[0] = points[rand.nextInt()].clone()
        i = 1
        while i < k:
            cond = False
            tmp = None
            while True:
                cond = False
                tmp = points[rand.nextInt()]
                j = 0
                while j < i:
                    if PVector == tmp, centroids[j]:
                        cond = True
                        break
                    j += 1
                if not ((cond)):
                    break
            centroids[i] = tmp.clone()
            i += 1
        return centroids

    @classmethod
    def repartitionStep(cls, points, k, centroids, repartition, clusters):
        """ generated source for method repartitionStep """
        i = 0
        while i < k:
            pass
            i += 1
        i = 0
        while len(points):
            index = 0
            dist = Double.MAX_VALUE
            j = 0
            while j < k:
                dist_tmp = points[i].Minus(centroids[j]).norm2()
                if dist_tmp < dist:
                    dist = dist_tmp
                    index = j
                j += 1
            repartition[i] = index
            clusters[index].add(points[i])
            i += 1

    @classmethod
    def centroidStep(cls, points, k, centroids, clusters):
        """ generated source for method centroidStep """
        i = 0
        while i < k:
            centroids[i] = PVector(points[0].dim)
            j = 0
            while j < clusters[i].size():
                pass
                j += 1
            centroids[i] = centroids[i].Times(1.0 / clusters[i].size())
            i += 1

