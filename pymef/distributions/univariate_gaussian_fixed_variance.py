#!/usr/bin/env python
""" generated source for module UnivariateGaussianFixedVariance """
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
#  * The univariate Gaussian distribution, with fixed variance \f$ \sigma^2 \f$, is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a univariate Gaussian distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = \mu \in R\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \in R\f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in R\f$
#  
class UnivariateGaussianFixedVariance(ExponentialFamily, PVector, PVector):
    """ generated source for class UnivariateGaussianFixedVariance """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Variance \f$ \sigma^2\f$
    # 	 
    variance = float()

    # 
    # 	 * Class constructor with \f$\sigma^2=1\f$
    # 	 
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(UnivariateGaussianFixedVariance, self).__init__()
        self.variance = 1.0

    # 
    # 	 * Class constructor.
    # 	 * @param variance variance \f$ \sigma^2\f$
    # 	 
    @__init__.register(object, float)
    def __init___0(self, variance):
        """ generated source for method __init___0 """
        super(UnivariateGaussianFixedVariance, self).__init__()
        self.variance = variance

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = \frac{\sigma^2 \theta^2 +  \log(2 \pi \sigma^2)}{2} \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return (T.array[0] * T.array[0] * self.variance + log(2 * PI * self.variance)) / 2.0

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = \sigma^2 \theta \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVector(1)
        gradient.array[0] = self.variance * T.array[0]
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{H}) = \frac{\eta^2}{2 \sigma^2} \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return (H.array[0] * H.array[0]) / (2 * self.variance)

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G( \mathbf{H} ) = \frac{\eta}{\sigma^2} \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVector(1)
        gradient.array[0] = H.array[0] / self.variance
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
    # 	 * @return     \f$ k(x) = -\frac{x^2}{2 \sigma^2} \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return -(x.array[0] * x.array[0]) / (2 * self.variance)

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \mu \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} =	\frac{\mu}{\sigma^2} \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(1)
        T.array[0] = L.array[0] / self.variance
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} = \theta \sigma^2 \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(1)
        L.array[0] = T.array[0] * self.variance
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \lambda \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H} = \lambda \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  natural parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \eta \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;\mu,\sigma^2) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;\mu,\sigma^2) = \frac{1}{ \sqrt{2\pi \sigma^2} } \exp \left( - \frac{(x-\mu)^2}{ 2 \sigma^2} \right) \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return exp(-((x.array[0] - param.array[0]) * (x.array[0] - param.array[0])) / (2 * self.variance)) / (sqrt(2 * PI * self.variance))
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(UnivariateGaussianFixedVariance, self).density(x, param)
        else:
            return super(UnivariateGaussianFixedVariance, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = \lambda \f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        rand = Random()
        v = PVector(1)
        v.array[0] = rand.nextGaussian() * sqrt(self.variance)
        return v.Plus(L)

    # 
    # 	 * Computes the Kullback-Leibler divergence between two univariate Gaussian distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P\|f_Q) = \frac{(\mu_Q-\mu_P)^2}{2\sigma^2} \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        mP = LP.array[0]
        mQ = LQ.array[0]
        return ((mQ - mP) * (mQ - mP)) / (2 * self.variance)

