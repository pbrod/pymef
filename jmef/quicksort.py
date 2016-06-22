#!/usr/bin/env python
""" generated source for module Quicksort """
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
#  * The Quicksort class implements the quicksort algorithm.
#  
class Quicksort(object):
    """ generated source for class Quicksort """
    # 
    # 	 * Sorts an array using quicksort algorithm.
    # 	 * @param  data   array to be sorted
    # 	 * @param  index  initial position (index) of the sorted elements
    # 	 
    @classmethod
    @overloaded
    def quicksort(cls, data, index):
        """ generated source for method quicksort """
        shuffle(data, index)
        #  to guard against worst-case
        cls.quicksort(data, index, 0, len(data))

    # 
    # 	 * Sorts the left and the right parts of an array using recursive quicksort algorithm.
    # 	 * @param  a     array to be sorted
    # 	 * @param  idx   index
    # 	 * @param  left  left index: sort between left to idx
    # 	 * @param  right right index: sort between idx to right
    # 	 
    @classmethod
    @quicksort.register(object, float, int, int, int)
    def quicksort_0(cls, a, idx, left, right):
        """ generated source for method quicksort_0 """
        if right <= left:
            return
        i = partition(a, idx, left, right)
        cls.quicksort(a, idx, left, i - 1)
        cls.quicksort(a, idx, i + 1, right)

    # 
    # 	 * Creates the partition.
    # 	 * @param  a     array to be sorted
    # 	 * @param  idx   array of indexes
    # 	 * @param  left  left index: sort between left to i
    # 	 * @param  right right index: sort between i to right
    # 	 
    @classmethod
    def partition(cls, a, idx, left, right):
        """ generated source for method partition """
        i = left - 1
        j = right
        i += 1
        j -= 1
        while True:
            while a[i] < a[right]:
                pass
            #  find item on left to swap
            #  a[right] acts as sentinel
            while a[right] < a[j]:
                #  find item on right to swap
                if j == left:
                    break
            #  don't go out-of-bounds
            if i >= j:
                break
            #  check if pointers cross
            exch(a, idx, i, j)
            #  swap two elements into place
        exch(a, idx, i, right)
        #  swap with partition element
        return i

    # 
    # 	 * Switches the the values a[i] and a[j] and the indexes idx[i] and idx[j].
    # 	 * @param  a     array to be sorted
    # 	 * @param  idx   array of indexes
    # 	 * @param  i     index
    # 	 * @param  j     index
    # 	 
    @classmethod
    def exch(cls, a, idx, i, j):
        """ generated source for method exch """
        swap = a[i]
        a[i] = a[j]
        a[j] = swap
        swap2 = idx[i]
        idx[i] = idx[j]
        idx[j] = swap2

    # 
    # 	 * Shuffles the array a
    # 	 * @param  a     array to be sorted
    # 	 * @param  idx   array of indexes
    # 	 
    @classmethod
    def shuffle(cls, a, idx):
        """ generated source for method shuffle """
        N = int()
        i = 0
        while i < N:
            r = i + int((random() * (N - i)))
            #  between i and N-1
            cls.exch(a, idx, i, r)
            i += 1

