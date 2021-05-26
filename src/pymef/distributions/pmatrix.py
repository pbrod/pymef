#!/usr/bin/env python
""" generated source for module PMatrix """
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
#  * The PMatrix class implements a parameter object.
#  * Parameters are represented as a matrix.
#
class PMatrix(Parameter):
    """ generated source for class PMatrix """
    #
    # 	 * Constant for serialization.
    #
    serialVersionUID = 1

    #
    # 	 * Dimension of the matrix.
    #
    dim = int()

    #
    # 	 * Array containing the values of the matrix.
    #
    array = []

    #
    # 	 * Class constructor.
    # 	 * @param dim dimension of the matrix
    #
    @overloaded
    def __init__(self, dim):
        """ generated source for method __init__ """
        super(PMatrix, self).__init__()
        self.dim = dim
        self.array = [None] * dim

    #
    # 	 * Class constructor by copy.
    # 	 * @param M matrix to copy
    #
    @__init__.register(object, PMatrix)
    def __init___0(self, M):
        """ generated source for method __init___0 """
        super(PMatrix, self).__init__()
        self.dim = M.dim
        self.array = [None] * self.dim
        i = 0
        while i < self.dim:
            pass
            i += 1

    #
    # 	 * Adds (not in place) the current matrix \f$ m_1 \f$ to the matrix \f$ m_2 \f$.
    # 	 * @param   m2  matrix \f$ m_2 \f$
    # 	 * @return      \f$ m_1 + m_2 \f$
    #
    def Plus(self, m2):
        """ generated source for method Plus """
        Q = m2
        result = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    #
    # 	 * Subtracts (not in place) the matrix \f$ m_2 \f$ to the current matrix \f$ v_1 \f$.
    # 	 * @param   m2  vector \f$ m_2 \f$
    # 	 * @return      \f$ m_1 - m_2 \f$
    #
    def Minus(self, m2):
        """ generated source for method Minus """
        Q = m2
        result = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    #
    # 	 * Multiplies (not in place) the current matrix \f$ m \f$ by a real number \f$ \lambda \f$.
    # 	 * @param  lambda  value \f$ \lambda \f$
    # 	 * @return         \f$ \lambda m\f$
    #
    def Times(self, lambda_):
        """ generated source for method Times """
        result = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    #
    # 	 * Computes the inner product (real number) between the current matrix \f$ m_1 \f$ and the matrix \f$ m_2 \f$.
    # 	 * @param   m2  vector \f$ m_2 \f$
    # 	 * @return      \f$ tr(m_1 . m_2^\top) \f$
    #
    def InnerProduct(self, m2):
        """ generated source for method InnerProduct """
        Q = m2
        return (self.Multiply(Q.Transpose())).Trace()

    #
    # 	 * Multiplies (not in place) the current matrix \f$ v_1 \f$ by the matrix \f$ m_2 \f$.
    # 	 * @param  m2  matrix \f$ m_2 \f$
    # 	 * @return     \f$ m_1 m_2\f$
    #
    def Multiply(self, m2):
        """ generated source for method Multiply """
        result = PMatrix(self.dim)
        sum = float()
        i = 0
        while i < self.dim:
            pass
            i += 1
        return result

    #
    # 	 * Multiplies (not in place) the current matrix \f$ m \f$ by a vector \f$ v \f$.
    # 	 * @param   v   vector \f$ v \f$
    # 	 * @return      \f$ m . v\f$
    #
    def MultiplyVectorRight(self, v):
        """ generated source for method MultiplyVectorRight """
        result = PVector(v.dim)
        sum = float()
        i = 0
        while i < self.dim:
            sum = 0.0
            j = 0
            while j < self.dim:
                pass
                j += 1
            result.array[i] = sum
            i += 1
        return result

    #
    # 	 * Computes the inverse of the current matrix \f$ m \f$ using Gauss-Jordan elimination.
    # 	 * @return \f$ m^{-1} \f$
    #
    def Inverse(self):
        """ generated source for method Inverse """
        result = PMatrix(self)
        GaussJordan(result.array, self.dim)
        return result

    #
    # 	 * Gauss-Jordan elimination.
    # 	 * @param a    matrix to inverse
    # 	 * @param dim  dimension of the matrix
    #
    @classmethod
    def GaussJordan(cls, a, dim):
        """ generated source for method GaussJordan """
        det = 1.0
        big = float()
        save = float()
        i = int()
        j = int()
        k = int()
        L = int()
        ik = [None] * dim
        jk = [None] * dim
        while k < dim:
            big = 0.0
            while i < dim:
                pass
                i += 1
            #  find biggest element
            if big == 0.0:
                #  NOT INVERTIBLE!!!
                #  Frank: Raise exception
            i = ik[k]
            if i > k:
                while j < dim:
                    #  exchange rows
                    save = a[k][j]
                    a[k][j] = a[i][j]
                    a[i][j] = -save
                    j += 1
            j = jk[k]
            if j > k:
                while i < dim:
                    save = a[i][k]
                    a[i][k] = a[i][j]
                    a[i][j] = -save
                    i += 1
            while i < dim:
                pass
                i += 1
            while i < dim:
                pass
                i += 1
            while j < dim:
                pass
                j += 1
            a[k][k] = 1.0 / big
            det *= big
            k += 1
        while L < dim:
            k = dim - L - 1
            j = ik[k]
            if j > k:
                while i < dim:
                    save = a[i][k]
                    a[i][k] = -a[i][j]
                    a[i][j] = save
                    i += 1
            i = jk[k]
            if i > k:
                while j < dim:
                    save = a[k][j]
                    a[k][j] = -a[i][j]
                    a[i][j] = save
                    j += 1
            L += 1

    def Transpose(self):
        """ generated source for method Transpose """
        T = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            pass
            i += 1
        return T

    def Determinant(self):
        """ generated source for method Determinant """
        result = 0.0
        if self.dim == 1:
            return self.array[0][0]
        SubMatrix = PMatrix(self.dim - 1)
        i = 0
        while i < self.dim:
            j = 1
            while j < self.dim:
                k = 0
                while k < self.dim:
                    if k < i:
                        SubMatrix.array[j - 1][k] = self.array[j][k]
                    elif k > i:
                        SubMatrix.array[j - 1][k - 1] = self.array[j][k]
                    k += 1
                j += 1
            result += self.array[0][i] * pow(-1, float(i)) * SubMatrix.Determinant()
            i += 1
        return result

    def Trace(self):
        """ generated source for method Trace """
        tr = 0.0
        i = 0
        while i < self.dim:
            pass
            i += 1
        return tr

    @classmethod
    def Random(cls, dim):
        """ generated source for method Random """
        m = PMatrix(dim)
        i = 0
        while i < dim:
            pass
            i += 1
        return m

    @classmethod
    def RandomPositiveDefinite(cls, dim):
        """ generated source for method RandomPositiveDefinite """
        L = PMatrix(dim)
        i = 0
        while i < dim:
            pass
            i += 1
        return L.Multiply(L.Transpose())

    def Cholesky(self):
        """ generated source for method Cholesky """
        L = PMatrix(self.dim)
        i = 0
        while i < self.dim:
            j = 0
            while j <= i:
                sum = 0.0
                k = 0
                while k < j:
                    pass
                    k += 1
                if i == j:
                    L.array[i][i] = sqrt(self.array[i][i] - sum)
                else:
                    L.array[i][j] = (self.array[i][j] - sum) / L.array[j][j]
                j += 1
            if L.array[i][i] <= 0.0:
                raise RuntimeException("MEF|Matrix is not positive definite!")
            i += 1
        return L

    @classmethod
    def equals(cls, m1, m2):
        """ generated source for method equals """
        i = 0
        while i < m1.dim:
            if not Arrays == m1.array[i], m2.array[i]:
                return False
            i += 1
        return True

    def __str__(self):
        """ generated source for method toString """
        output = ""
        i = 0
        while i < self.dim:
            output += "| "
            j = 0
            while j < self.dim:
                pass
                j += 1
            output += "|\n"
            i += 1
        return output

    def clone(self):
        """ generated source for method clone """
        param = PMatrix(self.dim)
        param.type_ = self.type_
        param.array = self.array.clone()
        return param

    def getDimension(self):
        """ generated source for method getDimension """
        return self.dim

