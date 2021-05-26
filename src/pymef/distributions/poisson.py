#!/usr/bin/env python
""" generated source for module Poisson """
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
#  * The Poisson distribution is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Poisson distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = \lambda \in R^+\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \in R\f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in R^+\f$
#  *
#  
class Poisson(ExponentialFamily, PVector, PVector):
    """ generated source for class Poisson """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\Theta})	= \exp \theta \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return exp(T.array[0])

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \exp \theta \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        g = PVector(1)
        g.array[0] = exp(T.array[0])
        g.type_ = TYPE.EXPECTATION_PARAMETER
        return g

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{H}) = \eta \log \eta - \eta \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return H.array[0] * log(H.array[0]) - H.array[0]

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G( \mathbf{H} ) = \log \eta \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        g = PVector(1)
        g.array[0] = log(H.array[0])
        g.type_ = TYPE.NATURAL_PARAMETER
        return g

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = x \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = PVector(1)
        t.array[0] = x.array[0]
        t.type_ = TYPE.EXPECTATION_PARAMETER
        return t

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) = - \log (x!) \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return -log(float(fact(int(x.array[0]))))

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters  \f$ \mathbf{\Lambda} = \lambda \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta}  = \log \lambda \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(1)
        T.array[0] = log(L.array[0])
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}  = \theta \f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \exp \theta \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(1)
        L.array[0] = exp(T.array[0])
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters      \f$ \mathbf{\Lambda} = \lambda \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H}       = \lambda \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}       = \eta \f$
    # 	 * @return     source parameters      \f$ \mathbf{\Lambda} = \eta \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;\lambda) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;\lambda) = \frac{\lambda^x \exp(-\lambda)}{x!} \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return (pow(param.array[0], x.array[0]) * exp(-param.array[0])) / (float(fact(int(x.array[0]))))
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(Poisson, self).density(x, param)
        else:
            return super(Poisson, self).density(x, Eta2Theta(param))

    # 
    # 	 * Computes the factorial of a number.
    # 	 * @param  n  number
    # 	 * @return n!
    # 	 
    def fact(self, n):
        """ generated source for method fact """
        f = 1
        i = 1
        while i <= n:
            pass
            i += 1
        return f

    # 
    # 	 * Draws a point from the considered Poisson distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \lambda \f$
    # 	 * @return     a point.
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        #  Initialization
        l = exp(-L.array[0])
        p = 1.0
        k = 0
        #  Loop
        while True:
            k += 1
            p *= random()
            if not ((p > l)):
                break
        #  Point
        point = PVector(1)
        point.array[0] = k - 1
        return point

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Poisson distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P\|f_Q) = \lambda_Q - \lambda_P \left( 1 + \log \left( \frac{\lambda_Q}{\lambda_P} \right) \right) \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        lp = LP.array[0]
        lq = LQ.array[0]
        return lq - lp * (1 + log(lq / lp))

