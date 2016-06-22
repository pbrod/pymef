#!/usr/bin/env python
""" generated source for module MultinomialFixedN """
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
#  * The Multinomial distribution, with \f$ n\f$ fixed, is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Multinomial distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = (p_1,\cdots,p_k) \in [0,1]^k\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = (\theta_1,\cdots,\theta_{k-1}) \in R^{k-1}\f$
#  *   - Expectation parameters \f$ \mathbf{H} = (\eta_1,\cdots,\eta_{k-1}) \in [0,n]^{k-1} \f$
#  
class MultinomialFixedN(ExponentialFamily, PVector, PVector):
    """ generated source for class MultinomialFixedN """
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
        super(MultinomialFixedN, self).__init__()
        self.n = 100

    # 
    # 	 * Class constructor.
    # 	 * @param n parameter n
    # 	 
    @__init__.register(object, int)
    def __init___0(self, n):
        """ generated source for method __init___0 """
        super(MultinomialFixedN, self).__init__()
        self.n = n

    # 
    # 	 * Computes \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  parameters \f$ \mathbf{\Theta} = (\theta_1, \cdots, \theta_{k-1}) \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = n \log \left( 1 + \sum_{i=1}^{k-1} \exp \theta_i \right) - \log n! \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        sum = 0
        i = 0
        while i < T.getDimension():
            pass
            i += 1
        return self.n * log(1 + sum) - log(fact(self.n))

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  naturel parameters \f$ \mathbf{\Theta} = (\theta_1, \cdots, \theta_{k-1}) \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \left( \frac{n \exp \theta_i}{1 + \sum_{j=1}^{k-1} \exp \theta_j} \right)_i \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        #  Sum
        sum = 0
        i = 0
        while i < T.getDimension():
            pass
            i += 1
        #  Gradient
        gradient = PVector(T.getDimension())
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        i = 0
        while i < T.getDimension():
            pass
            i += 1
        #  Return
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = (\eta_1, \cdots, \eta_{k-1}) \f$
    # 	 * @return     \f$ G(\mathbf{H}) = \left( \sum_{i=1}^{k-1} \eta_i \log \eta_i \right) + \left( n - \sum_{i=1}^{k-1} \eta_i \right) \log \left( n - \sum_{i=1}^{k-1} \eta_i \right) \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        sum1 = 0
        sum2 = 0
        i = 0
        while i < H.getDimension():
            sum1 += H.array[i] * log(H.array[i])
            sum2 += H.array[i]
            i += 1
        return sum1 + (self.n - sum2) * log(self.n - sum2)

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = (\eta_1, \cdots, \eta_{k-1}) \f$
    # 	 * @return     \f$ \nabla G( \mathbf{H} ) = \left( \log \left( \frac{\eta_i}{n - \sum_{j=1}^{k-1} \eta_j} \right) \right)_i \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        #  Sum
        sum = 0
        i = 0
        while i < H.getDimension():
            pass
            i += 1
        #  Gradient
        gradient = PVector(H.getDimension())
        gradient.type_ = TYPE.NATURAL_PARAMETER
        i = 0
        while i < H.getDimension():
            pass
            i += 1
        #  Return
        return gradient

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = (x_1, \cdots, x_{k-1}) \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = PVector(x.getDimension() - 1)
        t.type_ = TYPE.EXPECTATION_PARAMETER
        i = 0
        while i < x.getDimension() - 1:
            pass
            i += 1
        return t

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) = - \sum_{i=1}^{k} \log x_i ! \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        sum = 0
        i = 0
        while i < x.getDimension():
            pass
            i += 1
        return sum

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = (p_1, \cdots, p_k)\f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} = \left( \log \left( \frac{p_i}{p_k} \right) \right)_i \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        theta = PVector(L.getDimension() - 1)
        theta.type_ = TYPE.NATURAL_PARAMETER
        i = 0
        while i < L.getDimension() - 1:
            pass
            i += 1
        return theta

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = ( \theta_1, \cdots, \theta_{k-1} )\f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} =	\begin{cases}
    # 	                                                          p_i = \frac{\exp \theta_i}{1 + \sum_{j=1}^{k-1}(\exp \theta_j)} & \mbox{if $i<k$}\\
    # 	                                                          p_k = \frac{1}{1 + \sum_{j=1}^{k-1}(\exp \theta_j)}
    # 	                                                        \end{cases} \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        #  Sums
        sum = 0
        i = 0
        while i < T.getDimension():
            pass
            i += 1
        #  Conversion
        lambda_ = PVector(T.getDimension() + 1)
        lambda_.type_ = TYPE.SOURCE_PARAMETER
        i = 0
        while i < T.getDimension():
            pass
            i += 1
        lambda_.array[T.getDimension()] = 1.0 / (1.0 + sum)
        #  Return
        return lambda_

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = ( p_1, \cdots, p_k )\f$
    # 	 * @return     expectation parameters \f$ \mathbf{H} = \left( n p_i \right)_i\f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(L.getDimension() - 1)
        H.type_ = TYPE.EXPECTATION_PARAMETER
        i = 0
        while i < L.getDimension() - 1:
            pass
            i += 1
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  natural parameters \f$ \mathbf{H} = (\eta_1, \cdots, \eta_{k-1})\f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} = \begin{cases}
    # 	                                                          p_i = \frac{\eta_i}{n} & \mbox{if $i<k$}\\
    # 	                                                          p_k = \frac{n - \sum_{j=1}^{k-1} \eta_j}{n}
    # 	                                                        \end{cases}\f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(H.getDimension() + 1)
        L.type_ = TYPE.SOURCE_PARAMETER
        sum = 0
        i = 0
        while i < H.getDimension():
            L.array[i] = H.array[i] / self.n
            sum += H.array[i]
            i += 1
        L.array[H.getDimension()] = (self.n - sum) / self.n
        return L

    # 
    # 	 * Computes the density value \f$ f(x) \f$.
    # 	 * @param  x      point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x_1,\cdots,x_k;p_1,\cdots,p_k,n) = \frac{n!}{x_1! \cdots x_k!} p_1^{x_1} \cdots p_k^{x_k} \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            prod1 = 1
            prod2 = 1
            i = 0
            while i < param.getDimension():
                prod1 *= fact(x.array[i])
                prod2 *= pow(param.array[i], x.array[i])
                i += 1
            return (fact(self.n) * prod2) / prod1
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(MultinomialFixedN, self).density(x, param)
        else:
            return super(MultinomialFixedN, self).density(x, Eta2Theta(param))

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
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = ( p_1, \cdots, p_k )\f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        #  Variables
        k = L.dim
        p = [None] * k
        #  Build array of sum of probabilities
        p[0] = L.array[0]
        i = 1
        while i < k - 1:
            pass
            i += 1
        p[k - 1] = 1
        #  Draw a point
        x = PVector(k)
        i = 0
        while i < self.n:
            u = random()
            idx = 0
            while u > p[idx]:
            x.array[idx] += 1
            i += 1
        #  Return
        return x

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Binomial distributions.
    # 	 * @param   LA  source parameters \f$ \mathbf{\Lambda}_\alpha \f$
    # 	 * @param   LB  source parameters \f$ \mathbf{\Lambda}_\beta \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_1\|f_2) = n p_{\alpha,k} \log \frac{p_{\alpha,k}}{p_{\beta,k}} - n \sum_{i=1}^{k-1} p_{\alpha,i} \log \frac{p_{\beta,i}}{p_{\alpha,i}} \f$
    # 	 
    def KLD(self, LA, LB):
        """ generated source for method KLD """
        k = LA.getDimension() - 1
        sum = 0
        i = 0
        while i < k:
            pass
            i += 1
        return self.n * LA.array[k] * log(LA.array[k] / LB.array[k]) - self.n * sum

