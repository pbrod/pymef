#!/usr/bin/env python
""" generated source for module Bernoulli """
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
#  * The Bernoulli distribution is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Bernoulli distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = p \in [0,1]\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \in R^+\f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in [0,1] \f$
#  
class Bernoulli(ExponentialFamily, PVector, PVector):
    """ generated source for class Bernoulli """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = \log \left( 1 + \exp \theta \right) \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return log(1 + exp(T.array[0]))

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \frac{\exp \theta}{1 + \exp \theta} \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVector(1)
        gradient.array[0] = exp(T.array[0]) / (1 + exp(T.array[0]))
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{H}) = \log \left( \frac{\eta}{1-\eta} \right) \eta - \log \left( \frac{1}{1-\eta} \right) \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return H.array[0] * log(H.array[0] / (1 - H.array[0])) - log(1.0 / (1 - H.array[0]))

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G( \mathbf{H} ) = \log \left( \frac{\eta}{1-\eta} \right) \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVector(1)
        gradient.array[0] = log(H.array[0] / (1 - H.array[0]))
        gradient.type_ = TYPE.NATURAL_PARAMETER
        return gradient

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
    # 	 * @return     \f$ k(x) = 0 \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return 0.0

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters  \f$ \mathbf{\Lambda} = p \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta}  = \log \left( \frac{p}{1-p} \right) \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(1)
        T.array[0] = log(L.array[0] / (1 - L.array[0]))
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}  = \theta \f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \frac{\exp\theta}{1+\exp\theta} \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(1)
        L.array[0] = exp(T.array[0]) / (1 + exp(T.array[0]))
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters      \f$ \mathbf{\Lambda} = p \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H}       = p \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}       = \eta\f$
    # 	 * @return     source parameters      \f$ \mathbf{\Lambda} = \eta \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;p) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;p) = p^x (1-p)^{1-x} \mbox{ for } x \in \{0,1\} \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return pow(param.array[0], x.array[0]) * pow(1 - param.array[0], 1 - x.array[0])
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(Bernoulli, self).density(x, param)
        else:
            return super(Bernoulli, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = p \f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        x = PVector(1)
        if random() < L.array[0]:
            x.array[0] = 1
        else:
            x.array[0] = 0
        return x

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Bernoulli distributions.
    # 	 * @param   L1  source parameters \f$ \mathbf{\Lambda}_1 \f$
    # 	 * @param   L2  source parameters \f$ \mathbf{\Lambda}_2 \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_1\|f_2) = \log \left( \frac{1-p_1}{1-p_2} \right) - p_1 \log \left( \frac{p_2(1-p_1)}{p_1(1-p_2)} \right) \f$
    # 	 
    def KLD(self, L1, L2):
        """ generated source for method KLD """
        p1 = L1.array[0]
        p2 = L2.array[0]
        q1 = 1 - p1
        q2 = 1 - p2
        return log(q1 / q2) - p1 * log((p2 * q1) / (p1 * q2))

