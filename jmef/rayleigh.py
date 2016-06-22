#!/usr/bin/env python
""" generated source for module Rayleigh """
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
#  * The Rayleigh is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Rayleigh distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$ \mathbf{\Lambda} = \sigma^2 \in \mathds{R}^+ \f$
#  *   - Natural parameters \f$ \mathbf{\Theta} = \theta \in \mathds{R}^- \f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in \mathds{R}^+ \f$
#  *
#  
class Rayleigh(ExponentialFamily, PVector, PVector):
    """ generated source for class Rayleigh """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\theta}) = - \log (-2 \theta) \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return -log(-2 * T.array[0])

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F(\mathbf{\theta}) = -\frac{1}{\theta} \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVector(1)
        gradient.array[0] = -1.0 / T.array[0]
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{\eta}) = - \log \eta \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return -log(H.array[0])

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G(\mathbf{\eta}) = -\frac{1}{\eta} \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVector(1)
        gradient.array[0] = -1.0 / H.array[0]
        gradient.type_ = TYPE.NATURAL_PARAMETER
        return gradient

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = x^2 \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = PVector(1)
        t.array[0] = x.array[0] * x.array[0]
        t.type_ = TYPE.EXPECTATION_PARAMETER
        return t

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) = \log x \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return log(x.array[0])

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters  \f$ \mathbf{\Lambda} = \sigma^2 \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta}  = -\frac{1}{2 \sigma^2} \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(1)
        T.array[0] = -1.0 / (2.0 * L.array[0])
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}  = \theta \f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = -\frac{1}{2\theta} \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(1)
        L.array[0] = -1.0 / (2.0 * T.array[0])
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters      \f$ \mathbf{\Lambda} = \sigma^2 \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H}       = 2 \sigma^2 \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = 2 * L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}       = \eta\f$
    # 	 * @return     source parameters      \f$ \mathbf{\Lambda} = \frac{\eta}{2} \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0] / 2.0
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;p) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;\sigma^2) = \frac{x}{\sigma^2} \exp \left( -\frac{x^2}{2\sigma^2} \right) \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return (exp(-(x.array[0] * x.array[0]) / (2 * param.array[0])) * x.array[0]) / param.array[0]
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(Rayleigh, self).density(x, param)
        else:
            return super(Rayleigh, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \sigma^2 \f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        x = PVector(1)
        x.array[0] = sqrt(-2 * log(random()) * L.array[0])
        return x

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Binomial distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P \| f_Q) = \log \left( \frac{\sigma_Q^2}{\sigma_P^2} \right) + \frac{ \sigma_P^2 - \sigma_Q^2 }{\sigma_Q^2} \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        vP = LP.array[0]
        vQ = LQ.array[0]
        return log(vQ / vP) + ((vP - vQ) / vQ)

