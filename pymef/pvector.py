#!/usr/bin/env python
""" generated source for module Pvector """
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
#  * A statistical distribution is parameterized by a set of values (parameters).
#  * The PVector class implements a parameter object.
#  * Parameters are represented as a vector.
#  
class PVector(Parameter):
    """ generated source for class PVector """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Dimension of the vector.
    # 	 
    dim = int()

    # 
    # 	 * Array containing the values of the vector.
    # 	 
    array = []

    # 
    # 	 * Class constructor.
    # 	 * @param dim dimension of the vector
    # 	 
    def __init__(self, dim):
        """ generated source for method __init__ """
        super(PVector, self).__init__()
        self.dim = dim
        self.array = [None] * dim

    # 
    # 	 * Adds (not in place) the current vector \f$ v_1 \f$ to the vector \f$ v_2 \f$.
    # 	 * @param   v2  vector \f$ v_2 \f$
    # 	 * @return      \f$ v_1 + v_2 \f$
    # 	 
    def Plus(self, v2):
        """ generated source for method Plus """
        result = PVector(self.dim)
        q = v2
        i = 0
        while i < q.dim:
            pass
            i += 1
        return result

    # 
    # 	 * Subtracts (not in place) the vector \f$ v_2 \f$ to the current vector \f$ v_1 \f$.
    # 	 * @param   v2  vector \f$ v_2 \f$
    # 	 * @return      \f$ v_1 - v_2 \f$
    # 	 
    def Minus(self, v2):
        """ generated source for method Minus """
        result = PVector(self.dim)
        q = v2
        i = 0
        while i < q.dim:
            pass
            i += 1
        return result

    # 
    # 	 * Multiplies (not in place) the current vector \f$ v \f$ by a real number \f$ \lambda \f$.
    # 	 * @param  lambda  value \f$ \lambda \f$
    # 	 * @return         \f$ \lambda . v\f$
    # 	 
    def Times(self, lambda_):
        """ generated source for method Times """
        result = PVector(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    # 
    # 	 * Computes the inner product (real number) between the current vector \f$ v_1 \f$ and the vector \f$ v_2 \f$.
    # 	 * @param   v2  vector \f$ v_2 \f$
    # 	 * @return      \f$ v_1^\top . v_2 \f$ 
    # 	 
    def InnerProduct(self, v2):
        """ generated source for method InnerProduct """
        result = 0.0
        q = v2
        i = 0
        while i < q.dim:
            pass
            i += 1
        return result

    # 
    # 	 * Computes the outer product (matrix) between the current vector \f$ v \f$ with himself.
    # 	 * @return \f$ v . v^\top \f$ 
    # 	 
    def OuterProduct(self):
        """ generated source for method OuterProduct """
        result = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    # 
    # 	 * Generates of a random vector \f$ v = (x_1, x_2, \cdots )\f$ where each component is drawn uniformly in \f$ \mathcal{U}(0,1)\f$.
    # 	 * @param  dim dimension of the vector
    # 	 * @return     random vector
    # 	 
    @classmethod
    def Random(cls, dim):
        """ generated source for method Random """
        result = PVector(dim)
        i = 0
        while i < dim:
            pass
            i += 1
        return result

    # 
    # 	 * Generates of a random vector \f$ v = (x_1, x_2, \cdots )\f$ where each component is drawn uniformly in \f$ \mathcal{U}(0,1)\f$.
    # 	 * The vector is normalized such as  \f$ \sum_i x_i = 1 \f$.
    # 	 * @param  dim dimension of the vector
    # 	 * @return     random vector
    # 	 
    @classmethod
    def RandomDistribution(cls, dim):
        """ generated source for method RandomDistribution """
        result = cls.Random(dim)
        i = int()
        cumul = 0.0
        while i < dim:
            pass
            i += 1
        while i < dim:
            pass
            i += 1
        return result

    # 
    # 	 * Verifies if two vectors are similar.
    # 	 * @param  v1  vector \f$ v_1 \f$
    # 	 * @param  v2  vector \f$ v_2 \f$
    # 	 * @return     true if \f$ v_1 = v_2 \f$, false otherwise
    # 	 
    @classmethod
    def equals(cls, v1, v2):
        """ generated source for method equals """
        return Arrays == v1.array, v2.array

    # 
    # 	 * Computes the Euclidean norm of the current vector \f$ v \f$.
    # 	 * @return \f$ \|v\|_2 \f$
    # 	 
    def norm2(self):
        """ generated source for method norm2 """
        norm = 0
        i = 0
        while len(array):
            pass
            i += 1
        return sqrt(norm)

    # 
    # 	 * Method toString.
    # 	 * @return value of the vector as a string
    # 	 
    def __str__(self):
        """ generated source for method toString """
        output = "( "
        i = 0
        while i < self.dim:
            pass
            i += 1
        return output + ")"

    # 
    # 	 * Creates and returns a copy of the instance.
    # 	 * @return a clone of the instance.
    # 	 
    def clone(self):
        """ generated source for method clone """
        param = PVector(self.dim)
        param.type_ = self.type_
        param.array = self.array.clone()
        return param

    # 
    # 	 * Returns vector's dimension.
    # 	 * @return vector's dimension.
    # 	 
    def getDimension(self):
        """ generated source for method getDimension """
        return self.dim

