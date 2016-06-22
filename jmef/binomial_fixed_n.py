#!/usr/bin/env python
""" generated source for module BinomialFixedN """
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
#  * The Binomial distribution, with \f$ n \f$ fixed, is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Binomial distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = p \in [0,1] \f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \in R \f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in [0,1]^+ \f$
#  *
#  
class BinomialFixedN(ExponentialFamily, PVector, PVector):
    """ generated source for class BinomialFixedN """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Parameter n.
    # 	 
    n = int()

    # 
    # 	 * Class constructor. 
    # 	 
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(BinomialFixedN, self).__init__()
        self.n = 100

    # 
    # 	 * Class constructor.
    # 	 * @param n parameter n
    # 	 
    @__init__.register(object, int)
    def __init___0(self, n):
        """ generated source for method __init___0 """
        super(BinomialFixedN, self).__init__()
        self.n = n

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = n \log (1 + \exp \theta) - \log (n!) \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return self.n * log(1 + exp(T.array[0])) - log(fact(self.n))

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \frac{n \exp \theta}{1 + \exp \theta} \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVector(1)
        gradient.array[0] = self.n * exp(T.array[0]) / (1 + exp(T.array[0]))
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{H}) = \eta \log \left( \frac{\eta}{n-\eta} \right)  - n \log\left( \frac{n}{n-\eta} \right) \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return H.array[0] * log(H.array[0] / (self.n - H.array[0])) - self.n * log(self.n / (self.n - H.array[0]))

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G( \mathbf{H} ) = \log \left( \frac{\eta}{n-\eta} \right) \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVector(1)
        gradient.array[0] = log(H.array[0] / (self.n - H.array[0]))
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
    # 	 * @return     \f$ k(x) = - \log (x! (n-x)!) \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return float((-log(fact(x.array[0]) * fact(self.n - x.array[0]))))

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
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \frac{\exp \theta}{1 + \exp \theta} \f$
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
    # 	 * @return     expectation parameters \f$ \mathbf{H}       = np \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = self.n * L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}       = \eta\f$
    # 	 * @return     source parameters      \f$ \mathbf{\Lambda} = \frac{\eta}{n} \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0] / self.n
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;p) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;p) = \frac{n!}{x!(n-x)!} p^x (1-p)^{n-x} \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return (fact(self.n) * pow(param.array[0], x.array[0]) * pow(1 - param.array[0], self.n - x.array[0])) / (fact(x.array[0]) * fact(self.n - x.array[0]))
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(BinomialFixedN, self).density(x, param)
        else:
            return super(BinomialFixedN, self).density(x, Eta2Theta(param))

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
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = p \f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        #  Loop
        count = 0
        i = 0
        while i < self.n:
            pass
            i += 1
        #  Point
        point = PVector(1)
        point.array[0] = count
        return point

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Binomial distributions.
    # 	 * @param   L1  source parameters \f$ \mathbf{\Lambda}_1 \f$
    # 	 * @param   L2  source parameters \f$ \mathbf{\Lambda}_2 \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_1\|f_2) = n (1-p_1) \log \left( \frac{1-p_1}{1-p_2} \right) + n p_1 \log \left( \frac{p_1}{p_2} \right) \f$
    # 	 
    def KLD(self, L1, L2):
        """ generated source for method KLD """
        p1 = L1.array[0]
        p2 = L2.array[0]
        q1 = 1 - p1
        q2 = 1 - p2
        return self.n * q1 * log(q1 / q2) + self.n * p1 * log(p1 / p2)

