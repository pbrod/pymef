#!/usr/bin/env python
""" generated source for module MultivariateIsotropicGaussian """
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
#  * The multivariate isotropic Gaussian distribution (\f$\Sigma=\f$Id) is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a multivariate Gaussian distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = \mu \mbox{ with } \mu \in \mathds{R}^d \f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \f$
#  *   - Expectation parameters \f$\mathbf{H} = \eta \f$
#  
class MultivariateIsotropicGaussian(ExponentialFamily, PVector, PVector):
    """ generated source for class MultivariateIsotropicGaussian """
    # 
    # 	 * Constant for serialization
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\theta}) = \frac{1}{2} \theta^\top\theta + \frac{d}{2}\log 2\pi \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return 0.5 * (T.InnerProduct(T) + T.dim * log(2 * PI))

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural  \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \theta \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = T.clone()
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ F(\mathbf{\theta})= \frac{1}{2} \eta^\top\eta + \frac{d}{2}\log 2\pi \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return 0.5 * (H.InnerProduct(H) + H.dim * log(2 * PI))

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G(\mathbf{H}) = \eta \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = H.clone()
        gradient.type_ = TYPE.NATURAL_PARAMETER
        return gradient

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = x \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = x.clone()
        t.type_ = TYPE.EXPECTATION_PARAMETER
        return t

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) = -\frac{1}{2}x^\top x \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return -0.5 * x.InnerProduct(x)

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \mu \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} = \mu \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = L.clone()
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} = \theta \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = T.clone()
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \mu \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H}  = \mu \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = L.clone()
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}  = \eta \f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} = \eta \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = H.clone()
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;\mu) \f$.
    # 	 * @param  x      point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return         \f$ f(x;\mu) = \frac{1}{ (2\pi)^{d/2} } \exp \left( - \frac{(x-\mu)^T (x-\mu)}{2} \right) \mbox{ for } x \in \mathds{R}^d \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            v1 = (x.Minus(param)).InnerProduct(x.Minus(param))
            v2 = exp(-0.5 * v1)
            return v2 / pow(2.0 * PI, float(x.dim) / 2.0)
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(MultivariateIsotropicGaussian, self).density(x, param)
        else:
            return super(MultivariateIsotropicGaussian, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \mu \f$
    # 	 * @return     a point.
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        rand = Random()
        x = PVector(L.getDimension())
        i = 0
        while i < L.getDimension():
            pass
            i += 1
        return x

    # 
    # 	 * Computes the Kullback-Leibler divergence between two multivariate isotropic Gaussian distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P \| f_Q) = \frac{1}{2} ( \mu_Q - \mu_P )^\top( \mu_Q - \mu_P ) \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        diff = LQ.Minus(LP)
        return 0.5 * diff.InnerProduct(diff)

