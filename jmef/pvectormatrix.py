#!/usr/bin/env python
""" generated source for module PVectorMatrix """
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
#  * The PVectorMatrix class implements a parameter object.
#  * Parameters are represented as a mixed type vector-matrix.
#  
class PVectorMatrix(Parameter):
    """ generated source for class PVectorMatrix """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Vector parameter.
    # 	 
    v = None

    # 
    # 	 * Matrix parameter.
    # 	 
    M = None

    # 
    # 	 * Dimension of the matrix-vector.
    # 	 
    dim = int()

    # 
    # 	 * Class constructor.
    # 	 * @param dim dimension of the matrix
    # 	 
    def __init__(self, dim):
        """ generated source for method __init__ """
        super(PVectorMatrix, self).__init__()
        self.dim = dim
        self.v = PVector(dim)
        self.M = PMatrix(dim)

    # 
    # 	 * Adds (not in place) the current vector-matrix \f$ (v_1, m_1) \f$ to the vector-matrix \f$ (v_2, m_2) \f$.
    # 	 * @param   v2m2  vector-matrix \f$ (v_2, m_2) \f$
    # 	 * @return        \f$ ( v_1 + v_2, m_1 + m_2 ) \f$
    # 	 
    def Plus(self, v2m2):
        """ generated source for method Plus """
        Q = v2m2
        result = PVectorMatrix(Q.v.dim)
        result.v = self.v.Plus(Q.v)
        result.M = self.M.Plus(Q.M)
        return result

    # 
    # 	 * Subtracts (not in place) the vector-matrix \f$ (v_2, m_2) \f$ to the current vector-matrix \f$ (v_1, m_1) \f$.
    # 	 * @param   v2m2  vector-matrix \f$ (v_2, m_2) \f$
    # 	 * @return        \f$ ( v_1 - v_2, m_1 - m_2 ) \f$
    # 	 
    def Minus(self, v2m2):
        """ generated source for method Minus """
        Q = v2m2
        result = PVectorMatrix(Q.v.dim)
        result.v = self.v.Minus(Q.v)
        result.M = self.M.Minus(Q.M)
        return result

    # 
    # 	 * Multiplies (not in place) the current vector-matrix \f$ (v,m) \f$ by a real number \f$ \lambda \f$.
    # 	 * @param  lambda  value \f$ \lambda \f$
    # 	 * @return         \f$ ( \lambda v , \lambda m ) \f$
    # 	 
    def Times(self, lambda_):
        """ generated source for method Times """
        result = PVectorMatrix(self.v.dim)
        result.v = self.v.Times(lambda_)
        result.M = (self.M).Times(lambda_)
        return result

    # 
    # 	 * Computes the inner product (real number) between the current vector-matrix \f$ ( v_1 , m_1 ) \f$ and the vector-matrix \f$ ( v_2 , m_2 ) \f$.
    # 	 * @param   v2m2  vector-matrix \f$ (v_2, m_2) \f$
    # 	 * @return        \f$ \langle v_1,v_2 \rangle + \langle m_1,m_2 \rangle \f$ 
    # 	 
    def InnerProduct(self, v2m2):
        """ generated source for method InnerProduct """
        Q = v2m2
        return self.v.InnerProduct(Q.v) + self.M.InnerProduct(Q.M)

    # 
    # 	 * Generates a random vector-matrix \f$ (v,m) \f$ such as \f$ m \f$ is a positive definite matrix.
    # 	 * @param  dim  dimension of the matrix
    # 	 * @return      random vector-matrix \f$ ( v , m ) \f$
    # 	 
    @classmethod
    def RandomDistribution(cls, dim):
        """ generated source for method RandomDistribution """
        vM = PVectorMatrix(dim)
        vM.v = PVector.Random(dim)
        vM.M = PMatrix.RandomPositiveDefinite(dim)
        return vM

    # 
    # 	 * Verifies if two vector-matrices \f$ (v_1 , m_1) \f$ and \f$ (v_2 , m_2) \f$ are similar. 
    # 	 * @param   v1m1  vector-matrix \f$ (v_1, m_1) \f$
    # 	 * @param   v2m2  vector-matrix \f$ (v_2, m_2) \f$
    # 	 * @return        true if \f$ v_1 = v_2 \f$ and \f$ m_1 = m_2 \f$, false otherwise
    # 	 
    @classmethod
    def equals(cls, v1m1, v2m2):
        """ generated source for method equals """
        return (PVector == v1m1.v, v2m2.v and PMatrix == v1m1.M, v2m2.M)

    # 
    # 	 * Method toString.
    # 	 * @return value of the vector-matrix as a string
    # 	 
    def __str__(self):
        """ generated source for method toString """
        return "" + self.v + "\n" + self.M + "\n"

    # 
    # 	 * Creates and returns a copy of the instance.
    # 	 * @return a clone of the instance.
    # 	 
    def clone(self):
        """ generated source for method clone """
        param = PVectorMatrix(self.dim)
        param.type_ = self.type_
        param.v = self.v.clone()
        param.M = self.M.clone()
        return param

    # 
    # 	 * Returns parameters' dimension.
    # 	 * @return parameters' dimension.
    # 	 
    def getDimension(self):
        """ generated source for method getDimension """
        return self.v.dim

