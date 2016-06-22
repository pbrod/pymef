#!/usr/bin/env python
""" generated source for module MultivariateGaussian """
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
#  * The multivariate Gaussian distribution is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a multivariate Gaussian distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = ( \mu , \Sigma ) \mbox{ with } \mu \in \mathds{R}^d \mbox{ and } \Sigma \succ 0\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = ( \theta , \Theta )\f$
#  *   - Expectation parameters \f$\mathbf{H} = ( \eta , H )\f$
#  
class MultivariateGaussian(ExponentialFamily, PVector, PVectorMatrix):
    """ generated source for class MultivariateGaussian """
    # 
    # 	 * Constant for serialization
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = ( \theta , \Theta ) \f$
    # 	 * @return     \f$ F(\mathbf{\Theta})=\frac{1}{4} \mathrm{tr}(\Theta^{-1}\theta\theta^T) - \frac{1}{2} \log \det\Theta + \frac{d}{2} log \pi  \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return 0.25 * ((T.M.Inverse()).Multiply(T.v.OuterProduct())).Trace() - 0.5 * log(T.M.Determinant()) + (0.5 * T.v.dim) * log(PI)

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural  \f$ \mathbf{\Theta} = ( \theta , \Theta ) \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \left( \frac{1}{2} \Theta^{-1} \theta , -\frac{1}{2} \Theta^{-1} -\frac{1}{4} (\Theta^{-1} \theta)(\Theta^{-1} \theta)^T \right) \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVectorMatrix(T.v.dim)
        gradient.v = T.M.Inverse().MultiplyVectorRight(T.v).Times(0.5)
        gradient.M = T.M.Inverse().Times(-0.5).Minus((T.M.Inverse().MultiplyVectorRight(T.v)).OuterProduct().Times(0.25))
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    def G(self, H):
        """ generated source for method G """
        return -0.5 * log(1.0 + H.v.InnerProduct(H.M.Inverse().MultiplyVectorRight(H.v))) - 0.5 * log(H.M.Times(-1.0).Determinant()) - H.v.dim * 0.5 * log(2 * PI * E)

    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVectorMatrix(H.v.dim)
        tmp = H.M.Plus(H.v.OuterProduct()).Inverse()
        gradient.v = tmp.MultiplyVectorRight(H.v).Times(-1.0)
        gradient.M = tmp.Times(-0.5)
        gradient.type_ = TYPE.NATURAL_PARAMETER
        return gradient

    def t(self, x):
        """ generated source for method t """
        t = PVectorMatrix(x.dim)
        t.v = x
        t.M = x.OuterProduct().Times(-1)
        t.type_ = TYPE.EXPECTATION_PARAMETER
        return t

    def k(self, x):
        """ generated source for method k """
        return 0.0

    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVectorMatrix(L.v.dim)
        tmp = L.M.Inverse()
        T.v = tmp.MultiplyVectorRight(L.v)
        T.M = tmp.Times(0.5)
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVectorMatrix(T.v.dim)
        L.M = T.M.Inverse().Times(0.5)
        L.v = L.M.MultiplyVectorRight(T.v)
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVectorMatrix(L.v.dim)
        H.v = L.v.clone()
        H.M = L.M.Plus(L.v.OuterProduct()).Times(-1)
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVectorMatrix(H.v.dim)
        L.v = H.v.clone()
        L.M = H.M.Plus(H.v.OuterProduct()).Times(-1)
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            v1 = (x.Minus(param.v)).InnerProduct(param.M.Inverse().MultiplyVectorRight(x.Minus(param.v)))
            v2 = exp(-0.5 * v1)
            v3 = pow(2.0 * PI, float(x.dim) / 2.0) * sqrt(param.M.Determinant())
            return v2 / v3
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(MultivariateGaussian, self).density(x, param)
        else:
            return super(MultivariateGaussian, self).density(x, Eta2Theta(param))

    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        rand = Random()
        z = PVector(L.getDimension())
        i = 0
        while i < L.getDimension():
            pass
            i += 1
        return L.M.Cholesky().MultiplyVectorRight(z).Plus(L.v)

    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        mP = LP.v
        vP = LP.M
        mQ = LQ.v
        vQ = LQ.M
        tmp = mQ.Minus(mP)
        return 0.5 * (log(vQ.Determinant() / vP.Determinant()) + vQ.Inverse().Multiply(vP).Trace() + tmp.InnerProduct(vQ.Inverse().MultiplyVectorRight(tmp)) - LP.dim)

